import math
def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
    if y==0:
        return "Denominator cannot be zero at any cost!"
    else:
    return x/y


def multiply(x, y):
    return x*y


def square(x):
    x **= 2
    return x


def power(x, y):
    res=x**y
    return res

def sqrt(x):
    y=math.sqrt(x)
    return y
