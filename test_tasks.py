# test_tasks.py

import tasks2
import pytest


def setup_function():
    # This function runs before each test
    tasks2.tasks.clear()

def test_add_normal_task():
    result = tasks2.add_task("Do homework")
    assert result == "Task 'Do homework' added."
    assert "Do homework" in tasks2.list_tasks()

def test_add_duplicate_task():
    tasks2.add_task("Do homework")
    result = tasks2.add_task("Do homework")
    assert result == "Task already exists."
    assert tasks2.list_tasks().count("Do homework") == 1

def test_remove_existing_task():
    tasks2.add_task("Do homework")
    result = tasks2.remove_task("Do homework")
    assert result == "Task 'Do homework' removed."
    assert "Do homework" not in tasks2.list_tasks()

def test_remove_nonexistent_task():
    result = tasks2.remove_task("Go jogging")
    assert result == "Task not found."

def test_add_empty_task():
    with pytest.raises(ValueError, match="Task cannot be empty."):
        tasks2.add_task("")
    assert "" not in tasks2.list_tasks()

def test_add_very_long_task():
    long_task = "A" * 1000
    result = tasks2.add_task(long_task)
    assert result == "Invalid task: too long."
    assert long_task not in tasks2.list_tasks()

def test_add_task_whitespace_only():
    with pytest.raises(ValueError, match="Task cannot be empty."):
        tasks2.add_task("   ")
    assert "   " not in tasks2.list_tasks()

def test_add_task_non_string():
    with pytest.raises(ValueError, match="Task cannot be empty."):
        tasks2.add_task(None)
    with pytest.raises(ValueError, match="Task cannot be empty."):
        tasks2.add_task(123)
    with pytest.raises(ValueError, match="Task cannot be empty."):
        tasks2.add_task([])
    assert len(tasks2.list_tasks()) == 0

def test_remove_task_from_empty_list():
    result = tasks2.remove_task("Nonexistent")
    assert result == "Task not found."
    assert len(tasks2.list_tasks()) == 0

def test_list_tasks_returns_copy():
    tasks2.add_task("Task 1")
    tasks2.add_task("Task 2")
    listed = tasks2.list_tasks()
    listed.append("Injected")
    # The original list should not be affected by changes to the returned list
    assert "Injected" not in tasks2.tasks

def test_add_multiple_tasks_and_remove():
    tasks = ["Task 1", "Task 2", "Task 3"]
    for t in tasks:
        tasks2.add_task(t)
    assert all(t in tasks2.list_tasks() for t in tasks)
    tasks2.remove_task("Task 2")
    assert "Task 2" not in tasks2.list_tasks()
    assert len(tasks2.list_tasks()) == 2

def test_remove_task_with_whitespace():
    tasks2.add_task("TaskX")
    result = tasks2.remove_task("  TaskX  ")
    # Should not remove, as exact match is required
    assert result == "Task not found."
    assert "TaskX" in tasks2.list_tasks()