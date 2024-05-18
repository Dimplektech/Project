import unittest
from datetime import datetime
from task_manager import TaskManager, PriorityLevel, TaskStatus


class TestTaskManager(unittest.TestCase):
    """
    A class method to test the TaskManager class methods.
    
    Methods:

    setUp():
        Initialise a TaskManager for each test method
    test_add_task():
        Test the add_task method of TaskManager.
    test_edit_task():
        Test the edit_task method of TaskManager.
    test_delete_task():
        Test the delete_task method of TaskManager.
    test_mark_task_as_complete():
        Test the mark_task_as_complete method of TaskManager.
    """

    def setUp(self):
        file_path = "tasks.txt"  # File path where tasks are stored.
        """Initialise a TaskManager instatnce for each test method."""
        self.task_manager = TaskManager(file_path)
      
    def test_add_task(self):
        """ Test the add_task method of TaskManager."""
        # Create a Task.
        tasks = self.task_manager.get_all_tasks()
        # get total number of records before adding task.
        tot_tsks_before_add = len(tasks)
        self.task_manager.create_task("Test Task", "This task is test task",
                                      datetime.now(), PriorityLevel.HIGH)
        tasks = self.task_manager.get_all_tasks()
        # Check if the task was added successfully.
        self.assertEqual(len(tasks), tot_tsks_before_add + 1)

    def test_edit_task(self):
        task = self.task_manager.get_all_tasks()[0]
        # Call edit function.
        self.task_manager.edit_task(task, "Edited Task", "This is an "
                                    "edited task.", datetime.now(),
                                    PriorityLevel.LOW)
        edited_task = self.task_manager.get_all_tasks()[0]
        # Check if the task was edited Successfully.
        self.assertEqual(edited_task.title, "Edited Task")
        self.assertEqual(edited_task.description, "This is an edited task.")
        self.assertEqual(edited_task.priority, PriorityLevel.LOW)

    def test_delete_task(self):
        """Test the delete_task method of TaskManager."""
        # Get the number of tasks from file before delete one.
        tasks = self.task_manager.get_all_tasks()
        if tasks:  # Check if tasks list is not empty
            tot_tsks_before_del = len(tasks)
            # Get first task of the file and delete it.
            task = tasks[0]
            self.task_manager.delete_task(task)
            tasks = self.task_manager.get_all_tasks()
            self.assertEqual(len(tasks), tot_tsks_before_del - 1)
        else:
            # Skip the test if no tasks exist.
            self.skipTest("No tasks available to delete.")

    def test_mark_task_as_complete(self):
        """Test the mark_task_as_complete method of TaskManager."""
        # Get The first Task in the file and mark as completed.
        task = self.task_manager.get_all_tasks()[0]
        # Mark the task as complete
        self.task_manager.mark_task_as_complete(task)
        # Check if the task was marked as complete successfully
        task = self.task_manager.get_all_tasks()[0]
        self.assertEqual(task.status, TaskStatus.COMPLETED)


if __name__ == "__main__":
    unittest.main()
