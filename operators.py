#defining function of operators
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y
def floor(x,y):
    return x // y

#menu-driven driver code
while True:
    ch = input(":::::::::Calculator:::::::::\n1. Add\t\t2. Subtract\n3. Multiply\t4. Divide\n5. Power\t6. Floor\n7. Exit\n\nEnter choice: ")
    if ch in ('1','2','3','4','5','6'):
        num1 = float(input("Enter first number: "))
        if ch in ('1','2','3','4','5','6'):
            num2 = float(input("Enter second number: "))
        else:
            pass
        if ch == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif ch == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif ch == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif ch == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif ch == '5':
            print(num1, "**", num2, "=", power(num1, num2))
        elif ch == '6':
            print(num1, "//", num2, "=", floor(num1, num2))
        elif ch == '7':
            exit()
        else:
            pass
        rerun = input("Continue? (yes/no): ") #rerun the program
        if rerun.lower() == "n":
            break
    else:
        print("Invalid Input")
        pass
