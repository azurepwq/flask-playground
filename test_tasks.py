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