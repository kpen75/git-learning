# todo.py

"""
Simple To-Do List Manager
This script lets you add, view, and complete tasks.
Perfect for practicing Git version control and collaboration.
"""

# Store tasks in a list
tasks = []


def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()


def add_task(task):
    """Add a new task."""
    tasks.append(task)
    print(f"➕ Added: {task}")


def complete_task(index):
    """Mark a task as completed."""
    try:
        completed = tasks.pop(index - 1)
        print(f"✔ Completed: {completed}")
    except IndexError:
        print("❌ Invalid task number.")


def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Complete a task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                task_num = int(input("Enter task number to complete: "))
                complete_task(task_num)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
