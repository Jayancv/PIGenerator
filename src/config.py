import argparse
import os
import ollama
import os
from dotenv import load_dotenv


OPENSOURCE_MODELS = ["mistral", "wizardcoder", "deepseek-coder:33b-instruct", "codeqwen", "mixtral", "qwen"]

class Config:
    def __init__(self):

        load_dotenv()

        parser = argparse.ArgumentParser()
        parser.add_argument('--model', type=str, default="gpt-3.5-turbo")
        parser.add_argument('--version', type=str, default=None)
        parser.add_argument('--api_key', type=str, default=None)
        parser.add_argument('--base_url', type=str, default=None)
        parser.add_argument('--temperature', type=float, default=0.5)
        parser.add_argument('--retry', type=int, default=3)
        parser.add_argument("--use_rag",  type=bool, default=True)
        parser.add_argument("--task_id", type=int, default=1)

        self.args = parser.parse_args()

        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
        print (DEEPSEEK_API_KEY)
        if self.args.model in ["gpt-3.5-turbo", "gpt-4"]:
            os.environ["OPENAI_API_KEY"] = self.args.api_key if self.args.api_key else OPENAI_API_KEY
            self.args.api_key = os.getenv('OPENAI_API_KEY')
        elif self.args.model in ["deepseek-coder:33b-instruct","deepseek-reasoner","deepseek-chat"]:
            os.environ["DEEPSEEK_API_KEY"] = self.args.api_key if self.args.api_key else DEEPSEEK_API_KEY
            self.args.api_key = os.getenv('DEEPSEEK_API_KEY')
