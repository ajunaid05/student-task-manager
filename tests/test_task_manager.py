import os
import tempfile
import unittest
from unittest import mock

import task_manager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)
        patcher = mock.patch.object(task_manager, "TASKS_FILE", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(lambda: os.path.exists(self.path) and os.remove(self.path))

    def test_add_task(self):
        self.assertTrue(task_manager.add_task("Write report"))
        tasks = task_manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Write report")
        self.assertFalse(tasks[0]["completed"])

    def test_add_empty_title_rejected(self):
        self.assertFalse(task_manager.add_task("   "))
        self.assertEqual(task_manager.load_tasks(), [])

    def test_complete_task(self):
        task_manager.add_task("Study DevOps")
        self.assertTrue(task_manager.complete_task(1))
        self.assertTrue(task_manager.load_tasks()[0]["completed"])

    def test_complete_already_completed_returns_false(self):
        task_manager.add_task("Study DevOps")
        task_manager.complete_task(1)
        self.assertFalse(task_manager.complete_task(1))

    def test_complete_invalid_id(self):
        self.assertFalse(task_manager.complete_task(99))

    def test_delete_task(self):
        task_manager.add_task("Task A")
        task_manager.add_task("Task B")
        self.assertTrue(task_manager.delete_task(1))
        remaining = task_manager.load_tasks()
        self.assertEqual([t["id"] for t in remaining], [2])

    def test_delete_invalid_id(self):
        task_manager.add_task("Task A")
        self.assertFalse(task_manager.delete_task(42))
        self.assertEqual(len(task_manager.load_tasks()), 1)


if __name__ == "__main__":
    unittest.main()
