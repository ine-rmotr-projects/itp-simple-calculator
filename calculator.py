def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
    try:
        return x/y
    except: return "Cannot be devided by y"

def multiply(x, y):
    return x*y


def square(x):
    x**2


def power(x, y):
    x**y


def sqrt(x):
    return power(x,(1/2))
    
