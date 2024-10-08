# Task-Tracker

A command-line task management system that allows users to add, update, delete, and manage tasks with ease. Tasks are stored in a JSON file in the current directory, and users can interact with the system via command-line arguments or in an interactive mode if no arguments are passed. The JSON file will be created automatically if it doesn't exist.

## Features

- **Add tasks** with a title, description, and status (`not done`, `in progress`, or `done`).
- **Update tasks** to change their title, description, or status.
- **Delete tasks** from the task list.
- **List all tasks** with their respective status.
- **Filter tasks** by their status (done, not done, or in progress).
- **Search tasks** by keyword in the title or description.
- **Save tasks** persistently in a `tasks.json` file.

## Prerequisites

- Python 3.x must be installed on your machine.

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd Task-Tracker
   ```

## How to Use

You can either run the program with command-line arguments or in interactive mode if no arguments are provided.

### 1. Command-Line Mode

You can interact with the Task-Tracker via command-line arguments for task management.

#### Example usage:

- **Add a new task**:

  ```bash
  python3 main.py add "Task Title" "Task Description" "not done"
  ```
- **Update an existing task**:

  ```bash
  python3 main.py update <task_id> "New Title" "New Description" "done"
  ```
- **Delete a task**:

  ```bash
  python3 main.py delete <task_id>
  ```
- **List all tasks**:

  ```bash
  python3 main.py list
  ```
- **Filter tasks by status**:

  ```bash
  python3 main.py filter "done"
  ```
- **Search tasks by keyword**:

  ```bash
  python3 main.py search "keyword"
  ```

### 2. Interactive Mode

If no command-line arguments are provided, the program will run in interactive mode. Follow the on-screen prompts to manage your tasks.

#### To run in interactive mode:

```bash
python3 main.py
```

### Available Options in Interactive Mode

- **1. Add Task**: Enter task title, description, and select status (`not done`, `in progress`, `done`).
- **2. Update Task**: Enter the task ID and update its fields as needed.
- **3. Delete Task**: Enter the task ID to remove it.
- **4. List All Tasks**: Displays all tasks with their title, description, and status.
- **5. Filter Tasks**: Filter tasks by their status.
- **6. Search Tasks**: Search for tasks containing specific keywords in their title or description.
- **7. Exit**: Exit the program.

## Error Handling

The program handles common errors gracefully, such as:

- Invalid task ID inputs.
- Invalid status inputs (must be `not done`, `in progress`, or `done`).
- Loading malformed JSON data.
- Automatically initializes the `tasks.json` file if it doesn't exist.

## Example

**Adding a task**:

```bash
python3 main.py add "Buy groceries" "Milk, eggs, and bread" "not done"
```

**Updating a task**:

```bash
python3 main.py update 0 "Buy groceries" "Milk, eggs, bread, and butter" "in progress"
```

**Listing all tasks**:

```bash
python3 main.py list
```

**Filtering tasks by status**:

```bash
python3 main.py filter "done"
```

## File Structure

```
Task-Tracker/
│
├── main.py          # Main Python file containing the task management system
├── tasks.json       # JSON file to store tasks (auto-created)
└── README.md        # This README file
```

## Future Enhancements

- Add due dates to tasks.
- Priority tagging for tasks (low, medium, high).
- Enhanced search capabilities (search within descriptions).

## License

This project is open-source and available for use under the MIT License.

---
