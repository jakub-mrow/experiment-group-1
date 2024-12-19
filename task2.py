class Task:
    def __init__(self, title, description, priority, is_completed):
        self.title = title
        self.description = description
        self.priority = priority
        self.is_completed = is_completed

    def __repr__(self):
        return f"{self.title} - {self.description} - {self.priority} - {self.is_completed}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def view_sorted_tasks(self):
        return sorted(self.tasks, key=lambda x: x.priority, reverse=True)

    def mark_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.is_completed = True
                return True
        return False


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.add_task(Task("Task 1", "Description 1", 1, False))
    todo_list.add_task(Task("Task 2", "Description 2", 2, False))
    todo_list.add_task(Task("Task 3", "Description 3", 3, False))
    todo_list.add_task(Task("Task 4", "Description 4", 4, False))
    todo_list.add_task(Task("Task 5", "Description 5", 5, False))

    todo_list.add_task(Task("new task for testing", "New description", 100, False))

    print(todo_list.view_sorted_tasks())
    todo_list.mark_as_completed("Task 3")
    print(todo_list.view_sorted_tasks())
    todo_list.remove_task("Task 2")
    print(todo_list.view_sorted_tasks())





