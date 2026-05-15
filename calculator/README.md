# Calculator Application

This is a versatile calculator application that can perform a wide range of mathematical operations, from basic arithmetic to advanced calculus and linear algebra. It supports both interactive and command-line modes.

## Table of Contents
- [Basic Arithmetic Operations](#basic-arithmetic-operations)
- [Variable Assignment and Management](#variable-assignment-and-management)
- [Number Theory Functions](#number-theory-functions)
- [Trigonometric Functions](#trigonometric-functions)
- [Logarithmic Functions](#logarithmic-functions)
- [Special Functions](#special-functions)
- [Constants](#constants)
- [Complex Numbers](#complex-numbers)
- [Calculus Operations](#calculus-operations)
  - [Differentiation](#differentiation)
  - [Integration](#integration)
- [Linear Algebra Operations](#linear-algebra-operations)
  - [Matrix Creation](#matrix-creation)
  - [Matrix Addition and Subtraction](#matrix-addition-and-subtraction)
  - [Matrix Multiplication](#matrix-multiplication)
  - [Matrix Transpose](#matrix-transpose)
  - [Matrix Determinant](#matrix-determinant)
  - [Matrix Inverse](#matrix-inverse)
  - [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)

## Getting Started

To run the calculator in interactive mode, simply execute `main.py` without any arguments:

```bash
python main.py
```

To run the calculator in command-line mode, provide your expression as arguments:

```bash
python main.py "2 + 3 * 4"
```

## Basic Arithmetic Operations

The calculator supports standard arithmetic operations.

### Addition
```
> 5 + 3
```
Output:
```json
{
    "expression": "5 + 3",
    "result": 8.0
}
```

### Subtraction
```
> 10 - 4
```
Output:
```json
{
    "expression": "10 - 4",
    "result": 6.0
}
```

### Multiplication
```
> 6 * 7
```
Output:
```json
{
    "expression": "6 * 7",
    "result": 42.0
}
```

### Division
```
> 15 / 3
```
Output:
```json
{
    "expression": "15 / 3",
    "result": 5.0
}
```

### Exponentiation
```
> 2^3
```
Output:
```json
{
    "expression": "2^3",
    "result": 8.0
}
```

### Modulo
```
> 10 % 3
```
Output:
```json
{
    "expression": "10 % 3",
    "result": 1.0
}
```

### Round
Rounds a number to the nearest integer.
```
> round(3.7)
```
Output:
```json
{
    "expression": "round(3.7)",
    "result": 4.0
}
```
```
> round(3.2)
```
Output:
```json
{
    "expression": "round(3.2)",
    "result": 3.0
}
```

## Variable Assignment and Management

You can assign values to variables and use them in subsequent calculations.

### Assigning a variable
```
> x = 10
```
Output:
```json
{
    "expression": "x = 10",
    "result": 10.0
}
```

### Using a variable
```
> x * 5
```
Output:
```json
{
    "expression": "x * 5",
    "result": 50.0
}
```

### Listing variables
```
> list_vars
```
Output:
```
Current variables:
x = 10.0
```

### Clearing variables
```
> clear_vars
```
Output:
```
All variables cleared.
```

## Number Theory Functions

The calculator includes functions for common number theory operations.

### Greatest Common Divisor (GCD)
Calculates the greatest common divisor of two integers.
```
> gcd(12, 18)
```
Output:
```json
{
    "expression": "gcd(12, 18)",
    "result": 6.0
}
```

### Least Common Multiple (LCM)
Calculates the least common multiple of two integers.
```
> lcm(4, 6)
```
Output:
```json
{
    "expression": "lcm(4, 6)",
    "result": 12.0
}
```

## Trigonometric Functions

The calculator supports common trigonometric functions. Angles are assumed to be in radians.

### Sine
```
> sin(pi/2)
```
Output:
```json
{
    "expression": "sin(pi/2)",
    "result": 1.0
}
```

### Cosine
```
> cos(0)
```
Output:
```json
{
    "expression": "cos(0)",
    "result": 1.0
}
```

### Tangent
```
> tan(pi/4)
```
Output:
```json
{
    "expression": "tan(pi/4)",
    "result": 1.0
}
```

### Arcsine
```
> asin(1)
```
Output:
```json
{
    "expression": "asin(1)",
    "result": 1.5707963267948966
}
```

### Arccosine
```
> acos(0)
```
Output:
```json
{
    "expression": "acos(0)",
    "result": 1.5707963267948966
}
```

### Arctangent
```
> atan(1)
```
Output:
```json
{
    "expression": "atan(1)",
    "result": 0.7853981633974483
}
```

## Logarithmic Functions

The calculator supports natural logarithm and base-10 logarithm.

### Natural Logarithm (ln)
```
> ln(e)
```
Output:
```json
{
    "expression": "ln(e)",
    "result": 1.0
}
```

### Base-10 Logarithm (log10)
```
> log10(100)
```
Output:
```json
{
    "expression": "log10(100)",
    "result": 2.0
}
```

## Special Functions

### Factorial
Calculates the factorial of a non-negative integer. Note that for non-integer inputs, only the fractional part of the result is used in calculations. For example, `factorial(3.5)` will calculate `factorial(3)`.
```
> factorial(5)
```
Output:
```json
{
    "expression": "factorial(5)",
    "result": 120.0
}
```

```
> factorial(3.5)
```
Output:
```
Note: For factorial, only the integer part of the input is used. The fractional part will be ignored.
{"expression": "factorial(3.5)", "result": 6.0}
```

## Constants

Predefined mathematical and logical constants are available.

### Pi
```
> pi
```
Output:
```json
{
    "expression": "pi",
    "result": 3.141592653589793
}
```

### Euler's Number (e)
```
> e
```
Output:
```json
{
    "expression": "e",
    "result": 2.718281828459045
}
```

### True
```
> true
```
Output:
```json
{
    "expression": "true",
    "result": true
}
```

### False
```
> false
```
Output:
```json
{
    "expression": "false",
    "result": false
}
```

### Null
Represents an empty or non-existent value.
```
> null
```
Output:
```json
{
    "expression": "null",
    "result": null
}
```

## Complex Numbers

The calculator supports operations with complex numbers. Use `j` or `i` for the imaginary unit.

### Complex Number Addition
```
> (2 + 3j) + (1 - 2j)
```
Output:
```json
{
    "expression": "(2 + 3j) + (1 - 2j)",
    "result": "3 + 1j"
}
```

### Complex Number Multiplication
```
> (1 + j) * (2 - j)
```
Output:
```json
{
    "expression": "(1 + j) * (2 - j)",
    "result": "3 + 1j"
}
```

## Calculus Operations

The calculator can perform symbolic differentiation and definite integration.

### Differentiation

Use `diff(expression, variable)` for differentiation.

```
> diff(x^2, x)
```
Output:
```json
{
    "expression": "diff(x^2, x)",
    "result": "2*x"
}
```

```
> diff(sin(x), x)
```
Output:
```json
{
    "expression": "diff(sin(x), x)",
    "result": "cos(x)"
}
```

### Integration

Use `integrate(expression, variable, lower_limit, upper_limit)` for definite integration.

```
> integrate(x^2, x, 0, 1)
```
Output:
```json
{
    "expression": "integrate(x^2, x, 0, 1)",
    "result": 0.3333333333333333
}
```

```
> integrate(sin(x), x, 0, pi)
```
Output:
```json
{
    "expression": "integrate(sin(x), x, 0, pi)",
    "result": 2.0
}
```

## Linear Algebra Operations

The calculator supports various matrix operations. Matrices are represented as lists of lists.

### Matrix Creation

Matrices can be defined using square brackets.

```
> A = [[1, 2], [3, 4]]
```
Output:
```json
{
    "expression": "A = [[1, 2], [3, 4]]",
    "result": [[1.0, 2.0], [3.0, 4.0]]
}
```

### Matrix Addition and Subtraction

Matrices of the same dimensions can be added or subtracted.

#### Addition
```
> B = [[5, 6], [7, 8]]
> A + B
```
Output:
```json
{
    "expression": "A + B",
    "result": [[6.0, 8.0], [10.0, 12.0]]
}
```

#### Subtraction
```
> B = [[1, 1], [1, 1]]
> A - B
```
Output:
```json
{
    "expression": "A - B",
    "result": [[0.0, 1.0], [2.0, 3.0]]
}
```

### Matrix Multiplication

Use the `*` operator for matrix multiplication.

```
> A = [[1, 2], [3, 4]]
> B = [[2, 0], [1, 2]]
> A * B
```
Output:
```json
{
    "expression": "A * B",
    "result": [[4.0, 4.0], [10.0, 8.0]]
}
```

### Matrix Transpose

Use `transpose(matrix)` to get the transpose of a matrix.

```
> A = [[1, 2], [3, 4]]
> transpose(A)
```
Output:
```json
{
    "expression": "transpose(A)",
    "result": [[1.0, 3.0], [2.0, 4.0]]
}
```

### Matrix Determinant

Use `det(matrix)` to calculate the determinant of a square matrix.

```
> A = [[1, 2], [3, 4]]
> det(A)
```
Output:
```json
{
    "expression": "det(A)",
    "result": -2.0
}
```

### Matrix Inverse

Use `inv(matrix)` to calculate the inverse of a square matrix.

```
> A = [[1, 2], [3, 4]]
> inv(A)
```
Output:
```json
{
    "expression": "inv(A)",
    "result": [[-2.0, 1.0], [1.5, -0.5]]
}
```

### Eigenvalues and Eigenvectors

Use `eigen(matrix)` to find the eigenvalues and eigenvectors of a square matrix.

```
> A = [[2, 1], [1, 2]]
> eigen(A)
```
Output:
```json
{
    "expression": "eigen(A)",
    "result": {
        "eigenvalues": [3.0, 1.0],
        "eigenvectors": [
            [0.7071067811865476, -0.7071067811865476],
            [0.7071067811865476, 0.7071067811865476]
        ]
    }
}
