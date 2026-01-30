# To-Do List Application

A simple command-line to-do list application built with Python. Manage your tasks efficiently with add, view, update, and delete functionality.

## Features

- **Add Tasks** - Create new tasks with descriptions
- **View Tasks** - Display all tasks with their status
- **Update Tasks** - Mark tasks as done or edit descriptions
- **Delete Tasks** - Remove completed or unwanted tasks
- **Persistent Storage** - Tasks are saved to a JSON file

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Devil16VS/to-do-list.git
cd to-do-list
```

2. Run the application:
```bash
python "to do list.py"
```

## Usage

The application presents a menu with the following options:

1. **Add Task** - Enter a task description
2. **View Tasks** - See all your tasks with status indicators
3. **Update Task** - Modify a task (mark as done or edit description)
4. **Delete Task** - Remove a task
5. **Exit** - Close the application

Tasks are stored in `tasks.json` and automatically saved after each operation.

## File Structure

- `to do list.py` - Main application script
- `tasks.json` - Storage file for your tasks
- `demo_tasks.json` - Example tasks file

## License

Open source project