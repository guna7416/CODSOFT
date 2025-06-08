import json

TODO_FILE = "todo_list.json"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "❌"
        print(f"{index}. {task['task']} - {status}")

def update_task(index, new_task):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")

def mark_task_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Task marked as completed: {tasks[index]['task']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task description: ")
            update_task(index, new_task)
        elif choice == "4":
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            view_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(index)
        elif choice == "6":
            print("Exiting To-Do List Application. Bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
