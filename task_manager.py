# task_manager.py
# Student Task Manager - COMSATS University Lahore
# DevOps Assignment 4
# Branch: feature/completetask - Commit 2 (handle invalid ID and already-completed cases)
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
    """Display all tasks with ID, status, and title."""
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found. Add a task to get started!")
        return
    total = len(tasks)
    done = sum(1 for t in tasks if t['completed'])
    print(f"\n--- Task List ({done}/{total} completed) ---")
    for task in tasks:
        status = "✓" if task['completed'] else "○"
        print(f"  [{task['id']}] {status}  {task['title']}")
    print()


def add_task(title):
    """[STUB] Add a new task - to be implemented in feature/addtask."""
    print("[INFO] Add task feature not yet implemented.")
    return False


def complete_task(task_id):
    """Mark a task as completed, with proper validation.
    
    Handles cases where the task ID does not exist,
    or the task is already marked as completed.
    Returns True if status was changed, False otherwise.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print(f"Task [{task_id}] is already completed.")
            else:
                task['completed'] = True
                save_tasks(tasks)
                print(f"Task [{task_id}] marked as completed.")
            return True
    print(f"Error: No task found with ID {task_id}.")
    return False


def delete_task(task_id):
    """[STUB] Delete a task - to be implemented in feature/deletetask."""
    print("[INFO] Delete task feature not yet implemented.")
    return False


def main():
    """Main application loop."""
    print("=" * 35)
    print("   Student Task Manager v0.1")
    print("=" * 35)
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
