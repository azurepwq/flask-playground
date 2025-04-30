tasks = []
MAX_TASK_LENGTH = 255

def add_task(task):
    """
    Adds a task to the list. Raises ValueError if the task is empty or only whitespace.
    Returns a string message for other validation or success.
    """
    if not isinstance(task, str) or not task.strip():
        raise ValueError("Task cannot be empty.")
    if len(task) > MAX_TASK_LENGTH:
        return "Invalid task: too long."
    if task in tasks:
        return "Task already exists."
    tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed."
    else:
        return "Task not found."

def list_tasks():
    return list(tasks)  # Return a copy to prevent external modification

# Example usage
# print(add_task("Buy groceries"))
# print(add_task("Read a book"))
# print(list_tasks())
# print(remove_task("Read a book"))
# print(list_tasks())