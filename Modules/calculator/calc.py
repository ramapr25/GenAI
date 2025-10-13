"""The main program to run the calculator.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.function_bar()
"""

import math

print("in calc.py "  + __name__)

def mul(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers"""
    return a * b

def add(a: int | float, b: int | float) -> float:
    """Add two numbers (returns float). """
    return a + b

def div(a: int | float, b: int | float) -> float:
    """Divide two numbers (returns float). Raises ZeroDivisionError if b == 0"""
    return a / b

