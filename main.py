from tasks  import TodoList
from storage import save_tasks, load_tasks


todo = TodoList()
load_tasks(todo)

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Complete")
    print("4. Show Tasks")
    print("5. Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Task title: ")
        todo.add_task(title)

    elif choice == "2":
        todo.show_tasks()
        number = int(input("Task number: ")) - 1
        todo.remove_task(number)

    elif choice == "3":
        todo.show_tasks()
        number = int(input("Task number: ")) - 1
        todo.complete_task(number)

    elif choice == "4":
        todo.show_tasks()

    elif choice == "5":
        save_tasks(todo)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid option.")