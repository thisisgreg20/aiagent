# 🤖 AI Assistant README

Hello! I am an AI assistant designed to help you with your coding tasks. I can interact with your file system, read and write files, and execute Python scripts. Think of me as your personal coding companion.

## ✨ Capabilities

I can perform the following actions:

*   **List Files and Directories:** Explore the contents of your working directory.
*   **Read File Content:** View the content of any file.
*   **Write/Overwrite Files:** Create new files or modify existing ones.
*   **Execute Python Files:** Run your Python scripts and see their output.

## 🚀 How to Use Me

I operate in a conversational loop. You give me instructions or ask questions, and I will try my best to fulfill them by executing a series of commands. I will always take the next logical step in our interaction, so you can guide me through complex tasks incrementally.

### General Interaction

You can ask me to do various things, such as:

*   "What files are in the current directory?"
*   "Read the contents of `my_script.py`."
*   "Create a new file called `hello.py` with `print('Hello, World!')`."
*   "Run `test_suite.py`."

### Understanding My Responses

When I perform an action, I will output the results. For example, when I list files, you will see a dictionary containing file information. When I read a file, you will see its content. When I run a Python script, you will see its standard output and any errors.

## 🛠️ Available Tools and Arguments

Here are the specific functions I can call to interact with your environment. You don't call these directly, but understanding them will help you formulate your requests.

### `get_files_info`

*   **Description:** Lists files and directories in a specified path.
*   **Arguments:**
    *   `directory` (str, optional): The directory path (relative to your working directory). Defaults to the current directory (`.`).
*   **Example Usage (from your perspective):**
    *   "List files in the current directory."
    *   "Show me the contents of the `src` folder."

### `get_file_content`

*   **Description:** Retrieves the content of a specified file.
*   **Arguments:**
    *   `file_path` (str, required): The path to the file (relative to your working directory).
*   **Example Usage (from your perspective):**
    *   "Read `main.py`."
    *   "What's inside `config/settings.ini`?"

### `run_python_file`

*   **Description:** Executes a Python script.
*   **Arguments:**
    *   `file_path` (str, required): The path to the Python file.
    *   `args` (list[str], optional): A list of string arguments to pass to the script.
*   **Example Usage (from your perspective):**
    *   "Run `my_script.py`."
    *   "Execute `process_data.py` with arguments `input.csv` and `output.json`."

### `write_file`

*   **Description:** Writes content to a file, overwriting it if it already exists.
*   **Arguments:**
    *   `file_path` (str, required): The path to the file.
    *   `content` (str, required): The text content to write.
*   **Example Usage (from your perspective):**
    *   "Create `new_file.txt` with the text 'Hello from AI!'."
    *   "Update `settings.py` to set `DEBUG = False`."

## 💡 Tips for Interaction

*   **Be Specific:** The more precise your instructions, the better I can understand and execute them.
*   **Break Down Complex Tasks:** For larger coding tasks, break them into smaller, manageable steps.
*   **Review My Output:** Always check my responses and the results of my actions to ensure everything is proceeding as expected.
*   **Ask for Clarification:** If you're unsure about something, just ask!

I'm here to help you code more efficiently. Let's build something great together!