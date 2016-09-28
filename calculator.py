"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

# import all functions from arithmetic module
from arithmetic import *


# make infinite loop
while True:
    # reads user input
    input_string = raw_input("> ")
    # tokenizes input
    tokens = input_string.split()

    # changes str to int based on number of tokens
    if len(tokens) == 2:
        num1 = int(tokens[1])
    elif len(tokens) == 3:
        num1 = int(tokens[1])
        num2 = int(tokens[2])

    # responses to different user inputs
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
        print add(num1, num2)
    elif tokens[0] == "-":
        print subtract(num1, num2)
    elif tokens[0] == "*":
        print multiply(num1, num2)
    elif tokens[0] == "/":
        print divide(num1, num2)
    elif tokens[0] == "square":
        print square(num1) 
    elif tokens[0] == "cube":
        print cube(num1)
    elif tokens[0] == "pow":
        print power(num1, num2)
    elif tokens[0] == "mod":
        print mod(num1, num2)
    else:
        print "I don't understand"
