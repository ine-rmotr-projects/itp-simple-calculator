def add(x, y):
    x + y


def subtract(x, y):
    x - y


def divide(x, y):
    if y == 0:
        return 'invalid operation: division by 0'


def multiply(x, y):
    return x * y


def square(x):
    return x ** 2


def power(x, y):
    return x ** y


def sqrt(x):
    pow(x,1/2)
