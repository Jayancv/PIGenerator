import os
import json
from code_runner import CodeRunner
from helper import ensure_dir, write_file, append_file

class RetryHandler:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def execution_error_retry(self, messages, iterate, task_id, model_dir, error_info):
        with open('templates/execution_error.md', 'r', encoding='utf-8') as f:
            template = f.read()
        prompt = template.replace("[ERROR]", error_info)
        session_dir = f"{model_dir}/p{task_id}/{iterate}"
        ensure_dir(session_dir)
        append_file(f"{model_dir}/p{task_id}/execution_error_{iterate}", error_info)
        messages.append({"role": "user", "content": prompt})
        answer = self.llm_client.call_llm(messages)
        empty_code_error, raw_code = self.llm_client.extract_code(answer)
        input_path = f"{model_dir}/p{task_id}/p{task_id}_{iterate}_input.txt"
        output_path = f"{model_dir}/p{task_id}/p{task_id}_{iterate}_output.txt"
        write_file(input_path, json.dumps(messages))
        write_file(output_path, answer)
        code_path = f"{model_dir}/p{task_id}/{iterate}/p{task_id}_{iterate}.py"
        write_file(code_path, raw_code)
        execution_error, _, new_error_info, _ = CodeRunner.run_code(code_path)
        return execution_error, new_error_info, code_path

    def component_error_retry(self, messages, iterate, task_id, model_dir, user_input, code):
        with open('templates/component_check.md', 'r', encoding='utf-8') as f:
            template = f.read()
        prompt = template.replace("[USECASE]", user_input).replace("[CODE]", code)
        messages.append({"role": "user", "content": prompt})
        answer = self.llm_client.call_llm(messages)
        if "Correct" in answer:
            return 0, ""
        else:
            empty_code_error, raw_code = self.llm_client.extract_code(answer)
            code_path = f"{model_dir}/p{task_id}/{iterate}/p{task_id}_{iterate}.py"
            write_file(code_path, raw_code)
            return 1, code_path

    def pdf_generation(self, model_name, task_id, messages, code_path, retry_count):
        with open('templates/prompt_template_save.md', 'r', encoding='utf-8') as f:
            template = f.read()

        with open(code_path, 'r', encoding='utf-8') as code_file:
            code_content = code_file.read()

        prompt = template.replace('[CODE]', code_content)
        messages.append({"role": "user", "content": prompt})
        answer = self.llm_client.call_llm(messages)
        model_dir = self.llm_client.get_model_dir()
        if retry_count > 0:
            model_dir += f"_retry_{retry_count}"
        ensure_dir(f"{model_dir}/p{task_id}")
        iterate = 1
        empty_code_error, raw_code = self.llm_client.extract_code(answer)
        ensure_dir(f"{model_dir}/p{task_id}/{iterate}")
        input_path = f"{model_dir}/p{task_id}/p{task_id}_{iterate}_input.txt"
        output_path = f"{model_dir}/p{task_id}/p{task_id}_{iterate}_output.txt"
        write_file(input_path, prompt)
        write_file(output_path, answer)
        final_code_path = f"{model_dir}/p{task_id}/{iterate}/p{task_id}_final.py"
        write_file(final_code_path, raw_code)
