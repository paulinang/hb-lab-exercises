"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

# import all functions from arithmetic module
from arithmetic import *

def process_input(input_string):
    try:
        tokens = input_string.split()
        operator = tokens[0]
        numlist = map(int, tokens[1:])
        return operator, numlist
    except ValueError: 
        print "Please use numbers after operator."
        return ['no_operator','no_numlist']
    except IndexError:
        print "Please type something in."
        return ['no_operator','no_numlist']

# make infinite loop
while True:
    # reads user input
    input_string = raw_input("> ")
    operator, numlist = process_input(input_string)

    # responses to different user inputs
    if operator == "q":
        break
    elif operator == "+":
        print add(numlist)
    elif operator == "-":
        print subtract(numlist)
    elif operator == "*":
        print multiply(numlist)
    elif operator == "/":
        print divide(numlist)
    elif operator == "square":
        print square(numlist) 
    elif operator == "cube":
        print cube(numlist)
    elif operator == "pow":
        print power(numlist)
    elif operator == "mod":
        print mod(numlist)
    else:
        print "I don't understand"
