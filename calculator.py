import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "You are attempting to divide by 0. Please try again."
    else:
        return x / y

def multiply(x, y):
    return x * y

def square(x):
    return x * x

def power(x, y):
    return x ** y

def sqrt(x):
    square_root = math.sqrt(x)
    return square_root

nine = sqrt(9)
print(nine)
