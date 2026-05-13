import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_file_path]
        if args != None:
            for arg in args:
                command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return f"No output produced"
        return f"STDOUT: {result.stdout} STDERR: {result.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file in a specified directory relative to the working directory, using the specified arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Target file path to be opened, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Required arguments to pass when running the python file.",
                items=type.Schema(type=types.Type.STRING)
            ),
        },
    ),
)