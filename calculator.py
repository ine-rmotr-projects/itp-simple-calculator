def add(x, y):
    if type(x) != int or type(y) != int:
        return None
    return x + y


def subtract(x, y):
    if type(x) != int or type(y) != int:
        return None
    return x - y


def divide(x, y):
    if y == 0:
        return ("can't divide by 0")
    return x / y


def multiply(x, y):
    if type(x) != int or type(y) != int:
        return None
    return x * y


def square(x):
    if type(x) != int:
        return None
    return x ** 2


def power(x, y):
    if type(x) != int or type(y) != int:
        return None
    return x ** y


def sqrt(x):
    if type(x) != int:
        return None
    return sqrt(x)
