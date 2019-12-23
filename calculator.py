def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y != 0:
        return x / y
    return 'Error, Divided by Zero'

def multiply(x, y):
    return x * y


def square(x):
    return x**2


def power(x, y):
    return x ** y


def sqrt(x):
    return power(x, 1/2)
