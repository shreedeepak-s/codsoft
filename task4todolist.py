tasks = []

def show_tasks():
    """Display all tasks."""
    if len(tasks) == 0:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{index}. {task['task']} - {status}")

def add_task():
    """Add a new task to the to-do list."""
    task_name = input("\nEnter the task description: ")
    task = {'task': task_name, 'completed': False}
    tasks.append(task)
    print(f"Task '{task_name}' added to the to-do list.")

def update_task():
    """Update an existing task in the to-do list."""
    show_tasks()
    try:
        task_id = int(input("\nEnter the number of the task to update: ")) - 1
        if 0 <= task_id < len(tasks):
            new_task_name = input(f"Enter the new description for the task '{tasks[task_id]['task']}': ")
            tasks[task_id]['task'] = new_task_name
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    """Delete a task from the to-do list."""
    show_tasks()
    try:
        task_id = int(input("\nEnter the number of the task to delete: ")) - 1
        if 0 <= task_id < len(tasks):
            deleted_task = tasks.pop(task_id)
            print(f"Task '{deleted_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_complete():
    """Mark a task as completed."""
    show_tasks()
    try:
        task_id = int(input("\nEnter the number of the task to mark as complete: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks[task_id]['completed'] = True
            print(f"Task '{tasks[task_id]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def menu():
    """Display the menu and handle user choices."""
    while True:
        print("\n To-Do List Menu ")
        print("a. Show Tasks")
        print("b. Add Task")
        print("c. Update Task")
        print("d. Delete Task")
        print("e. Mark Task as Completed")
        print("f. Exit")
        
        choice = input("\nChoose any option: ")

        if choice == "a":
            show_tasks()
        elif choice == "b":
            add_task()
        elif choice == "c":
            update_task()
        elif choice == "d":
            delete_task()
        elif choice == "e":
            mark_task_complete()
        elif choice == "f":
            print(" Your tasks are saved ")
            break
        else:
            print("Invalid choice. Please retry again")
if __name__ == "__main__":
    menu()
