import argparse
import os

OPENSOURCE_MODELS = ["mistral", "wizardcoder", "deepseek-coder:33b-instruct", "codeqwen", "mixtral", "qwen"]

class Config:
    def __init__(self):
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
        self.args = parser.parse_args()
        os.environ[
            "OPENAI_API_KEY"] = r"sk-proj-123-EIcINIA"
        if any([model in self.args.model for model in OPENSOURCE_MODELS]):
            import ollama  # Import if using an open-source model
        if self.args.skill:
            self.args.num_of_retry = min(2, self.args.num_of_retry)
