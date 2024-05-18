from enum import Enum


# Enumeration class for Priority Level
class PriorityLevel(Enum):
    HIGH = 1   # High priority level
    MEDIUM = 2   # Medium priority level
    LOW = 3   # Low priority level


# Enumeration class for Task Status
class TaskStatus(Enum):
    PENDING = 1  # Task is pending
    IN_PROGRESS = 2  # Task is in_progress
    COMPLETED = 3  # Task is completed