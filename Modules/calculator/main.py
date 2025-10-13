# executable file
"""The main program to run the calculator.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.function_bar()
"""
#########################################################################
# from calc import (
#     mul,
#     div
# )
# print("in main.py " + __name__)
# print(mul(2,6))
# print(div(10,1))
#######################################################################

#Using Standard functions

import sys
import calc

if __name__ == '__main_':
    args = sys.argv[1::]
    print(args)
    if len(args) != 3:
        print("Not enough arguments passed")
    if args[0] == 'mul':
        print(calc.mul(int(args[1]), int(args[2]))) 



