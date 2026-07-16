def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

def exit():
    print ("Thanks for using the calculator.Come agin soon")

def show_menu(title):
    print(title)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

show_menu("-----calculator-----")
choice = input("choose an option: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = add(num1, num2)
elif choice == "2":
    result = subtract(num1, num2)
elif choice == "3":
    result = multiply(num1, num2)
elif choice == "4":
    result = divide(num1, num2)
else:
    result = "Invalid option"

    exit()
print(result)

while True:
    show_menu("-----calculator-----")
    choice = input("choose an option: ")
    if choice == "5":
        exit()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        result = "Invalid option"

    print(result)