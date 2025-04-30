import threading

tasks = []
tasks_lock = threading.Lock()
MAX_TASK_LENGTH = 255

def add_task(task):
    if not isinstance(task, str) or not task.strip():
        return "Invalid task: cannot be empty."
    if len(task) > MAX_TASK_LENGTH:
        return "Invalid task: too long."
    with tasks_lock:
        if task in tasks:
            return "Task already exists."
        tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    with tasks_lock:
        if task in tasks:
            tasks.remove(task)
            return f"Task '{task}' removed."
        else:
            return "Task not found."

def list_tasks():
    with tasks_lock:
        return list(tasks)  # Return a copy to avoid race conditions

# Example usage
print(add_task("Buy groceries"))
print(add_task("Read a book"))
print(add_task("Buy groceries"))
print(list_tasks())
print(remove_task("Read a book"))
print(list_tasks())
print(add_task(""))
print(list_tasks())
long_task = "A" * 1000
print(add_task(long_task))
print(list_tasks())