import math

def add(x, y):
    return sum([x, b])


def subtract(x, y):
    return x - y


def divide(x, y):
    if x or y == 0:
        return "Invalid value for denominator, cant't divide by 0!"
    else:
        return x / y

def multiply(x, y):
    return x * y


def square(x):
    return x ** 2

def power(x, y):
    return x ** y


def sqrt(x):
    return math.sqrt(x)
