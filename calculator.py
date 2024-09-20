def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0 :
        return invalid
    else :
        return x/y


def multiply(x, y):
    return x * y 


def square(x):
    return x ** 2


def power(x, y):
    return x ** y


def sqrt(x):
    return x ** 0.5

def calculator (choice, x , y ) :
    if choice == '1' : 
        return add(x, y)
    elif choice == '2':
        return subtract(x, y)
    elif choice == '3':
        return divide(x,y)
    elif choice == '4':
        return multiply(x, y)
    elif choice == '5':
        return square(x)
    elif choice == '6':
        return power(x, y)
    elif choice == '7':
        return sqrt(x)
    else:
        return error
