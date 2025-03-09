import subprocess

class CodeRunner:
    @staticmethod
    def run_code(file_path):
        simulation_error = 0
        execution_error = 0
        execution_error_info = ""
        floating_node = ""
        try:
            result = subprocess.run(
                ["python", "-u", file_path],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=60
            )
            stdout_lines = result.stdout.splitlines()
            stderr_lines = result.stderr.splitlines()
            if len(stdout_lines) >= 2 and ("failed" in stdout_lines[-2] or "failed" in stdout_lines[-1]):
                if "check node" in stdout_lines[1]:
                    simulation_error = 1
                    floating_node = stdout_lines[1].split()[-1]
                else:
                    execution_error = 1
                    execution_error_info = CodeRunner.parse_error(stdout_lines)
            if len(stderr_lines) >= 2:
                if "check node" in stderr_lines[1]:
                    simulation_error = 1
                    floating_node = stderr_lines[1].split()[-1]
                else:
                    execution_error = 1
                    execution_error_info = CodeRunner.parse_error(stderr_lines)
            if simulation_error:
                execution_error = 0
            if not execution_error_info and execution_error:
                execution_error_info = "Simulation failed."
            if "error" in result.stdout.lower() and "<<NAN, error" not in result.stdout.lower() and not simulation_error:
                execution_error = 1
                execution_error_info = result.stdout + result.stderr
            return execution_error, simulation_error, execution_error_info, floating_node
        except subprocess.CalledProcessError as e:
            if "failed" in e.stdout and "check node" in e.stderr.splitlines()[1]:
                simulation_error = 1
            execution_error = 1
            execution_error_info = e.stdout + e.stderr
            if simulation_error:
                execution_error = 0
                execution_error_info = "Simulation failed."
            return execution_error, simulation_error, execution_error_info, floating_node
        except subprocess.TimeoutExpired:
            return 1, simulation_error, (
                "Time out error when running code.\n"
                "Suggestion: Avoid letting users input in Python code.\n"
            ), floating_node

    @staticmethod
    def parse_error(lines):
        error_info = ""
        for i in range(1, min(len(lines), 4)):
            line = lines[i]
            if "ERROR" in line or "Error" in line:
                error_info += line.split("ERROR")[-1] if "ERROR" in line else line.split("Error")[-1]
        return error_info

def start_tmux_session(session_name, command):
    subprocess.run(['tmux', 'new-session', '-d', '-s', session_name])
    subprocess.run(['tmux', 'send-keys', '-t', session_name, command, 'C-m'])
    print(f"Started tmux session '{session_name}' with command: {command}")

def kill_tmux_session(session_name):
    try:
        subprocess.run(['tmux', 'kill-session', '-t', session_name], check=True)
        print(f"Tmux session '{session_name}' killed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to kill tmux session '{session_name}'. It might not exist.")
