from tasks import Task


def save_tasks(todo_list, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in todo_list.tasks:
            file.write(f"{task.title}|{task.completed}\n")


def load_tasks(todo_list, filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                title, completed = line.strip().split("|")
                task = Task(title)
                task.completed = completed == "True"
                todo_list.tasks.append(task)
    except FileNotFoundError:
        pass