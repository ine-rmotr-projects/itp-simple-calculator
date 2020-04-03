def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "ERROR: Invalid denominator value. Unable to divide by 0"
    return x / y


def multiply(x, y):
    return x * y


def square(x):
    return x ** 2


def power(x, y):
    return pow(x, y)


def sqrt(x):
    return pow(x,1/2)
