tasks = {}  # Initialize an empty dictionary to store position, task, and status
position = 0  # Start with position 0

# Add a task with an automatic position and default status "not done"
def add(task_name):
    global position
    tasks[position] = {'task': task_name, 'status': 'not done'}
    position += 1
    print(f"Added task: {task_name}")

# Update a task description at a specific position
def update(pos, new_task_name):
    if pos in tasks:
        tasks[pos]['task'] = new_task_name
        print(f"Updated task at position {pos}: {new_task_name}")
    else:
        print(f"No task found at position {pos}")

# Delete a task at a specific position
def delete(pos):
    if pos in tasks:
        removed_task = tasks.pop(pos)
        print(f"Deleted task: {removed_task['task']} from position {pos}")
    else:
        print(f"No task found at position {pos}")

# Mark a task as "in progress" or "done"
def mark_status(pos, status):
    if pos in tasks:
        if status in ['not done', 'in progress', 'done']:
            tasks[pos]['status'] = status
            print(f"Task at position {pos} marked as '{status}'")
        else:
            print(f"Invalid status. Use 'not done', 'in progress', or 'done'.")
    else:
        print(f"No task found at position {pos}")

# List all tasks
def list_all_tasks():
    print("All Tasks:")
    for pos, details in tasks.items():
        print(f"Position {pos}: {details['task']} (Status: {details['status']})")

# List tasks based on a specific status
def list_tasks_by_status(status):
    print(f"Tasks with status '{status}':")
    for pos, details in tasks.items():
        if details['status'] == status:
            print(f"Position {pos}: {details['task']}")

# Example usage:
add("hello")
add("world")
mark_status(0, "in progress")
mark_status(1, "done")

list_all_tasks()  # List all tasks
list_tasks_by_status('done')  # List tasks that are done
list_tasks_by_status('not done')  # List tasks that are not done
list_tasks_by_status('in progress')  # List tasks that are in progress
