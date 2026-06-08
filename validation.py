from datetime import datetime

def validate_task_title(title):
    if not title or len(title) == 0:
        raise ValueError("Task title cannot be empty.")
    if len(title) > 100:
        raise ValueError("Task title cannot exceed 100 characters.")
    return True

def validate_task_description(description):
    if not description or len(description) == 0:
        raise ValueError("Task description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Task description cannot exceed 500 characters.")
    return True

def validate_due_date(due_date):
    if not due_date or len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return True
