import math  

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "Invalid value for denominator, cant't divide by 0!"
    else:
        return x / y


def multiply(x, y):
    return x * y


def square(x):
    return round(x ** 2)


def power(x, y):
    return round(x ** y)


def sqrt(x):
    return round(math.sqrt(x))