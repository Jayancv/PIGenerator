from datetime import datetime

from openai import OpenAI
import openai
import argparse
import re
import os
import subprocess
import time
import pandas as pd
import sys
import signal
import json


class TimeoutException(Exception):
    pass


def signal_handler(signum, frame):
    raise TimeoutException("timeout")


parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default="gpt-3.5-turbo")
parser.add_argument('--temperature', type=float, default=0.5)
parser.add_argument('--num_per_task', type=int, default=15)
parser.add_argument('--num_of_retry', type=int, default=3)
parser.add_argument("--num_of_done", type=int, default=0)
parser.add_argument("--task_id", type=int, default=1)
parser.add_argument("--ngspice", action="store_true", default=False)
parser.add_argument("--no_prompt", action="store_true", default=False)
parser.add_argument("--skill", action="store_true", default=False)
parser.add_argument("--no_context", action="store_true", default=False)
parser.add_argument("--no_chain", action="store_true", default=False)
parser.add_argument('--api_key', type=str, default="gpt-3.5-turbo")
parser.add_argument("--retrieval", action="store_true", default=False)

args = parser.parse_args()
os.environ[
    "OPENAI_API_KEY"] = r"Key"
opensource_models = ["mistral", "wizardcoder", "deepseek-coder:33b-instruct", "codeqwen", "mixtral", "qwen"]

if any([model in args.model for model in opensource_models]):
    import ollama
if args.skill:
    args.num_of_retry = min(2, args.num_of_retry)

complex_task_type = ['Oscillator', 'Integrator', 'Differentiator', 'Adder', 'Subtractor', 'Schmitt']
bias_usage = """Due to the operational range of the op-amp being 0 to 5V, please connect the nodes that were originally grounded to a 2.5V DC power source.
Please increase the gain as much as possible to maintain oscillation.
"""

import_dwsim = """
dwsimpath = "C:\\Users\\jcvid\\AppData\\Local\\DWSIM\\"
clr.AddReference("System")
clr.AddReference(dwsimpath + "CapeOpen.dll")
clr.AddReference(dwsimpath + "DWSIM.Automation.dll")
clr.AddReference(dwsimpath + "DWSIM.Interfaces.dll")
clr.AddReference(dwsimpath + "DWSIM.GlobalSettings.dll")
clr.AddReference(dwsimpath + "DWSIM.SharedClasses.dll")
clr.AddReference(dwsimpath + "DWSIM.Thermodynamics.dll")
clr.AddReference(dwsimpath + "DWSIM.Thermodynamics.ThermoC.dll")
clr.AddReference(dwsimpath + "DWSIM.UnitOperations.dll")
clr.AddReference(dwsimpath + "DWSIM.Inspector.dll")
clr.AddReference(dwsimpath + "System.Buffers.dll")
"""

openai.api_key = 'Key'
global client

client = OpenAI(
    api_key="Key")


# This function extracts the code from the generated content which in markdown format
def extract_code(generated_content):
    empty_code_error = 0
    assert generated_content != "", "generated_content is empty"
    regex = r".*?```.*?\n(.*?)```"
    matches = re.finditer(regex, generated_content, re.DOTALL)
    first_match = next(matches, None)
    try:
        code = first_match.group(1)
        print("code", code)
        code = "\n".join([line for line in code.split("\n") if len(line.strip()) > 0])
    except:
        code = ""
        empty_code_error = 1
        return empty_code_error, code
    # Add necessary libraries

    if "dwsimpath" not in code:
        code = import_dwsim + " \n " + code

    new_code = ""
    for line in code.split("\n"):
        new_code += line + "\n"
        # if "circuit.simulator()" in line:
        #     break

    return empty_code_error, new_code


def run_code(file):
    print("IN RUN_CODE : {}".format(file))
    simulation_error = 0
    execution_error = 0
    execution_error_info = ""
    floating_node = ""
    try:
        print("-----------------running code-----------------")
        print("file:", file)
        result = subprocess.run(["python", "-u", file], check=True, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        print("num of lines", len(result.stdout.split("\n")))
        print("num of error lines", len(result.stderr.split("\n")))
        print(result.stderr)
        print(result.stdout)
        if len(result.stdout.split("\n")) >= 2 and (
                "failed" in result.stdout.split("\n")[-2] or "failed" in result.stdout.split("\n")[-1]):
            if len(result.stdout.split("\n")) >= 2:
                if "check node" in result.stdout.split("\n")[1]:
                    simulation_error = 1
                    floating_node = result.stdout.split("\n")[1].split()[-1]
                else:
                    execution_error = 1
                    if "ERROR" in result.stdout.split("\n")[1]:
                        execution_error_info = "ERROR" + result.stdout.split("\n")[1].split("ERROR")[-1]
                    elif "Error" in result.stdout.split("\n")[1]:
                        execution_error_info = "Error" + result.stdout.split("\n")[1].split("Error")[-1]
                    if len(result.stdout.split("\n")) >= 3 and "ERROR" in result.stdout.split("\n")[2]:
                        execution_error_info += "\nERROR" + result.stdout.split("\n")[2].split("ERROR")[-1]
                    elif len(result.stdout.split("\n")) >= 3 and "Error" in result.stdout.split("\n")[2]:
                        execution_error_info += "\nError" + result.stdout.split("\n")[2].split("Error")[-1]
                    if len(result.stdout.split("\n")) >= 4 and "ERROR" in result.stdout.split("\n")[3]:
                        execution_error_info += "\nERROR" + result.stdout.split("\n")[3].split("ERROR")[-1]
                    elif len(result.stdout.split("\n")) >= 4 and "Error" in result.stdout.split("\n")[3]:
                        execution_error_info += "\nError" + result.stdout.split("\n")[3].split("Error")[-1]
            if len(result.stderr.split("\n")) >= 2:
                if "check node" in result.stderr.split("\n")[1]:
                    simulation_error = 1
                    floating_node = result.stderr.split("\n")[1].split()[-1]
                else:
                    execution_error = 1
                    if "ERROR" in result.stderr.split("\n")[1]:
                        execution_error_info = "ERROR" + result.stderr.split("\n")[1].split("ERROR")[-1]
                    elif "Error" in result.stderr.split("\n")[1]:
                        execution_error_info = "Error" + result.stderr.split("\n")[1].split("Error")[-1]
                    if len(result.stdout.split("\n")) >= 3 and "ERROR" in result.stderr.split("\n")[2]:
                        execution_error_info += "\nERROR" + result.stderr.split("\n")[2].split("ERROR")[-1]
                    elif len(result.stdout.split("\n")) >= 3 and "Error" in result.stdout.split("\n")[2]:
                        execution_error_info += "\nError" + result.stdout.split("\n")[2].split("Error")[-1]
                    if len(result.stdout.split("\n")) >= 4 and "ERROR" in result.stderr.split("\n")[3]:
                        execution_error_info += "\nERROR" + result.stderr.split("\n")[3].split("ERROR")[-1]
                    elif len(result.stdout.split("\n")) >= 4 and "Error" in result.stderr.split("\n")[3]:
                        execution_error_info += "\nError" + result.stderr.split("\n")[3].split("Error")[-1]
            if simulation_error == 1:
                execution_error = 0
            if execution_error_info == "" and execution_error == 1:
                execution_error_info = "Simulation failed."
        code_content = open(file, "r").read()
        if "error" in result.stdout.lower() and not "<<NAN, error".lower() in result.stdout.lower() and simulation_error == 0:
            execution_error = 1
            execution_error_info = result.stdout + result.stderr
        return execution_error, simulation_error, execution_error_info, floating_node
    except subprocess.CalledProcessError as e:
        print(f"error when running: {e}")
        print("stderr", e.stderr, file=sys.stderr)
        if "failed" in e.stdout:
            if len(e.stderr.split("\n")) >= 2:
                if "check node" in e.stderr.split("\n")[1]:
                    simulation_error = 1
                    floating_node = e.stderr.split("\n")[1].split()[-1]
        execution_error = 1

        execution_error_info = e.stdout + e.stderr
        if simulation_error == 1:
            execution_error = 0
            execution_error_info = "Simulation failed."
        return execution_error, simulation_error, execution_error_info, floating_node
    except subprocess.TimeoutExpired:
        print(f"Time out error when running code.")
        execution_error = 1
        execution_error_info = "Time out error when running code.\n"
        execution_error_info = "Suggestion: Avoid letting users input in Python code.\n"
        return execution_error, simulation_error, execution_error_info, floating_node


def start_tmux_session(session_name, command):
    subprocess.run(['tmux', 'new-session', '-d', '-s', session_name])
    subprocess.run(['tmux', 'send-keys', '-t', session_name, command, 'C-m'])
    print(f"tmux session '{session_name}' started, running command: {command}")


def kill_tmux_session(session_name):
    try:
        subprocess.run(['tmux', 'kill-session', '-t', session_name], check=True)
        print(f"tmux session '{session_name}' has been killed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to kill tmux session '{session_name}'. Session might not exist.")


def call_LLM(client, messages, model_name):
    if any(model in model_name for model in opensource_models):  # TODO need to support opensource models
        print(f"start {args.model} completion")
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(360)
        try:
            completion = ollama.chat(
                model=model_name,
                messages=messages,
                options={
                    "temperature": args.temperature,
                    "top_p": 1.0,
                    # "num_predict": 16192,
                })
            print(f"{model_name} completion finish")
            signal.alarm(0)

        except TimeoutException as e:
            print(e)
            print("timeout")
            signal.alarm(0)
            print("restart ollama")
            kill_tmux_session("ollama")
            result = subprocess.run(['ollama', 'restart'], capture_output=True, text=True)
            start_tmux_session("ollama", "ollama serve")
            time.sleep(120)
    else:
        try:
            print(messages)
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=args.temperature
            )

        except openai.APIStatusError as e:
            print("Encountered an APIStatusError. Details:")
            print(e)
            print("sleep 30 seconds")
            time.sleep(30)
    if "gpt" in model_name or "deepseek-chat" in model_name:
        answer = completion.choices[0].message.content
    else:
        answer = completion['message']['content']
    return answer


def get_model_dir(model_name):
    if "ft:gpt-3.5" in model_name:
        if "a:9HyyBpNI" in args.model:
            model_dir = "gpt3p5-ft-A"
        elif "b:9Hzb5l4S" in args.model:
            model_dir = "gpt3p5-ft-B"
        elif "c:9I0X557K" in args.model:
            model_dir = "gpt3p5-ft-C"
        else:
            model_dir = 'unknown'
    elif "gpt-3" in model_name:
        model_dir = 'gpt3p5'
    elif "gpt-4-turbo" in model_name:
        model_dir = 'gpt4'
    elif "gpt-4o" in model_name:
        model_dir = 'gpt4o'
    elif "deepseek-chat" in model_name:
        model_dir = "deepseek2"
    elif any(model in model_name for model in opensource_models):
        model_dir = str(model_name).replace(":", "-")
    else:
        model_dir = 'unknown'

    return model_dir


def execution_error_retry_loop(model_name, messages, iterate, task_id, model_dir, execution_error_info):
    fopen_exe_error = open('templates/execution_error.md', 'r')
    prompt_exe_error = fopen_exe_error.read()
    fopen_exe_error.close()

    new_prompt = prompt_exe_error.replace("[ERROR]", execution_error_info)

    if not os.path.exists("{}/p{}/{}".format(model_dir, task_id, iterate)):
        os.mkdir("{}/p{}/{}".format(model_dir, task_id, iterate))

    ftmp = open("{}/p{}/{}/execution_error_{}".format(model_dir, task_id, iterate, iterate), "a", encoding='utf-8')
    ftmp.write(execution_error_info)
    ftmp.close()

    messages.append({"role": "user", "content": new_prompt})
    answer = call_LLM(client, messages, model_name)

    print("Answer: ")
    print(answer)
    model_dir = get_model_dir(model_name)

    empty_code_error, raw_code = extract_code(answer)

    fwrite_input = open('{}/p{}/p{}_{}_input.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_input.write(messages)
    fwrite_input.flush()
    fwrite_output = open('{}/p{}/p{}_{}_output.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_output.write(answer)
    fwrite_output.flush()

    code_path = '{}/p{}/{}/p{}_{}.py'.format(model_dir, task_id, iterate, task_id, iterate)
    fwrite_code = open(code_path, 'w', encoding='utf-8')
    fwrite_code.write(raw_code)
    fwrite_code.close()

    execution_error, simulation_error, execution_error_info, floating_node = run_code(code_path)
    print("execution_error = {}, simulation_error = {}".format(execution_error, simulation_error))
    print("execution_error = {}, info = {}".format(execution_error, execution_error_info))

    return execution_error, execution_error_info, code_path


def component_error_retry_loop(model_name, messages, iterate, task_id, model_dir, input, code):
    fopen_exe_error = open('templates/component_check.md', 'r')
    prompt_exe_error = fopen_exe_error.read()
    fopen_exe_error.close()

    new_prompt = prompt_exe_error.replace("[USECASE]", input).replace("[CODE]", code)

    messages.append({"role": "user", "content": new_prompt})

    answer = call_LLM(client, messages, model_name)

    print("Answer: ")
    print(answer)

    if not os.path.exists("{}/p{}/{}".format(model_dir, task_id, iterate)):
        # try:
        os.mkdir("{}/p{}/{}".format(model_dir, task_id, iterate))

    fwrite_input = open('{}/p{}/p{}_{}_input.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_input.write(new_prompt)
    fwrite_input.flush()
    fwrite_output = open('{}/p{}/p{}_{}_output.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_output.write(answer)
    fwrite_output.flush()

    if ("Correct" in answer):
        component_error = 0
        return component_error, ""

    else:
        # items = answer.splitlines()
        # component_error = len(items)
        # missing_components = answer
        empty_code_error, raw_code = extract_code(answer)
        component_error = 1
        code_path = '{}/p{}/{}/p{}_{}.py'.format(model_dir, task_id, iterate, task_id, iterate)
        fwrite_code = open(code_path, 'w', encoding='utf-8')
        fwrite_code.write(raw_code)
        fwrite_code.close()

        print("component_error = {} ".format(component_error))
        print("missing_components = {}".format(raw_code))

        return component_error, code_path






def pdf_generation(model_name, task_id, messages, code, retry_count):
    fopen_pdf_save = open('templates/prompt_template_save.md', 'r')
    prompt_pdf_save = fopen_pdf_save.read()
    fopen_pdf_save.close()
    prompt = prompt_pdf_save.replace('[CODE]', code)
    messages.append({"role": "user", "content": prompt})

    answer = call_LLM(client, messages, model_name)

    print("Answer: ")
    print(answer)
    model_dir = get_model_dir(model_name)

    if retry_count > 0:
        model_dir += "_retry_{}".format(retry_count)

    if not os.path.exists(model_dir):
        try:
            os.mkdir(model_dir)
        except:
            pass
    if not os.path.exists('{}/p{}'.format(model_dir, task_id)):
        try:
            os.mkdir('{}/p{}'.format(model_dir, task_id))
        except:
            pass

    iterate = 1  # update later
    empty_code_error, raw_code = extract_code(answer)

    if not os.path.exists("{}/p{}/{}".format(model_dir, task_id, iterate)):
        # try:
        os.mkdir("{}/p{}/{}".format(model_dir, task_id, iterate))

    code = raw_code
    fwrite_input = open('{}/p{}/p{}_{}_input.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_input.write(prompt)
    fwrite_input.flush()
    fwrite_output = open('{}/p{}/p{}_{}_output.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_output.write(answer)
    fwrite_output.flush()

    code_path = '{}/p{}/{}/p{}_final.py'.format(model_dir, task_id, iterate, task_id)
    fwrite_code = open(code_path, 'w', encoding='utf-8')
    fwrite_code.write(raw_code)
    fwrite_code.close()


def work(input, background, model_name, client, retry_count):
    global generator
    task_id = str(datetime.now().strftime('%Y%m%d%H%M%S%f'))
    total_tokens = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0

    output = ""

    fopen = open('templates/prompt_template.md', 'r')
    prompt = fopen.read()
    prompt = prompt.replace('[KEYWORDS]', background)
    prompt = prompt.replace('[INPUT]', input)
    prompt = prompt.replace('[OUTPUT]', output)
    fopen.close()

    messages = [
        {"role": "system", "content": "You are an Pipe and Instrumental diagram design expert."},
        {"role": "user", "content": prompt}
    ]
    retry = True

    print(args)

    ## First hit
    answer = call_LLM(client, messages, model_name)

    print("Answer: ")
    print(answer)

    model_dir = get_model_dir(model_name)

    if retry_count > 0:
        model_dir += "_retry_{}".format(retry_count)

    if not os.path.exists(model_dir):
        try:
            os.mkdir(model_dir)
        except:
            pass
    if not os.path.exists('{}/p{}'.format(model_dir, task_id)):
        try:
            os.mkdir('{}/p{}'.format(model_dir, task_id))
        except:
            pass

    iterate = 1  # update later

    # delete files
    existing_code_files = os.listdir("{}/p{}".format(model_dir, task_id))
    for existing_code_file in existing_code_files:
        if existing_code_file.endswith(".py"):
            os.remove("{}/p{}/{}".format(model_dir, task_id, existing_code_file))
            print("remove file: ", existing_code_file)
        if existing_code_file.endswith("_op.txt"):
            os.remove("{}/p{}/{}".format(model_dir, task_id, existing_code_file))
            print("remove file: ", existing_code_file)

    if os.path.exists("{}/p{}/{}".format(model_dir, task_id, iterate)):
        existing_code_files = os.listdir("{}/p{}/{}".format(model_dir, task_id, iterate))
        for existing_code_file in existing_code_files:
            if os.path.isfile("{}/p{}/{}/{}".format(model_dir, task_id, iterate, existing_code_file)):
                try:
                    os.remove("{}/p{}/{}/{}".format(model_dir, task_id, iterate, existing_code_file))
                except:
                    pass
                print("remove file: ", existing_code_file)

    if not os.path.exists("{}/p{}/{}".format(model_dir, task_id, iterate)):
        # try:
        os.mkdir("{}/p{}/{}".format(model_dir, task_id, iterate))
        # except:
        #     pass
    messages.append({"role": "assistant", "content": answer})

    empty_code_error, raw_code = extract_code(answer)

    fwrite_input = open('{}/p{}/p{}_{}_input.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_input.write(prompt)
    fwrite_input.flush()

    fwrite_output = open('{}/p{}/p{}_{}_output.txt'.format(model_dir, task_id, task_id, iterate), 'a', encoding='utf-8')
    fwrite_output.write(answer)
    fwrite_output.flush()

    code_path = '{}/p{}/{}/p{}_{}.py'.format(model_dir, task_id, iterate, task_id, iterate)
    fwrite_code = open(code_path, 'w', encoding='utf-8')
    fwrite_code.write(raw_code)
    fwrite_code.close()

    if empty_code_error < 1:
        # Code execution
        execution_error, simulation_error, execution_error_info, floating_node = run_code(code_path)
        print("execution_error = {}, simulation_error = {}".format(execution_error, simulation_error))
        print("execution_error = {}, info = {}".format(execution_error, execution_error_info))

    retry = False
    error_count = 0

    if execution_error > 0 or empty_code_error > 0:
        retry = True
        exe_err = True
    else:
        messages.append({"role": "user", "content": answer})
        component_error, code_path = component_error_retry_loop(model_name, messages, iterate, task_id,
                                                                model_dir, input, raw_code)
        if component_error > 0:
            retry = True
            cmp_err = False  # because the new code didn't check with component error
            exe_err = True

    exe_err = False
    cmp_err = False
    error_info = execution_error_info
    final_code_path = code_path

    while retry and retry_count > 0:
        iterate += 1

        if exe_err:
            error_count, error_info, final_code_path = execution_error_retry_loop(model_name, messages, iterate,
                                                                                  task_id,
                                                                                  model_dir, error_info)

        if cmp_err:
            error_count, missing_components = component_error_retry_loop(model_name, messages, iterate, task_id,
                                                                         model_dir, input, raw_code)

        if error_count < 1:
            retry = False
            code_path = final_code_path
            break
        else:
            retry_count = retry_count - 1

    if error_count < 1:
        print("PDF generation")
        pdf_generation(model_name, task_id, messages, code_path, retry_count)

    # save messages
    fwrite = open('{}/p{}/p{}_{}_messages.txt'.format(model_dir, task_id, iterate, task_id, iterate), 'w',
                  encoding='utf-8')
    fwrite.write(str(messages))
    fwrite.close()
    fwrite_input.close()
    fwrite_output.close()
    return 0


def main():
    with open('problem3.json') as f:
        data = json.load(f)
    df = pd.DataFrame(data, index=[0])

    model_name = df.loc[0, 'model']
    input_prompt = df.loc[0, 'description']
    keywords = df.loc[0, 'keywords']
    api_key = df.loc[0, 'api_key']
    retry = df.loc[0, 'retry_count']
    print(model_name)

    if "gpt" in model_name:
        client = OpenAI(api_key=api_key)
        print("gpt client created...")
    elif "deepseek-chat" in model_name:
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")
        print("deepseek client created...")
    else:
        client = None
        print("no model found.")
    remaining_money = work(input_prompt, keywords, model_name, client, retry)


if __name__ == "__main__":
    main()
