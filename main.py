from utils import (
    select_task, 
    select_task_type, 
    select_time, 
    calculate_efficiency, 
    format_report
)  # Utility functions

from db_utils import (
    add_task, 
    get_tasks_by_date, 
    update_task_status, 
    delete_task, 
    get_master_list, 
    get_waiting_list, 
    get_tasks_by_range,
)  # Database operations

import datetime  # Module for working with dates
from tabulate import tabulate  # For displaying tables

def main_menu():
    """Main menu of the program."""
    while True:
        print("\n🌟 Welcome to Navigoals! 🌟")
        print()

        # Fetch today's tasks
        today = datetime.date.today().isoformat()  # Fetch current date in YYYY-MM-DD format
        print(f"Today is {today}")

        tasks = get_tasks_by_date(today)

        if tasks:
            metrics = calculate_efficiency(tasks)  # Calculate efficiency
            print(f"\nToday's Goals 🗓️  Today's Efficiency: {metrics['efficiency']:.2f}% {metrics['emoji']}")
            # Display tasks as a table with column headers
            headers = ["Daily ID", "Name", "Category", "Status"]
            formatted_tasks = [(task[0], task[1], task[2], task[3]) for task in tasks]  # Extract relevant columns
            print(tabulate(formatted_tasks, headers=headers, tablefmt="pretty"))
        else:
            print("No goals today 📭")

        print()
        print("1. Manage Tasks 📝")
        print("2. View Reports 📊")
        print("3. Watch Lists 👁️")
        print("4. Exit 🚪")
        print()
        choice = input("Select an option: ")

        if choice == "1":
            manage_tasks()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            watch_list_menu()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option, please try again.")

# TASK Management Menu
def manage_tasks():
    """Submenu for managing tasks."""
    while True:
        print("\n📝 Task Management:")
        print("1 Add Task")
        print("2 Update Task")
        print("3 Delete Task")
        print("4 Copy Task")
        print("5 Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            add_task_menu()
        elif choice == "2":
            update_task_menu()
        elif choice == "3":
            delete_task_menu()
        elif choice == "4":
            copy_task_menu()
        elif choice == "5":
            return
        else:
            print("❌ Invalid option, please try again.")

# REPORTS Menu
def view_reports():
    """Submenu for viewing reports."""
    while True:
        print("\n📊 Reports:")
        print("1 Daily Report")
        print("2 Weekly Report")
        print("3 Monthly Report")
        print("4 Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            daily_report()
        elif choice == "2":
            weekly_report()
        elif choice == "3":
            monthly_report()
        elif choice == "4":
            return
        else:
            print("❌ Invalid option, please try again.")

# Functions for Tasks
def add_task_menu():
    """Add a new task."""
    print("\n➕ Adding a new task...")
    print("Where would you like to add the task?")
    print("1. Daily Tasks")
    print("2. Master List")
    print("3. Waiting List")
    list_choice = input("Select an option: ").strip()

    task_name = input("Enter the task name: ").strip()
    task_type = select_task_type()  # Select category
    task_time = None

    if list_choice == "1":
        task_time = select_time()  # Select date for Daily Tasks
        if task_type and task_time:
            add_task(task_name, task_type, task_time, list_type="daily")
            print(f"✅ Task '{task_name}' added successfully as {task_type} for {task_time}.")
        else:
            print("❌ Task creation canceled due to invalid input.")
    elif list_choice == "2":
        if task_type:
            add_task(task_name, task_type, list_type="master")
            print(f"✅ Task '{task_name}' added successfully to the Master List.")
        else:
            print("❌ Task creation canceled due to invalid input.")
    elif list_choice == "3":
        if task_type:
            add_task(task_name, task_type, list_type="waiting")
            print(f"✅ Task '{task_name}' added successfully to the Waiting List.")
        else:
            print("❌ Task creation canceled due to invalid input.")
    else:
        print("❌ Invalid option. Task not added.")

def update_task_menu():
    """Update one or multiple existing tasks."""
    print("\n✏️ Updating tasks...")
    today = datetime.date.today().isoformat()
    tasks = get_tasks_by_date(today)

    if not tasks:
        print("No tasks available to update.")
        return

    tasks_to_update = select_task(tasks, multi_select=True)  # Allow multiple selections
    if not tasks_to_update:
        print("Update canceled.")
        return

    print("Choose a new status:")
    print("1) Done ✅")
    print("2) Failed ❌")
    print("3) Moved 📦")
    print("4) Cancelled 🚫")
    
    new_status_options = {"1": "Done ✅", "2": "Failed ❌", "3": "Moved 📦", "4": "Cancelled 🚫"}
    new_status_choice = input("Enter the number of the new status: ").strip()

    new_status = new_status_options.get(new_status_choice)
    if new_status:
        for task in tasks_to_update:
            daily_id = task[0]  # Extract Daily ID
            update_task_status(daily_id, new_status, today)  # Pass daily_id and date
            print(f"✅ Task '{task[1]}' updated successfully to '{new_status}'.")
    else:
        print("❌ Update canceled due to invalid input.")

def delete_task_menu():
    """Delete one or multiple tasks."""
    print("\n🗑️ Deleting tasks...")
    print("1. Delete from Today's Tasks")
    print("2. Delete from Master List")
    print("3. Delete from Waiting List")
    print("4. Back to Main Menu")
    choice = input("Select an option: ").strip()

    if choice == "1":
        tasks = get_tasks_by_date(datetime.date.today().isoformat())
        if not tasks:
            print("No tasks available to delete.")
            return

        tasks_to_delete = select_task(tasks, multi_select=True)  # Allow multiple selections
        if not tasks_to_delete:
            print("Delete canceled.")
            return

        for task in tasks_to_delete:
            daily_id = task[0]  # Extract Daily ID from task tuple
            confirm = input(f"Are you sure you want to delete the task '{task[1]}'? (y/n): ").strip().lower()
            if confirm == 'y':
                delete_task(daily_id, table="tasks")  # Call the delete function
                print(f"✅ Task '{task[1]}' deleted successfully.")
            else:
                print(f"❌ Task '{task[1]}' delete canceled.")

    elif choice == "2":
        print("\n📚 Deleting from Master List...")
        master_tasks = get_master_list()
        if not master_tasks:
            print("No tasks available in the Master List.")
            return

        tasks_to_delete = select_task(master_tasks, multi_select=True)  # Allow multiple selections
        if not tasks_to_delete:
            print("Delete canceled.")
            return

        for task in tasks_to_delete:
            task_id = task[0]  # Extract task ID from tuple
            confirm = input(f"Are you sure you want to delete the task '{task[1]}'? (y/n): ").strip().lower()
            if confirm == 'y':
                delete_task(task_id, table="master_list")  # Call the delete function
                print(f"✅ Task '{task[1]}' deleted successfully from Master List.")
            else:
                print(f"❌ Task '{task[1]}' delete canceled.")

    elif choice == "3":
        print("\n⏳ Deleting from Waiting List...")
        waiting_tasks = get_waiting_list()
        if not waiting_tasks:
            print("No tasks available in the Waiting List.")
            return

        tasks_to_delete = select_task(waiting_tasks, multi_select=True)  # Allow multiple selections
        if not tasks_to_delete:
            print("Delete canceled.")
            return

        for task in tasks_to_delete:
            task_id = task[0]  # Extract task ID from tuple
            confirm = input(f"Are you sure you want to delete the task '{task[1]}'? (y/n): ").strip().lower()
            if confirm == 'y':
                delete_task(task_id, table="waiting_list")  # Call the delete function
                print(f"✅ Task '{task[1]}' deleted successfully from Waiting List.")
            else:
                print(f"❌ Task '{task[1]}' delete canceled.")

    elif choice == "4":
        return

    else:
        print("❌ Invalid option. Please try again.")

def copy_task_menu():
    """Copy one or multiple existing tasks."""
    print("\n📋 Copying tasks...")
    tasks = get_tasks_by_date(datetime.date.today().isoformat())

    if not tasks:
        print("No tasks available to copy.")
        return

    tasks_to_copy = select_task(tasks, multi_select=True)  # Allow multiple selections
    if not tasks_to_copy:
        print("Copy canceled.")
        return

    new_time = select_time()
    if new_time:
        for task in tasks_to_copy:
            add_task(task[1], task[2], new_time)  # Adds the copied task with the new time
            print(f"✅ Task '{task[1]}' copied successfully to {new_time}.")
    else:
        print("❌ Copy canceled due to invalid input.")

def watch_list_menu():
    """Submenu for viewing different task lists."""
    while True:
        print("\n👁️ Watch List Menu:")
        print("1. See List by Day")
        print("2. View Master List")
        print("3. View Waiting List")
        print("4. Copy Task(s) from a List")
        print("5. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\nSelect a Date:")
            print("1. Tomorrow")
            print("2. Yesterday")
            print("3. Select Date")
            date_choice = input("Choose an option: ").strip()

            if date_choice == "1":
                date = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
            elif date_choice == "2":
                date = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
            elif date_choice == "3":
                date = input("Enter the date (YYYY-MM-DD): ").strip()
                try:
                    datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                except ValueError:
                    print("Invalid date format. Please try again.")
                    continue
            else:
                print("Invalid option. Returning to Watch List Menu.")
                continue

            tasks = get_tasks_by_date(date)
            if tasks:
                print("\nTasks for the day:")
                headers = ["Daily ID", "Name", "Category", "Status"]
                formatted_tasks = [(task[0], task[1], task[2], task[3]) for task in tasks]
                print(tabulate(formatted_tasks, headers=headers, tablefmt="pretty"))
            else:
                print("No tasks found for this day.")
        elif choice == "2":
            print("\n📚 Viewing the Master List...")
            master_tasks = get_master_list()
            if master_tasks:
                headers = ["ID", "Name", "Category"]
                print(tabulate(master_tasks, headers=headers, tablefmt="pretty"))
            else:
                print("No tasks in the Master List.")

        elif choice == "3":
            print("\n⏳ Viewing the Waiting List...")
            waiting_tasks = get_waiting_list()
            if waiting_tasks:
                headers = ["ID", "Name", "Category"]
                print(tabulate(waiting_tasks, headers=headers, tablefmt="pretty"))
            else:
                print("No tasks in the Waiting List.")

        elif choice == "4":
            print("\n📋 Copying Task(s) from a List...")
            print("1. Copy from Master List")
            print("2. Copy from Waiting List")
            list_choice = input("Select the list to copy from: ").strip()

            if list_choice == "1":
                tasks = get_master_list()
            elif list_choice == "2":
                tasks = get_waiting_list()
            else:
                print("❌ Invalid list selection.")
                continue

            if not tasks:
                print("No tasks available in the selected list.")
                continue

            print("Select tasks to copy by entering their IDs (comma-separated). Use '*' to select all.")
            task_selection = input("Enter the task ID(s) or '*': ").strip()

            if task_selection == "*":
                selected_tasks = tasks
            else:
                try:
                    selected_ids = [int(x) for x in task_selection.split(",") if x.strip().isdigit()]
                    selected_tasks = [task for task in tasks if task[0] in selected_ids]
                except ValueError:
                    print("❌ Invalid input. Please try again.")
                    continue

            if not selected_tasks:
                print("❌ No valid tasks selected.")
                continue

            new_time = select_time()
            if new_time:
                for task in selected_tasks:
                    add_task(task[1], task[2], new_time)  # Adds the copied task with the new time
                    print(f"✅ Task '{task[1]}' copied successfully to {new_time}.")
            else:
                print("❌ Copy canceled due to invalid time selection.")

        elif choice == "5":
            return

        else:
            print("❌ Invalid option, please try again.")

# Placeholder Functions for Reports
def daily_report():
    """Generate a daily report."""
    print("\nGenerating daily report...")
    print("1. Today")
    print("2. Yesterday")
    print("3. Select Date")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        report_date = datetime.date.today()
    elif choice == "2":
        report_date = datetime.date.today() - datetime.timedelta(days=1)
    elif choice == "3":
        report_date = input("Enter the date (YYYY-MM-DD): ").strip()
        try:
            report_date = datetime.datetime.strptime(report_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please try again.")
            return
    else:
        print("Invalid option. Returning to Reports Menu.")
        return

    # Fetch tasks for the selected date
    tasks = get_tasks_by_date(report_date.isoformat())

    if not tasks:
        print(f"No tasks found for {report_date}.")
        return

    # Calculate metrics and format report
    metrics = calculate_efficiency(tasks)
    format_report(metrics, tasks)

def weekly_report():
    """Generate a weekly report."""
    print("\nGenerating weekly report...")
    print("1. Current Week")
    print("2. Select Start Date for Week")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())  # Monday
        end_of_week = start_of_week + datetime.timedelta(days=6)  # Sunday
    elif choice == "2":
        start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
        try:
            start_of_week = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_of_week = start_of_week + datetime.timedelta(days=6)
        except ValueError:
            print("Invalid date format. Please try again.")
            return
    else:
        print("Invalid option. Returning to Reports Menu.")
        return

    # Fetch tasks for the week
    tasks = get_tasks_by_range(start_of_week.isoformat(), end_of_week.isoformat())

    if not tasks:
        print(f"No tasks found from {start_of_week} to {end_of_week}.")
        return

    # Calculate metrics and format report
    metrics = calculate_efficiency(tasks)
    print(f"\nWeekly Report ({start_of_week} to {end_of_week})")
    format_report(metrics, tasks)


def monthly_report():
    """Generate a monthly report."""
    print("\nGenerating monthly report...")
    print("1. Current Month")
    print("2. Select Month and Year")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        today = datetime.date.today()
        start_of_month = today.replace(day=1)
        end_of_month = (start_of_month + datetime.timedelta(days=31)).replace(day=1) - datetime.timedelta(days=1)
    elif choice == "2":
        month_year = input("Enter the month and year (MM-YYYY): ").strip()
        try:
            start_of_month = datetime.datetime.strptime(month_year, "%m-%Y").date().replace(day=1)
            end_of_month = (start_of_month + datetime.timedelta(days=31)).replace(day=1) - datetime.timedelta(days=1)
        except ValueError:
            print("Invalid date format. Please try again.")
            return
    else:
        print("Invalid option. Returning to Reports Menu.")
        return

    # Fetch tasks for the month
    tasks = get_tasks_by_range(start_of_month.isoformat(), end_of_month.isoformat())

    if not tasks:
        print(f"No tasks found from {start_of_month} to {end_of_month}.")
        return

    # Calculate metrics and format report
    metrics = calculate_efficiency(tasks)
    print(f"\nMonthly Report ({start_of_month} to {end_of_month})")
    format_report(metrics, tasks)

# Entry Point
if __name__ == "__main__":
    main_menu()