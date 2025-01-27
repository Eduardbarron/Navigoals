import datetime
from tabulate import tabulate

# Utils module for handling common interactions

def select_task(tasks, multi_select=False):
    """Allow user to select one or multiple tasks."""
    print("\nSelect a task:")
    for task in tasks:
        if len(task) == 3:  # Master List or Waiting List format
            print(f"{task[0]}: {task[1]} ({task[2]})")  # id, name, category
        elif len(task) == 4:  # Daily tasks format
            print(f"{task[0]}: {task[1]} ({task[2]}) - {task[3]}")  # daily_id, name, category, status

    if multi_select:
        selection = input("Enter the task ID(s), comma-separated (or '*' for all): ").strip()
        if selection == "*":
            return tasks
        try:
            selected_ids = [int(x) for x in selection.split(",") if x.strip().isdigit()]
            return [task for task in tasks if task[0] in selected_ids]
        except ValueError:
            print("❌ Invalid input. Please try again.")
            return None
    else:
        try:
            selected_id = int(input("Enter the task ID: ").strip())
            return next((task for task in tasks if task[0] == selected_id), None)
        except ValueError:
            print("❌ Invalid input. Please try again.")
            return None

def select_task_type():
    """
    Prompt the user to select a task type.
    Returns the selected type.
    """
    types = {"1": "Work 💼", "2": "Study 📘", "3": "Social 👥", "4": "Personal 🏠"}
    retries = 0
    while retries < 2:
        print("\nTask Types:")
        for key, value in types.items():
            print(f"{key}. {value}")

        choice = input("Select a task type: ").strip()
        if choice in types:
            return types[choice]

        print("Invalid input. Try again.")
        retries += 1

    print("Returning to main menu.")
    return None

def select_time():
    """
    Prompt the user to select a time for the task.
    Returns the selected date.
    """
    retries = 0
    while retries < 2:
        print("\nSelect Time:")
        print("1. Today")
        print("2. Tomorrow")
        print("3. Weeks from now")
        print("4. Months from now")
        print("5. Free date (YYYY-MM-DD)")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            return datetime.date.today().isoformat()
        elif choice == "2":
            return (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
        elif choice == "3":
            weeks = input("Enter the number of weeks: ").strip()
            if weeks.isdigit():
                return (datetime.date.today() + datetime.timedelta(weeks=int(weeks))).isoformat()
        elif choice == "4":
            months = input("Enter the number of months: ").strip()
            if months.isdigit():
                today = datetime.date.today()
                month = (today.month - 1 + int(months)) % 12 + 1
                year = today.year + (today.month - 1 + int(months)) // 12
                day = min(today.day, (datetime.date(year, month, 28) + datetime.timedelta(days=4)).day)
                return datetime.date(year, month, day).isoformat()
        elif choice == "5":
            free_date = input("Enter a date (YYYY-MM-DD): ").strip()
            try:
                datetime.datetime.strptime(free_date, "%Y-%m-%d")
                return free_date
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        print("Invalid input. Try again.")
        retries += 1

    print("Returning to main menu.")
    return None

def calculate_efficiency(tasks):
    """Calculate efficiency and task metrics."""
    # Treat all "Pending" tasks as "Failed ❌" for efficiency calculation
    efficiency_tasks = [task for task in tasks if task[3] in ["Done ✅", "pending", "Failed ❌"]]
    completed_tasks = sum(1 for task in efficiency_tasks if task[3] == "Done ✅")
    failed_tasks = sum(1 for task in efficiency_tasks if task[3] in ["pending", "Failed ❌"])
    moved_or_cancelled = len(tasks) - len(efficiency_tasks)

    # Efficiency is calculated based on "Done ✅" tasks only
    efficiency = (completed_tasks / len(efficiency_tasks) * 100) if efficiency_tasks else 0

    emoji = ""
    if efficiency == 0:
        emoji = "⚪"  # No progress
    elif efficiency < 50:
        emoji = "🟥"  # Red square
    elif 50 <= efficiency <= 80:
        emoji = "🟧"  # Orange square
    elif 81 <= efficiency <= 95:
        emoji = "🟩"  # Green square
    elif 96 <= efficiency <= 100:
        emoji = "🌟"  # star
    
    return {
        "total_tasks": len(tasks),
        "completed_tasks": completed_tasks,
        "failed_tasks": failed_tasks,
        "moved_or_cancelled": moved_or_cancelled,
        "efficiency": efficiency,
        "emoji": emoji
    }



def format_report(metrics, tasks):
    """Format and print the report."""
    print("\nReport Summary")
    print("===============")
    print(f"Total Tasks: {metrics['total_tasks']}")
    print(f"Completed Tasks: {metrics['completed_tasks']}")
    print(f"Failed Tasks: {metrics['failed_tasks']}")
    print(f"Moved/Cancelled Tasks: {metrics['moved_or_cancelled']}")
    print(f"Efficiency: {metrics['efficiency']:.2f}%")

    headers = ["Daily ID", "Name", "Category", "Status", "Date"]
    print("\nTask Details:")
    print(tabulate(tasks, headers=headers, tablefmt="pretty"))
