import sys
import os

from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    calculator = Calculator()

    if len(sys.argv) <= 1:
        # Interactive mode
        print("Calculator App - Interactive Mode")
        print("Enter 'exit' or 'quit' to end the session.")
        while True:
            try:
                expression = input("> ")
                if expression.lower() in ['exit', 'quit']:
                    calculator._save_variables() # Save variables before exiting
                    break
                if expression.lower() == 'list_vars':
                    calculator.list_variables()
                    continue
                if expression.lower() == 'clear_vars':
                    calculator.clear_variables()
                    continue
                if not expression.strip():
                    continue

                result = calculator.evaluate(expression)
                if result is not None:
                    to_print = format_json_output(expression, result)
                    print(to_print)
                else:
                    print("Error: Expression is empty or contains only whitespace.")
            except Exception as e:
                print(f"Error: {e}")
    else:
        # Command-line mode
        expression = " ".join(sys.argv[1:])
        try:
            # For command line mode, we'll only support evaluation, not variable management commands
            result = calculator.evaluate(expression)
            if result is not None:
                to_print = format_json_output(expression, result)
                print(to_print)
            else:
                print("Error: Expression is empty or contains only whitespace.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
