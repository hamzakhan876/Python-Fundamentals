
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")