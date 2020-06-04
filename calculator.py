def add(x, y):
    return x + y

$ py.test test_add.py


def subtract(x, y):
    return x - y

$ py.test test_subtract.py


def divide(x, y):
    if y == 0:
        return "Invalid value for denominator, cant't divide by 0!"
    return x / y
$ py.test test_divide.py


def multiply(x, y):
    return x * y

$ py.test test_multiply.py


def square(x):
    return x ** 2

$ py.test test_square.py


def power(x, y):
    return x ** y

$ py.test test_power.py


def sqrt(x):
    return x ** 0.5

$ py.test test_sqrt.py