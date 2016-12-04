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
        command = tokens[0]
        numlist = map(int, tokens[1:])
        return command, numlist
    except ValueError: 
        print "Please use numbers after operator."
        return ["error","error"]
    except IndexError:
        print "Please type something in."
        return ["error","error"]

operator_list = ["q", "+", "-", "*", "/", "square", "cube", "pow", "mod"]

# make infinite loop
while True:
    # reads user input
    input_string = raw_input("> ")
    command, numlist = process_input(input_string)

    if not command in operator_list:
        print "Please type in correct command. \nTry again."
    elif command == "q":
        break
    elif len(numlist) == 0:
        print "Please give a number after operator."
    elif command == "+":
        print add(numlist)
    elif command == "-":
        print subtract(numlist)
    elif command == "*":
        print multiply(numlist)
    elif command == "/":
        print divide(numlist)
    elif command == "square":
        print square(numlist) 
    elif command == "cube":
        print cube(numlist)
    elif command == "pow":
        print power(numlist)
    elif command == "mod":
        print mod(numlist)
    elif command == "error":
        print "Try again."
    else:
        print "Please type in a command first. \nTry again."
