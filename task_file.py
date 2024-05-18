from datetime import datetime
from enums import PriorityLevel, TaskStatus


class Task:
    """
    Intialise a task with title, description, due date, priority, and status.
    """
    def __init__(self, title, description, due_date, priority: PriorityLevel):
        """
        Initializes a Task object with the given attributes.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            due_date (datetime): The due date of the task.
            priority (PriorityLevel): The priority level of the task.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = TaskStatus.PENDING

    def to_string(self):
        """
        Converts the task to a string representation.

        Returns:
            str: The string representation of the task.
        """
        return (f"{self.title};{self.description};"
                f"{self.due_date.strftime('%d-%m-%Y')};{self.priority.name};"
                f"{self.status.name}")

    @classmethod
    def from_string(cls, task_str):
        """
        Creates a Task object from a string representation.

        Args:
            task_str (str): The string representation of the task.

        Returns:
            Task: The Task object created from the string.
        """
        task_data = task_str.split(";")
        due_date = datetime.strptime(task_data[2], "%d-%m-%Y")
        priority = PriorityLevel[task_data[3]]
        status = TaskStatus[task_data[4]]
        task = cls(task_data[0], task_data[1], due_date, priority)
        task.status = status
        return task


