""" Basic task management system with functionalities to create, edit, delete,
 mark as complete, and retrieve tasks. It interacts with a file storage system
 (filestorage) to save and load tasks from a file."""

# Importing TaskManager class from task_manager module.
from task_manager import TaskManager
# Importing datetime class from datetime module.
from datetime import datetime
# Importing PriorityLevel class from enums module.
from enums import PriorityLevel


def main():
    """
    Main Function to run the Task Management Apllicaton.
    """
    file_path = "tasks.txt"  # File path where tasks are stored.
    task_manager = TaskManager(file_path)  # Creating instance of TaskManager.

    while True:
        # Displaying Menu Option.
        print("\nTask Management Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark as Completed")
        print("6. Quit")

        choice = input("Enter Your Choice: ")  # Taking User input for choice.

        if choice == "1":
            # View tasks
            print("\nViewing tasks...")
            all_tasks = []
            all_tasks = task_manager.get_all_tasks()
            for task in all_tasks:
                # Printing details of each task.
                print(f"Title: {task.title}, Description: {task.description},"
                      f" Priority: {task.priority.name},"
                      f" Status: {task.status.name}")
        elif choice == "2":
            # Add a new task
            print("\nAdding a new task...")
            try:
                title = input("Enter title: ")
                description = input("Enter description: ")
                due_date_str = input("Enter due date (DD-MM-YYYY): ")
                # Handling date input errors.
                try:
                    due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
                except ValueError:
                    raise ValueError("Invalid date format. Please enter the"
                                     " date in the format DD-MM-YYYY.")
                               
                priority_str = input("Enter priority (HIGH, MEDIUM, LOW): ")
                # Handling priority input errors.
                try:
                    priority = PriorityLevel[priority_str.upper()]
                except KeyError:
                    raise ValueError("Invalid priority level entered."
                                     "Please enter HIGH, MEDIUM, or LOW.")
              
                #  Calling create task function.
                task_manager.create_task(title, description,
                                         due_date, priority)
                print("Task added successfully!")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif choice == "3":
            # Edit a task
            print("\nEditing a task...")
            task_title = input("\nEnter the title of the task to edit: ")
            tasks = task_manager.get_all_tasks()
            # Getting matching tasks if exist.
            matching_tasks = [task for task in tasks
                              if task.title == task_title]
            if matching_tasks:  # If matching Task exist, then edit it.
                task_to_edit = matching_tasks[0]
                print(f"Editing Task Title : {task_to_edit.title}")
                title = input("Enter new title: ")
                description = input("Enter new description: ")
                due_date_str = input("Enter new due date (DD-MM-YYYY): ")
                due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
                priority_str = input("Enter new priority (HIGH, "
                                     "MEDIUM, LOW): ")
                priority = PriorityLevel[priority_str.upper()]
                task_manager.edit_task(task_to_edit, title,
                                       description, due_date, priority)
                print("Task edited successfully!")
            else:
                print("Task not found.")
        elif choice == "4":
            # Delete a task
            print("\nDeleting a task...")
            task_title = input("Enter the title of the task to delete: ")
            tasks = task_manager.get_all_tasks()
            matching_tasks = [task for task in tasks
                              if task.title == task_title]
            if matching_tasks:
                task_to_delete = matching_tasks[0]
                task_manager.delete_task(task_to_delete)
                print("Task deleted successfully!")
            else:
                print("Task not found.")
        elif choice == "5":
            # Mark Task as complted.
            print("\nMarking task as completed...")
            task_title = input("Enter the title of the task "
                               "to mark as completed: ")
            tasks = task_manager.get_all_tasks()
            # Iterate task which you need to mark as completed.
            matching_tasks = [task for task in tasks
                              if task.title == task_title]
            if matching_tasks:  # call mark_task_as_completed function.
                task_manager.mark_task_as_complete(matching_tasks[0])
                print("Task Marked as Completed!")
            else:
                print("Task not found.")
        elif choice == "6":
            # Exit the apllication.
            print("\nExiting the application...")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
