# Calculator App

This is a simple calculator application that can be run in two modes: interactive and command-line.

## How to use

### Interactive Mode

To start the calculator in interactive mode, simply run the `main.py` file without any arguments:

```bash
python main.py
```

In this mode, you can enter expressions one by one. The calculator will evaluate the expression and print the result. You can also use the following commands:

- `list_vars`: Lists all stored variables.
- `clear_vars`: Clears all stored variables.
- `exit` or `quit`: Exits the calculator.

Example:

```
> 2 + 2
{"expression": "2 + 2", "result": 4}
> x = 10
{"expression": "x = 10", "result": 10}
> x * 5
{"expression": "x * 5", "result": 50}
> list_vars
{"variables": {"x": 10}}
> exit
```

### Command-line Mode

To use the calculator in command-line mode, provide the expression as arguments when running the `main.py` file:

```bash
python main.py <expression>
```

The calculator will evaluate the expression and print the result, then exit. Variable management commands (`list_vars`, `clear_vars`) are not supported in command-line mode.

Example:

```bash
python main.py "10 / 2 + 3"
{"expression": "10 / 2 + 3", "result": 8}
```
