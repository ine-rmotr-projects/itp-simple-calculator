def add(x, y):
    addition = 0
    addition = int(x + y)
    return addition


def subtract(x, y):
    subtraction = 0
    subtraction = int(x - y)
    return subtraction


def divide(x, y):
    division = 0
    if x == 0 or y ==0:
        division = "Error - cannot divide by zero!"
        return division
    else:
        division = int(x / y)
    return division

def multiply(x, y):
    multiplication = 0
    multiplication = int(x * y)
    return multiplication

def square(x):
    squared = 0
    squared = int(abs(x ** 2))
    return squared

def power(x, y):
    exponent = 0
    exponent = int(x ** (y))
    return exponent

def sqrt(x):
    square_root = 0
    square_root = int(x **(.5))
    return square_root