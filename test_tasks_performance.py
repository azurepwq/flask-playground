import tasks2
import time

def setup_function():
    tasks2.tasks.clear()

def test_add_many_tasks_performance():
    setup_function()
    num_tasks = 10000
    start = time.time()
    for i in range(num_tasks):
        tasks2.add_task(f"Task {i}")
    end = time.time()
    duration = end - start
    print(f"Adding {num_tasks} tasks took {duration:.4f} seconds")
    assert duration < 2  # Example threshold: should finish in under 2 seconds

def test_list_many_tasks_performance():
    setup_function()
    num_tasks = 10000
    for i in range(num_tasks):
        tasks2.add_task(f"Task {i}")
    start = time.time()
    _ = tasks2.list_tasks()
    end = time.time()
    duration = end - start
    print(f"Listing {num_tasks} tasks took {duration:.6f} seconds")
    assert duration < 0.1  # Should be very fast 