try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("The result of the division is:", result)