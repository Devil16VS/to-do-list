import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    description = input("Enter task description: ")
    task_id = len(tasks) + 1
    task = {'id': task_id, 'description': description, 'status': 'pending'}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "[ ]" if task['status'] == 'pending' else "[X]"
        print(f"{task['id']}. {status} {task['description']}")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to update: "))
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            print("Task not found.")
            return
        print("1. Mark as done")
        print("2. Edit description")
        choice = input("Choose option: ")
        if choice == '1':
            task['status'] = 'done'
        elif choice == '2':
            new_desc = input("Enter new description: ")
            task['description'] = new_desc
        else:
            print("Invalid choice.")
            return
        save_tasks(tasks)
        print("Task updated successfully!")
    except ValueError:
        print("Invalid ID.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            print("Task not found.")
            return
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except ValueError:
        print("Invalid ID.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
