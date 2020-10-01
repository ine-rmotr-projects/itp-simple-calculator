def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation: ")
print("1.Add", " 2.Subtract"," 3.Multiply"," 4.Divide",)

while True:
    
    choose = input("Enter numberinput(1/2/3/4): ")
    numberinput = choose

    if numberinput in ('1', '2', '3', '4',):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if numberinput == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif numberinput == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif numberinput == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif numberinput == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
       
        break
    else:
        print("Error")
