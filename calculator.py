def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "Can't divide by zero."
    return x / y

def multiply(x, y):
    return x * y


def square(x):
    return x * x


def power(x, y):
    return x ** y


def sqrt(x):
    return power(x, 1/2)
