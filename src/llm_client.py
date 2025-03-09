import re
import time
import signal
import subprocess

import ollama
import openai
from config import OPENSOURCE_MODELS
from logger import setup_logger

logger = setup_logger('llm_client', 'logs/llm_client.log')

IMPORT_DWSIM = (
    'dwsimpath = "C:\\Users\\jcvid\\AppData\\Local\\DWSIM\\" \n'
    'clr.AddReference("System")\n'
    'clr.AddReference(dwsimpath + "CapeOpen.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.Automation.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.Interfaces.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.GlobalSettings.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.SharedClasses.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.Thermodynamics.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.Thermodynamics.ThermoC.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.UnitOperations.dll")\n'
    'clr.AddReference(dwsimpath + "DWSIM.Inspector.dll")\n'
    'clr.AddReference(dwsimpath + "System.Buffers.dll")'
)

class TimeoutException(Exception):
    pass

def signal_handler(signum, frame):
    raise TimeoutException("timeout")

class LLMClient:


    logger.debug("Initializing LLMClient")
    def __init__(self, config, client=None):
        self.config = config
        self.model = self.config.args.model
        self.temperature = self.config.args.temperature
        self.client = client or openai

    def extract_code(self, generated_content):
        if not generated_content:
            raise ValueError("Empty generated content")
        regex = r".*?```.*?\n(.*?)```"
        match = re.search(regex, generated_content, re.DOTALL)
        if match:
            code = "\n".join(line for line in match.group(1).splitlines() if line.strip())
        else:
            return 1, ""
        if "dwsimpath" not in code:
            code = IMPORT_DWSIM + "\n" + code
        return 0, code

    def call_llm(self, messages):
        if any(model in self.model for model in OPENSOURCE_MODELS):
            print("Using Ollama for completion")
            signal.signal(signal.SIGALRM, signal_handler)
            signal.alarm(360)
            try:
                completion = ollama.chat(
                    model=self.model,
                    messages=messages,
                    options={"temperature": self.temperature, "top_p": 1.0}
                )
                signal.alarm(0)
            except TimeoutException:
                signal.alarm(0)
                self.restart_ollama()
                time.sleep(120)
            answer = completion.choices[0].message.content
        else:
            try:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature
                )
                answer = completion.choices[0].message.content
            except openai.APIStatusError as e:
                print("APIStatusError encountered:", e)
                time.sleep(30)
                answer = ""

        return answer

    def get_model_dir(self):
        if "ft:gpt-3.5" in self.model:
            if "a:9HyyBpNI" in self.model:
                return "gpt3p5-ft-A"
            elif "b:9Hzb5l4S" in self.model:
                return "gpt3p5-ft-B"
            elif "c:9I0X557K" in self.model:
                return "gpt3p5-ft-C"
            else:
                return "unknown"
        elif "gpt-3" in self.model:
            return "gpt3p5"
        elif "gpt-4-turbo" in self.model:
            return "gpt4"
        elif "gpt-4o" in self.model:
            return "gpt4o"
        elif "deepseek-chat" in self.model:
            return "deepseek2"
        elif any(model in self.model for model in OPENSOURCE_MODELS):
            return self.model.replace(":", "-")
        return "unknown"

    def restart_ollama(self):
        from code_runner import kill_tmux_session, start_tmux_session
        kill_tmux_session("ollama")
        subprocess.run(['ollama', 'restart'], capture_output=True, text=True)
        start_tmux_session("ollama", "ollama serve")
