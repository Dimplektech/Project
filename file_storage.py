from typing import List
from task_file import Task


class filestorage:
    """
    A static class to handle saving tasks to a file.
    """
    @staticmethod
    def save_tasks(file_path: str, tasks: List[Task]):
        """
        Save tasks to a file.

        Args:
            file_path (str): The path to the file where tasks will be saved.
            tasks (List[Task]): The list of tasks to be saved.
        """
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(Task.to_string(task) + "\n")

   