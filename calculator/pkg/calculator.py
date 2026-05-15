import re
import math # Import math module
import json # Import json module
import os # Import os module

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
            "%": lambda a, b: a % b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3,
            "%": 2,
        }
        self.functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "abs": abs,
            "ceil": math.ceil,
            "floor": math.floor,
            "round": round,
            "exp": math.exp,
            "log10": math.log10,
            "degrees": math.degrees,
            "radians": math.radians,
            "atan2": math.atan2, # Added atan2
            "hypot": math.hypot, # Added hypot
            "trunc": math.trunc, # Added trunc
            "fmod": math.fmod, # Added fmod
            "modf": math.modf, # Added modf
            "copysign": math.copysign, # Added copysign
            "gamma": math.gamma, # Added gamma
            "lgamma": math.lgamma, # Added lgamma
            "factorial": math.factorial, # Added factorial
            "erf": math.erf, # Added erf
            "erfc": math.erfc, # Added erfc
        }
        self.constants = {
            "pi": math.pi,
            "e": math.e,
            "tau": math.tau, # Added tau
            "inf": math.inf, # Added inf
            "nan": math.nan, # Added nan
        }
        self.variables = {}
        self.variables_file = "variables.json"
        self._load_variables()

    def _load_variables(self):
        if os.path.exists(self.variables_file):
            with open(self.variables_file, "r") as f:
                try:
                    self.variables = json.load(f)
                except json.JSONDecodeError:
                    self.variables = {}

    def _save_variables(self):
        with open(self.variables_file, "w") as f:
            json.dump(self.variables, f)

    def list_variables(self):
        if self.variables:
            print("Defined variables:")
            for var, value in self.variables.items():
                print(f"  {var} = {value}")
        else:
            print("No variables defined.")

    def clear_variables(self):
        self.variables = {}
        self._save_variables()
        print("All variables cleared.")

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None

        # Check for variable assignment
        assignment_match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*)$', expression)
        if assignment_match:
            var_name = assignment_match.group(1)
            expr_to_evaluate = assignment_match.group(2)
            # Recursively evaluate the right-hand side of the assignment
            result = self.evaluate(expr_to_evaluate)
            if result is not None:
                self.variables[var_name] = result
                self._save_variables() # Save variables after assignment
                return result # Return the assigned value
            else:
                raise ValueError(f"Invalid assignment: {expression}")

        # Replace constants with their values before tokenization
        for const, value in self.constants.items():
            expression = re.sub(r'\b{}\b'.format(const), str(value), expression)
        
        # Update regex to include function names, and handle them as tokens
        # Variable names are handled in _evaluate_infix
        # Removed the optional minus from number regex to handle unary minus explicitly
        token_pattern = r'\b(?:sin|cos|tan|sqrt|log|abs|ceil|floor|round|exp|log10|degrees|radians|atan2|hypot|trunc|fmod|modf|copysign|gamma|lgamma|factorial|erf|erfc)\b|\d+\.?\d*|[+\-*/()%^()]|[a-zA-Z_][a-zA-Z0-9_]*|\S+'

        tokens = re.findall(token_pattern, expression)
        tokens = [token.strip() for token in tokens if token.strip()]

        try:
            return self._evaluate_infix(tokens)
        except ZeroDivisionError:
            raise ValueError("Error: Division by zero.")

    def _evaluate_infix(self, tokens):
        values = []
        operators = []
        
        # List of functions that require integer arguments
        integer_functions = ["factorial"]
        
        # Process tokens to handle unary minus
        processed_tokens = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '-' and (i == 0 or tokens[i-1] in ['('] + list(self.operators.keys())):
                # This is a unary minus
                if i + 1 < len(tokens):
                    next_token = tokens[i+1]
                    try:
                        # If the next token is a number, combine them
                        processed_tokens.append(str(-float(next_token)))
                        i += 1 # Skip the next token as it's been processed
                    except ValueError:
                        # If not a number, push the minus sign and let it be handled as an operator
                        processed_tokens.append(token)
                else:
                    raise ValueError("Invalid expression: unary minus without operand")
            else:
                processed_tokens.append(token)
            i += 1
        
        tokens = processed_tokens # Use processed tokens for evaluation

        for token in tokens:
            if token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values, integer_functions)
                if not operators or operators[-1] != "(":
                    raise ValueError("Mismatched parentheses")
                operators.pop()  # Pop the '('
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                    and (token != "^" or self.precedence[operators[-1]] > self.precedence[token]) 
                ):
                    self._apply_operator(operators, values, integer_functions)
                operators.append(token)
            elif token in self.functions: # Handle functions
                operators.append(token) # Push function onto operator stack
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    # If it's not an an operator, parenthesis, a function, or a number
                    # Check if it's a variable
                    if token in self.variables: 
                        values.append(float(self.variables[token]))
                    else:
                        # If it's none of the above, it's an invalid token
                        raise ValueError(f"Invalid token or undefined variable: {token}")

        while operators:
            if operators[-1] == "(":
                raise ValueError("Mismatched parentheses")
            self._apply_operator(operators, values, integer_functions)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values, integer_functions):
        if not operators:
            return

        operator = operators.pop()
        if operator in self.functions: # If it's a function, it only takes one operand
            if operator in ["atan2", "hypot", "fmod", "modf"]: # These functions take two arguments
                if len(values) < 2:
                    raise ValueError(f"not enough operands for function {operator}")
                b = values.pop()
                a = values.pop()
                # modf returns a tuple (fractional, integral), so we need to handle it.
                # For simplicity, we'll return the fractional part as the primary result.
                if operator == "modf":
                    fractional, integral = self.functions[operator](a)
                    values.append(fractional)
                else:
                    values.append(self.functions[operator](a, b))
            else: # All other functions take one argument
                if len(values) < 1:
                    raise ValueError(f"not enough operands for function {operator}")
                a = values.pop()
                if operator in integer_functions:
                    a = int(a) # Convert to int if the function requires it
                values.append(self.functions[operator](a))
        else:
            # Now only binary operators here, as unary minus is handled during token processing
            if len(values) < 2:
                raise ValueError(f"not enough operands for operator {operator}")
            b = values.pop()
            a = values.pop()
            values.append(self.operators[operator](a, b))
