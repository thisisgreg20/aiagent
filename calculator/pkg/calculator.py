import re

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None

        # Robust regex to tokenize:
        # 1. Matches numbers (positive, negative, and floating-point).
        # 2. Matches operators and parentheses.
        # 3. Matches any other sequence of non-whitespace characters as an invalid token.
        # The order in the regex ensures correct prioritization (numbers/operators before invalid tokens).
        tokens = re.findall(r'-?\d+\.?\d*|[+\-*/()]|\S+', expression)
        
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values)
                if not operators or operators[-1] != "(":
                    raise ValueError("Mismatched parentheses")
                operators.pop()  # Pop the '('
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    # If it's not an operator, parenthesis, or a number, it's an invalid token
                    raise ValueError(f"invalid token: {token}")

        while operators:
            if operators[-1] == "(":
                raise ValueError("Mismatched parentheses")
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
