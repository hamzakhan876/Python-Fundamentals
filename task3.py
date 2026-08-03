class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass
salary = int(input("Enter your salary: "))
if salary <0:
    raise NegativeNumberError("Salary cannot be negative.")
else:
    print("salary:", salary)