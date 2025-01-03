import datetime

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
