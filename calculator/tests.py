import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
import json

from pkg.calculator import Calculator
from pkg.render import format_json_output

# Mock sys.argv for testing main function

@patch('sys.stdout', new_callable=StringIO)
class TestMainFunction(unittest.TestCase):

    def setUp(self):
        # Clear sys.modules cache for 'main' to ensure a fresh import
        if 'main' in sys.modules:
            del sys.modules['main']

    @patch('sys.argv', ['main.py'])
    def test_no_arguments_prints_usage(self, mock_stdout):
        import main  # Import main here to use the patched sys.argv
        main.main()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn("Calculator App", output[0])
        self.assertIn("Usage:", output[1])

    @patch('sys.argv', ['main.py', '3', '+', '5'])
    def test_valid_expression_prints_json(self, mock_stdout):
        import main  # Import main here to use the patched sys.argv
        main.main()
        output = mock_stdout.getvalue().strip()
        # Parse the JSON output and assert its content
        parsed_output = json.loads(output)
        self.assertEqual(parsed_output, {"expression": "3 + 5", "result": 8})

    @patch('sys.argv', ['main.py', 'abc'])
    def test_invalid_expression_prints_error(self, mock_stdout):
        import main  # Import main here to use the patched sys.argv
        main.main()
        output = mock_stdout.getvalue().strip()
        self.assertIn('Error: invalid token: abc', output)

    @patch('sys.argv', ['main.py', '1', '/', '0'])
    def test_division_by_zero_prints_error(self, mock_stdout):
        import main  # Import main here to use the patched sys.argv
        main.main()
        output = mock_stdout.getvalue().strip()
        self.assertIn('Error: float division by zero', output)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("1 + 2"), 3)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("5 - 3"), 2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("2 * 4"), 8)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("6 / 3"), 2)

    def test_float_numbers(self):
        self.assertEqual(self.calculator.evaluate("1.5 + 2.5"), 4.0)

    def test_order_of_operations(self):
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14)
        self.assertEqual(self.calculator.evaluate("(2 + 3) * 4"), 20)

    def test_complex_expression(self):
        self.assertEqual(self.calculator.evaluate("10 - 2 * (6 / 3) + 1"), 7)

    def test_expression_with_spaces(self):
        self.assertEqual(self.calculator.evaluate(" 1   +  2 "), 3)

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate("   "))
        self.assertIsNone(self.calculator.evaluate(""))

    def test_invalid_token(self):
        with self.assertRaisesRegex(ValueError, "invalid token: @"):
            self.calculator.evaluate("1 + @")

    def test_mismatched_parentheses(self):
        with self.assertRaisesRegex(ValueError, "Mismatched parentheses"):
            self.calculator.evaluate("(1 + 2")
        with self.assertRaisesRegex(ValueError, "Mismatched parentheses"):
            self.calculator.evaluate("1 + 2)")

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "float division by zero"):
            self.calculator.evaluate("1 / 0")

class TestRender(unittest.TestCase):
    def test_format_json_output_integer_result(self):
        self.assertEqual(format_json_output("5 + 3", 8.0), '''{
  "expression": "5 + 3",
  "result": 8
}''')

    def test_format_json_output_float_result(self):
        self.assertEqual(format_json_output("5 / 2", 2.5), '''{
  "expression": "5 / 2",
  "result": 2.5
}''')

if __name__ == '__main__':
    unittest.main()
