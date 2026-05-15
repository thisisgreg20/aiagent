import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
import math # Added import for math

from pkg.calculator import Calculator
from main import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("1+1"), 2)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("5-3"), 2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("2*3"), 6)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("6/3"), 2)

    def test_power(self):
        self.assertEqual(self.calculator.evaluate("2^3"), 8)

    def test_modulo(self):
        self.assertEqual(self.calculator.evaluate("7%3"), 1)

    def test_decimal(self):
        self.assertEqual(self.calculator.evaluate("1.5+2.5"), 4.0)

    def test_parentheses(self):
        self.assertEqual(self.calculator.evaluate("(1+2)*3"), 9)

    def test_variable_assignment_and_use(self):
        self.calculator.evaluate("x = 10")
        self.assertEqual(self.calculator.evaluate("x + 5"), 15)

    def test_function_call(self):
        self.assertAlmostEqual(self.calculator.evaluate("sin(0)"), 0.0)
        self.assertAlmostEqual(self.calculator.evaluate("cos(0)"), 1.0)

    def test_precedence(self):
        self.assertEqual(self.calculator.evaluate("2+3*4"), 14)
        self.assertEqual(self.calculator.evaluate(" (2+3)*4"), 20)

    def test_unsupported_operator(self):
        with self.assertRaisesRegex(ValueError, "Invalid token or undefined variable: #"):
            self.calculator.evaluate("1#2")

    def test_invalid_token(self):
        with self.assertRaisesRegex(ValueError, "Invalid token or undefined variable: @"):
            self.calculator.evaluate("1 + @")

    def test_mismatched_parentheses(self):
        with self.assertRaisesRegex(ValueError, "Mismatched parentheses"):
            self.calculator.evaluate("(1+2)*3)") # Corrected expression

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate(""))
        self.assertIsNone(self.calculator.evaluate("   "))

    def test_expression_with_variables(self):
        self.calculator.evaluate("a = 10")
        self.calculator.evaluate("b = 20")
        self.assertEqual(self.calculator.evaluate("a + b"), 30)

    def test_reassign_variable(self):
        self.calculator.evaluate("x = 10")
        self.calculator.evaluate("x = 20")
        self.assertEqual(self.calculator.evaluate("x"), 20)

    def test_variable_in_function(self):
        self.calculator.evaluate("y = 0")
        self.assertAlmostEqual(self.calculator.evaluate("sin(y)"), 0.0)

    def test_constant_pi(self):
        self.assertAlmostEqual(self.calculator.evaluate("pi"), math.pi)

    def test_constant_e(self):
        self.assertAlmostEqual(self.calculator.evaluate("e"), math.e)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Error: Division by zero."):
            self.calculator.evaluate("1 / 0")

    def test_negative_numbers(self):
        self.assertEqual(self.calculator.evaluate("-1 + 2"), 1)
        self.assertEqual(self.calculator.evaluate("3 * -2"), -6)

    def test_long_expression(self):
        self.assertAlmostEqual(self.calculator.evaluate("(1 + 2 * 3) / 7 + sin(pi/2)"), 2.0)

    def test_factorial(self):
        self.assertEqual(self.calculator.evaluate("factorial(5)"), 120)

    def test_erf_function(self):
        self.assertAlmostEqual(self.calculator.evaluate("erf(1)"), 0.8427007929497149)

    def test_tau_constant(self):
        self.assertAlmostEqual(self.calculator.evaluate("tau"), math.tau)

    def test_infinity(self):
        self.assertEqual(self.calculator.evaluate("inf + 1"), float("inf"))

    def test_nan(self):
        self.assertTrue(math.isnan(self.calculator.evaluate("nan * 2")))

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_command(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Calculator App - Interactive Mode", output)

    @patch('builtins.input', side_effect=['1 + 1', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_command_line_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn('{\n  "expression": "1 + 1",\n  "result": 2\n}', output)

    @patch('builtins.input', side_effect=['1 / 0', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero_prints_error(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn('Error: Division by zero.', output) # Updated expected error message

    @patch('builtins.input', side_effect=['abc', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_expression_prints_error(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn('Error: Invalid token or undefined variable: abc', output) # Updated expected error message

    @patch('builtins.input', side_effect=['x = 10', 'list_vars', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_vars_command(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Defined variables:", output)
        self.assertIn("x = 10.0", output)
    
    @patch('builtins.input', side_effect=['x = 10', 'clear_vars', 'list_vars', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_clear_vars_command(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("All variables cleared.", output)
        self.assertIn("No variables defined.", output)


if __name__ == '__main__':
    unittest.main()