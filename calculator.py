def add(x, y):
	if (type(x) != int or type(y) != int):
		return None
	else :
		return x+y


def subtract(x, y):
	if (type(x) != int or type(y) != int):
		return None
	else :
		return x-y


def divide(x, y):
	if y == 0:
		return "Invalid value for denominator, cant't divide by 0!"
	elif (type(x) != int or type(y) != int):
		return None
	else :
		return x/y


def multiply(x, y):
	if (type(x) != int or type(y) != int):
		return None
	else :
		return x*y


def square(x):
	if (type(x) != int):
		return None
	else :
		return round(x**2,3)


def power(x, y):
	if (type(x) != int or type(y) != int):
		return None
	else :
		return round(x**y,3)


def sqrt(x):
	if (type(x) != int):
		return None
	else :
		return round(x**(0.5),3)