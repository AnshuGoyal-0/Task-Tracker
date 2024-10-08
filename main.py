import os
import json

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            try:
                with open('tasks.json', 'r') as f:
                    tasks_data = json.load(f)
                    # Ensure data is a list of dictionaries
                    if isinstance(tasks_data, list):
                        self.tasks = [Task(**task) for task in tasks_data if isinstance(task, dict)]
                    else:
                        print("JSON data is not in the expected format. Initializing with an empty task list.")
                        self.tasks = []
            except json.JSONDecodeError:
                print("Error decoding JSON. Initializing with an empty task list.")
                self.tasks = []
        else:
            print("No task file found. Initializing with an empty task list.")
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def add_task(self, title, description, status):
        task = Task(title, description, status)
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, task_id, title=None, description=None, status=None):
        if 0 <= task_id < len(self.tasks):
            if title:
                self.tasks[task_id].title = title
            if description:
                self.tasks[task_id].description = description
            if status in ['not done', 'in progress', 'done']:
                self.tasks[task_id].status = status
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status == status]
        for i, task in enumerate(filtered):
            print(f"{i}: Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        for i, task in enumerate(results):
            print(f"{i}: Title: {task.title}, Description: {task.description}, Status: {task.status}")

# Command-line interface
if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List All Tasks")
        print("5. Filter Tasks")
        print("6. Search Tasks")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status = input("Enter task status (not done/in progress/done): ")
            if status not in ['not done', 'in progress', 'done']:
                print("Invalid status. Use 'not done', 'in progress', or 'done'.")
                continue
            task_manager.add_task(title, description, status)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new task title (leave blank for no change): ")
            description = input("Enter new task description (leave blank for no change): ")
            status = input("Enter new task status (not done/in progress/done, leave blank for no change): ")
            if status not in ['not done', 'in progress', 'done', '']:
                print("Invalid status. Use 'not done', 'in progress', or 'done'.")
                continue
            task_manager.update_task(task_id, title if title else None, description if description else None, status if status else None)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            status = input("Enter status to filter (not done/in progress/done): ")
            if status in ['not done', 'in progress', 'done']:
                task_manager.filter_tasks(status)
            else:
                print("Invalid status.")
        elif choice == '6':
            keyword = input("Enter keyword to search for: ")
            task_manager.search_tasks(keyword)
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.")
