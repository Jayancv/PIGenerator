import os
import json
import pandas as pd
from datetime import datetime
import openai
from config import Config
from llm_client import LLMClient
from retry_handler import RetryHandler
from code_runner import CodeRunner, kill_tmux_session
# from src.rag import get_retrieved_details
from src.rag_sys import get_retrieved_details1

MAX_TOKENS = 16385


def cleanup_directory(model_dir, task_id, iterate):
    base_dir = f"{model_dir}/p{task_id}"
    if os.path.exists(base_dir):
        for file in os.listdir(base_dir):
            if file.endswith(".py") or file.endswith("_op.txt"):
                os.remove(os.path.join(base_dir, file))
    iter_dir = f"{base_dir}/{iterate}"
    if os.path.exists(iter_dir):
        for file in os.listdir(iter_dir):
            file_path = os.path.join(iter_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


def write_to_file(file_path, content, mode='w'):
    # Ensure the directory exists
    dir_path = os.path.dirname(file_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Write to the file
    with open(file_path, mode, encoding='utf-8') as file:
        file.write(content)


def work_flow(user_input, llm_client, problem_no):
    config = llm_client.config
    retry_count = config.args.retry
    use_rag = config.args.use_rag

    # **STEP 1: Retrieve Relevant Details using RAG**
    context = ""
    if use_rag:
        # retrieved_details = get_retrieved_details(user_input)
        retrieved_details = get_retrieved_details1(user_input,False)
        if retrieved_details:
            context = '\n'.join(
                f"Context {i + 1} \n {item['Description']} \n Sample python code \n {item['PythonCode']}" for i, item in
                enumerate(retrieved_details)
                if item['PythonCode']
            )
            print(context)
            if len(context) > MAX_TOKENS:
                total_length = sum(len(item['PythonCode']) for item in retrieved_details)
                print("Total length of PythonCodes:", total_length)
                if len(context) < MAX_TOKENS:
                    print("Context length exceeds the maximum limit. Summarising the context. Length = ", len(context))
                    context = ""
                    for i, item in enumerate(retrieved_details):
                        summary = llm_client.summarize(item['Description'])
                        context += f"Context {i + 1} \n {summary} \n Sample python code \n {item['PythonCode']}\n"
                else:
                    print("Select only top content from the retrieved details.")
                    context = f"Context 1 \n {retrieved_details[0]['Description']} \n Sample python code \n {retrieved_details[0]['PythonCode']}"
            if len(context) > MAX_TOKENS:
                print("Context length exceeds the maximum limit after summarising the context. length = ", len(context))
                # context = ""
        else:
            context = "No relevant context found in the dataset."
    else:
        context = "No RAG retrieval used."
    print("Context   = ", context)

    task_id = str(problem_no) + "_" + datetime.now().strftime('%Y%m%d%H%M%S%f')
    with open('templates/prompt_template.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    prompt = (prompt_template.replace('[CONTEXT]', context).replace('[INPUT]', user_input))

    messages = [
        {"role": "system", "content": "You are an Pipe and Instrumental diagram design expert."},
        {"role": "user", "content": prompt}
    ]

    answer = llm_client.call_llm(messages)

    model_dir = llm_client.get_model_dir()
    if retry_count > 0:
        model_dir += f"_retry_{retry_count}"
    os.makedirs(f"{model_dir}/p{task_id}", exist_ok=True)

    iterate = 1  # update later

    cleanup_directory(model_dir, task_id, iterate)

    input_path = '{}/p{}/p{}_{}_input.txt'.format(model_dir, task_id, task_id, iterate)
    output_path = '{}/p{}/p{}_{}_output.txt'.format(model_dir, task_id, task_id, iterate)

    write_to_file(input_path, prompt, 'a')
    write_to_file(output_path, answer, 'a')

    messages.append({"role": "assistant", "content": answer})

    empty_code_error, raw_code = llm_client.extract_code(answer)

    # iter_dir = f"{model_dir}/p{task_id}/{iterate}"
    # os.makedirs(iter_dir, exist_ok=True)
    # code_path = f"{iter_dir}/p{task_id}_{iterate}.py"
    # with open(code_path, 'w', encoding='utf-8') as f:
    #     f.write(raw_code)
    code_path = '{}/p{}/{}/p{}_{}.py'.format(model_dir, task_id, iterate, task_id, iterate)
    write_to_file(code_path, raw_code)

    # Error -> 1, Success -> 0
    if empty_code_error == 0:
        execution_error, simulation_error, error_info, floating_node = CodeRunner.run_code(code_path)
        print("execution_error = {}, simulation_error = {}".format(execution_error, simulation_error))
        print("execution_error = {}, info = {}".format(execution_error, error_info))
    else:
        execution_error = 0
        error_info = "Empty code generated."

    retry_handler = RetryHandler(llm_client)

    retry = False
    error_count = 0
    exe_err = False
    cmp_err = False
    final_code_path = code_path
    if execution_error == 1 or empty_code_error == 1:
        retry = True
        exe_err = True
        cmp_err = True

    if execution_error == 0:
        comp_error, comp_code_path = retry_handler.component_error_retry(messages, iterate, task_id, model_dir,
                                                                         user_input, raw_code)
        if comp_error == 1:
            execution_error = 1
            final_code_path = comp_code_path
            retry = True
            cmp_err = False  # because the new code didn't check with component error
            exe_err = True

    while retry and retry_count > 0:
        iterate += 1
        if exe_err:
            execution_error, error_info, final_code_path = retry_handler.execution_error_retry(messages, iterate,
                                                                                               task_id,
                                                                                               model_dir, error_info)

            if execution_error == 1:
                retry = True
                exe_err = True
            else:
                exe_err = False

        if (execution_error == 0 or exe_err) and cmp_err:
            comp_error, comp_code_path = retry_handler.component_error_retry(messages, iterate, task_id, model_dir,
                                                                             user_input, raw_code)
            if comp_error == 1:
                final_code_path = comp_code_path
                retry = True
                cmp_err = True  # because the new code didn't check with component error
                exe_err = True

        if not (exe_err or cmp_err):
            retry = False
            code_path = final_code_path
            break
        else:
            retry_count -= 1

    # if execution_error == 0:
    #     retry_handler.pdf_generation(model_dir, task_id, messages, final_code_path)
    retry_handler.pdf_generation(model_dir, task_id, messages, final_code_path)
    final_messages_path = f"{model_dir}/p{task_id}/p{task_id}_{iterate}_messages.txt"
    with open(final_messages_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(messages))
    return 0


def main():

    config = Config()
    llm_client = LLMClient(config)

    problem_no = 13
    if config.args.task_id > 0:
        problem_no = config.args.task_id
    with open('problems/problem' + str(problem_no) + '.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    df = pd.DataFrame(data, index=[0])

    input_prompt = df.loc[0, 'description']

    work_flow(input_prompt, llm_client, problem_no)


if __name__ == "__main__":
    main()
