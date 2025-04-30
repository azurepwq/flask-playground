import unittest
import tasks2

class TestTasks(unittest.TestCase):
    def setUp(self):
        tasks2.tasks.clear()

    def test_add_normal_task(self):
        result = tasks2.add_task("Do homework")
        self.assertEqual(result, "Task 'Do homework' added.")
        self.assertIn("Do homework", tasks2.list_tasks())

    def test_add_duplicate_task(self):
        tasks2.add_task("Do homework")
        result = tasks2.add_task("Do homework")
        self.assertEqual(result, "Task already exists.")
        self.assertEqual(tasks2.list_tasks().count("Do homework"), 1)

    def test_remove_existing_task(self):
        tasks2.add_task("Do homework")
        result = tasks2.remove_task("Do homework")
        self.assertEqual(result, "Task 'Do homework' removed.")
        self.assertNotIn("Do homework", tasks2.list_tasks())

    def test_remove_nonexistent_task(self):
        result = tasks2.remove_task("Go jogging")
        self.assertEqual(result, "Task not found.")

    def test_add_empty_task(self):
        with self.assertRaisesRegex(ValueError, "Task cannot be empty."):
            tasks2.add_task("")
        self.assertNotIn("", tasks2.list_tasks())

    def test_add_very_long_task(self):
        long_task = "A" * 1000
        result = tasks2.add_task(long_task)
        self.assertEqual(result, "Invalid task: too long.")
        self.assertNotIn(long_task, tasks2.list_tasks())

if __name__ == '__main__':
    unittest.main() 