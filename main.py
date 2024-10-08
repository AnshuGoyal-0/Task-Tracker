import argparse
import json
import os

# The name of the JSON file to store tasks
TASK_FILE = 'tasks.json'

# Function to load tasks from the JSON file, or initialize if the file doesn't exist
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task to the tasks dictionary
def add_task(task_name):
    tasks = load_tasks()
    position = len(tasks)  # Automatically assign position based on number of tasks
    tasks[position] = {'task': task_name, 'status': 'not done'}
    save_tasks(tasks)
    print(f"Task added: {task_name} at position {position}")

# Update an existing task at a specific position
def update_task(pos, new_task_name):
    tasks = load_tasks()
    if str(pos) in tasks:
        tasks[str(pos)]['task'] = new_task_name
        save_tasks(tasks)
        print(f"Task at position {pos} updated to: {new_task_name}")
    else:
        print(f"No task found at position {pos}")

# Delete a task by position
def delete_task(pos):
    tasks = load_tasks()
    if str(pos) in tasks:
        removed_task = tasks.pop(str(pos))
        save_tasks(tasks)
        print(f"Task deleted: {removed_task['task']} from position {pos}")
    else:
        print(f"No task found at position {pos}")

# Mark a task as 'in progress', 'done', or 'not done'
def mark_task_status(pos, status):
    if status not in ['not done', 'in progress', 'done']:
        print("Invalid status. Use 'not done', 'in progress', or 'done'.")
        return
    tasks = load_tasks()
    if str(pos) in tasks:
        tasks[str(pos)]['status'] = status
        save_tasks(tasks)
        print(f"Task at position {pos} marked as '{status}'")
    else:
        print(f"No task found at position {pos}")

# List all tasks
def list_all_tasks():
    tasks = load_tasks()
    if tasks:
        print("All Tasks:")
        for pos, details in tasks.items():
            print(f"Position {pos}: {details['task']} (Status: {details['status']})")
    else:
        print("No tasks found.")

# List tasks by a specific status
def list_tasks_by_status(status):
    tasks = load_tasks()
    if tasks:
        print(f"Tasks with status '{status}':")
        for pos, details in tasks.items():
            if details['status'] == status:
                print(f"Position {pos}: {details['task']}")
    else:
        print("No tasks found.")

# Main function to parse command-line arguments and call the appropriate functions
def main():
    parser = argparse.ArgumentParser(description="Task Manager")
    parser.add_argument("command", choices=['add', 'update', 'delete', 'mark', 'list', 'list_done', 'list_not_done', 'list_in_progress'], help="Command to execute")
    parser.add_argument("--task", help="Task description")
    parser.add_argument("--pos", type=int, help="Position of the task")
    parser.add_argument("--status", choices=['not done', 'in progress', 'done'], help="Task status")

    args = parser.parse_args()

    if args.command == 'add':
        if args.task:
            add_task(args.task)
        else:
            print("Please provide a task name using --task")

    elif args.command == 'update':
        if args.pos is not None and args.task:
            update_task(args.pos, args.task)
        else:
            print("Please provide both position (--pos) and task name (--task)")

    elif args.command == 'delete':
        if args.pos is not None:
            delete_task(args.pos)
        else:
            print("Please provide the position of the task to delete using --pos")

    elif args.command == 'mark':
        if args.pos is not None and args.status:
            mark_task_status(args.pos, args.status)
        else:
            print("Please provide both position (--pos) and status (--status)")

    elif args.command == 'list':
        list_all_tasks()

    elif args.command == 'list_done':
        list_tasks_by_status('done')

    elif args.command == 'list_not_done':
        list_tasks_by_status('not done')

    elif args.command == 'list_in_progress':
        list_tasks_by_status('in progress')

if __name__ == "__main__":
    main()
