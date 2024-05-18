
from typing import List
from task_file import Task
from datetime import datetime
from file_storage import filestorage
from enums import PriorityLevel, TaskStatus


class TaskManager:
    """
    A class to manage tasks and interact with task storage.

    Attributes:
        file_path (str): The path to the file where tasks are stored.
        tasks (List[Task]): A list of Task objects representing the tasks.
    """
    def __init__(self, file_path):
        """
        Initialize TaskManager with the file path.

        Args:
            file_path (str): The path to the file where tasks are stored.
        """
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """
        Load tasks from the file and return a list of Task objects.

        Returns:
            List[Task]: A list of Task objects representing the tasks.
        """
        try:
            with open(self.file_path, "r") as file:
                tasks = []
                tasks_data = []
                tasks_data = file.readlines()
                for task_data in tasks_data:
                    task = Task.from_string(task_data.strip())
                    tasks.append(task)
                return tasks
        except FileNotFoundError:
            return []
    
    def create_task(self, title: str, description: str, due_date: datetime,
                    priority: PriorityLevel) -> Task:
        """
        Create a new task and add it to the list of tasks.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            due_date (datetime): The due date of the task.
            priority (PriorityLevel): The priority level of the task.

        Returns:
            Task: The created Task object.
        """
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        filestorage.save_tasks(self.file_path, self.tasks)
        return task
    
    def edit_task(self, task_to_edit: Task, title: str, description: str,
                  due_date: datetime, priority: PriorityLevel):
        """
        Edit an existing task based on its title.

        Args:
            task_to_edit (Task): The task to be edited.
            title (str): The new title of the task.
            description (str): The new description of the task.
            due_date (datetime): The new due date of the task.
            priority (PriorityLevel): The new priority level of the task.
        """
        self.tasks = self.load_tasks()
        print("Task to edit title:", task_to_edit.title)
        for task1 in self.tasks:
            print("Task title in loop:", task1.title)
            if task_to_edit.title == task1.title:
                task1.title = title
                task1.description = description
                task1.due_date = due_date
                task1.priority = priority
                break   # Break out of the loop once the task
                # is found and edited.
        filestorage.save_tasks(self.file_path, self.tasks)

    def delete_task(self, task: Task):
        """
        Delete a task from the list of tasks.

        Args:
            task (Task): The task to be deleted.
        """
        self.tasks.remove(task)
        filestorage.save_tasks(self.file_path, self.tasks)

    def mark_task_as_complete(self, task: Task):
        """
        Mark a task as complete.

        Args:
            task (Task): The task to be marked as complete.
        """
        task.status = TaskStatus.COMPLETED
        filestorage.save_tasks(self.file_path, self.tasks)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks stored in the file.

        Returns:
            List[Task]: A list of all Task objects stored in the file.
        """
        self.tasks = self.load_tasks()
        return self.tasks
