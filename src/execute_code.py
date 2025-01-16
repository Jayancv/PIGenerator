import unittest

from src.main_flow import run_code

def main():
    success_script = r"D:\Masters\LLM Project\PIGenerator\src\gpt3p5_retry_5\p20250105111054302608\1\p20250105111054302608_1_0.py"
    print("run")

    out = run_code(success_script)
    print(out)

if __name__ == "__main__":
    main()
