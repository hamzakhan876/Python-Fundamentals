again = "yes"

while again == "yes":

    # Ask for student information
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    marks = int(input("Enter Student Marks: "))

    # Check result
    if marks >= 50:
        result = "Pass"
    else:
        result = "Fail"
    
    
    # Display information
    print("\n----- Student Report -----")
    print("Name :", name)
    print("Age :", age)
    print("Marks :", marks)
    print("Result :", result)

    # Ask to continue
    again = input("\nDo you want to check another student? (yes/no): ")

print("\nProgram Ended.")