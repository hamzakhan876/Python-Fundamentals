
students = []
    
def add_student():
    name = input("Enter Student Name:")
    grade = float(input("Enter Student Grade:"))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade between 0 and 100.")
        return
    students.append({"name": name, "grade": grade})
    print( students)
    
def view_students():
    if not students:
        print("No students found.")
    else:
        for s in students:
            print(f"Name: {s['name']}, Grade: {s['grade']}")

def class_average():
    print( students)
    if not students:
        print("No students found.")
    else:
        total = sum(s['grade'] for s in students)
        average = total / len(students)
        print(f"Class Average: {average}")

def top_student():
    if not students:
        print("No students found.")
        return None
    return max(students, key=lambda s: s['grade'])

def show_menu():
    print("------Student Grade Tracker Menu------")
    print("1. Add student ")
    print("2. View students")
    print("3. Calculate class average")
    print("4. Find top student")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-5):")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        class_average()
    elif choice == "4":
        top = top_student()
        if top:
            print(f"Top student: {top['name']}, Grade: {top['grade']}")
        else:
            print("No students found.")
    elif choice == "5":
        print("Exiting the Program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
