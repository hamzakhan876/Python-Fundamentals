class Calculator:

    def __init__(self):
        self.history = []
        self.load_history()

    # ----------------------------
    # Load history from file
    # ----------------------------
    def load_history(self):
        try:
            with open("history.txt", "r") as file:
                self.history = file.readlines()

            # Remove "\n" from every line
            self.history = [line.strip() for line in self.history]

        except FileNotFoundError:
            # Create file if it doesn't exist
            with open("history.txt", "w") as file:
                pass

    # ----------------------------
    # Save one calculation
    # ----------------------------
    def save_history(self, calculation):

        self.history.append(calculation)

        with open("history.txt", "a") as file:
            file.write(calculation + "\n")

    # ----------------------------
    # Add
    # ----------------------------
    def add(self, num1, num2):

        result = num1 + num2

        calculation = f"{num1} + {num2} = {result}"

        self.save_history(calculation)

        return result

    # ----------------------------
    # Subtract
    # ----------------------------
    def subtract(self, num1, num2):

        result = num1 - num2

        calculation = f"{num1} - {num2} = {result}"

        self.save_history(calculation)

        return result

    # ----------------------------
    # Multiply
    # ----------------------------
    def multiply(self, num1, num2):

        result = num1 * num2

        calculation = f"{num1} * {num2} = {result}"

        self.save_history(calculation)

        return result

    # ----------------------------
    # Divide
    # ----------------------------
    def divide(self, num1, num2):

        if num2 == 0:
            return "Cannot divide by zero."

        result = num1 / num2

        calculation = f"{num1} / {num2} = {result}"

        self.save_history(calculation)

        return result

    # ----------------------------
    # Show History
    # ----------------------------
    def show_history(self):

        if len(self.history) == 0:
            print("\nNo History Found.\n")

        else:
            print("\n===== Calculator History =====\n")

            for item in self.history:
                print(item)

            print()


# ====================================
# Main Program
# ====================================

calculator = Calculator()

while True:

    print("========== Calculator ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "6":
        print("\nThank you for using Calculator!")
        break

    if choice == "5":
        calculator.show_history()
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid Choice\n")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result =", calculator.add(num1, num2))

    elif choice == "2":
        print("Result =", calculator.subtract(num1, num2))

    elif choice == "3":
        print("Result =", calculator.multiply(num1, num2))

    elif choice == "4":
        print("Result =", calculator.divide(num1, num2))

    print()