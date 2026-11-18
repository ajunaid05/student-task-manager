# task_manager.py
# Student Task Manager - COMSATS University Lahore
# DevOps Assignment 4
# Version: 0.0 - Initial skeleton
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON storage file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Persist tasks to the JSON storage file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def display_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Task List ---")
    for task in tasks:
        status = "Done" if task['completed'] else "Pending"
        print(f"  ID:{task['id']} | {task['title']} | {status}")
    print()


def add_task(title):
    """[STUB] Add a new task - feature not yet implemented."""
    print("[INFO] Add task feature not yet implemented.")
    return False


def complete_task(task_id):
    """[STUB] Mark a task complete - feature not yet implemented."""
    print("[INFO] Complete task feature not yet implemented.")
    return False


def delete_task(task_id):
    """[STUB] Delete a task - feature not yet implemented."""
    print("[INFO] Delete task feature not yet implemented.")
    return False


def main():
    """Main application loop."""
    print("================================")
    print("   Student Task Manager v0.0")
    print("================================")
    while True:
        print("\nOptions:")
        print("  1. Add Task")
        print("  2. View Tasks")
        print("  3. Complete Task")
        print("  4. Delete Task")
        print("  5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            display_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid numeric ID.")
        elif choice == '4':
            display_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid numeric ID.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
