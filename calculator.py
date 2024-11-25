def add(a,b):
    return a + b 

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print("**************************************************")
print("Welcome to the calculator app")
print()

while True:
    try:
        user = int(input("Pick a number of the ones below \n1.Add \n2.Subtract \n3.Multiply \n4.Divide\n"))
        if user in [1, 2, 3, 4]:  
            break  
        else:
            print("Please enter a number between 1 and 4.")
    except ValueError: 
        print("Please enter a valid number.")

if user == 1:
    while True:
        try:
            print()
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = add(a,b)
            print("Sum: " + str(result))
            break
        except:
            print("Please enter a valid number")

if user == 2:
    while True:
        try:
            print()
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = subtract(a,b)
            print("Diffrence: " + str(result))
            break
        except:
            print("Please enter a valid number")

if user == 3:
    while True:
        try:
            print()
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = multiply(a,b)
            print("Product: " + str(result))
            break
        except:
            print("Please enter a valid number")

if user == 4:
    while True:
        try:
            print()
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = divide(a,b)
            print("Quotient: " + str(result))
            break
        except:
            print("Please enter a valid number")

print()
print("**************************************************")