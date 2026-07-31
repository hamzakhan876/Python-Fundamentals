# ==============================
# Task Class
# ==============================

class Task:

    def __init__(self, title):
        self.title = title
        self.completed = False

    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"Title  : {self.title}")
        print(f"Status : {status}")
        print("-" * 30)

    def mark_completed(self):
        if self.completed:
            print(f'"{self.title}" is already completed.')
        else:
            self.completed = True
            print(f'"{self.title}" marked as completed.')


# ==============================
# TodoList Class
# ==============================

class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print("Task added successfully.")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("\nNo tasks available.\n")
            return

        print("\n====== TO-DO LIST ======\n")

        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}")
            task.display()

    def remove_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid Task Number.")
            return

        removed_task = self.tasks.pop(task_number - 1)
        print(f'"{removed_task.title}" removed successfully.')

    def complete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid Task Number.")
            return

        self.tasks[task_number - 1].mark_completed()


# ==============================
# Main Program
# ==============================

todo = TodoList()

while True:

    print("\n=========================")
    print("      TO-DO APP")
    print("=========================")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task Complete")
    print("4. Show All Tasks")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        title = input("Enter Task Title: ")
        todo.add_task(title)

    elif choice == "2":

        todo.show_tasks()

        number = int(input("Enter Task Number to Remove: "))
        todo.remove_task(number)

    elif choice == "3":

        todo.show_tasks()

        number = int(input("Enter Task Number to Complete: "))
        todo.complete_task(number)

    elif choice == "4":

        todo.show_tasks()

    elif choice == "5":

        print("Thank you for using To-Do App.")
        break

    else:
        print("Invalid Choice.")