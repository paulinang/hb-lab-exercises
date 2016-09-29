def add(numlist):
    total = 0
    for num in numlist:
        total += num
    return total


def subtract(numlist):
    difference = numlist[0]
    for num in numlist[1:]:
        difference -= num
    return difference


def multiply(numlist):
    product = 1
    for num in numlist:
        product = product * num
    return product        

def divide(numlist):
    # Need to turn at least argument to float for division to
    # not be integer division
    quotient = float(numlist[0])
    for num in numlist[1:]:
        quotient = quotient / num
    return quotient 


def square(numlist):
    squares = []
    for num in numlist:
       squares.append(num ** 2)
    return squares


def cube(numlist):
    cubes = []
    for num in numlist:
        cubes.append(num ** 3)
    return cubes


def power(numlist):
    final_powered = numlist[0]
    for num in numlist[1:]:
        final_powered = final_powered ** num
    return final_powered  # ** = exponent operator


def mod(numlist):
    final_remainder = numlist[0]
    for num in numlist[1:]:
        final_remainder = final_remainder % num
    return final_remainder