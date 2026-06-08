from datetime import datetime
try:
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
except ModuleNotFoundError:
    from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    task = {"title": title, "description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid task index.")
    tasks[index]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No working currently")
    else:
        for i, task in enumerate(pending):
            print(str(i + 1) + ". Title: " + task["title"] + ", Description: " + task["description"] + ", Due Date: " + task["due_date"])

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0.0
    else:
        completed = sum(1 for task in tasks if task["completed"])
        progress = (completed / len(tasks)) * 100
    return progress
