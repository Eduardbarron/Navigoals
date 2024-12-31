# Import the necessary modules
from utils import select_task, select_task_type, select_time  # Utility functions
from db_utils import add_task, get_tasks_by_date, update_task_status, delete_task  # Placeholder for TASK operations
# Import additional functions as needed (e.g., reports)
import datetime  # Module for working with dates
from tabulate import tabulate  # For displaying tables

def main_menu():
    """Main menu of the program."""
    while True:
        print("\n🌟 Welcome to Navigoals! 🌟")
        print()

        # Fetch today's tasks
        today = datetime.date.today().isoformat()  # Fetch current date in YYYY-MM-DD format        print(f"Today is {today}")
        print(f"today is {today}")
        print()

        tasks = get_tasks_by_date(today)

    
        if tasks:
            print("\n Today's Goals 🗓️")
            # Display tasks as a table with column headers
            headers = ["ID", "Name", "Category", "Status"]
            print(tabulate(tasks, headers=headers, tablefmt="pretty"))
        else:
            print("No goals today 📭")

        print()
        print("1. Manage Tasks 📝")
        print("2. View Reports 📊")
        print("3. Exit 🚪")
        print()
        choice = input("Select an option: ")

        if choice == "1":
            manage_tasks()
        elif choice == "2":
            view_reports()
        elif choice == "3":
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
        print("5 Master List")
        print("6 Waiting List")
        print("7 Back to Main Menu")
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
            master_list_menu()
        elif choice == "6":
            waiting_list_menu()
        elif choice == "7":
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
        print("4 See Log")
        print("5 Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            daily_report()
        elif choice == "2":
            weekly_report()
        elif choice == "3":
            monthly_report()
        elif choice == "4":
            see_log()
        elif choice == "5":
            return
        else:
            print("❌ Invalid option, please try again.")


#Functions for Tasks

def add_task_menu():
    """Add a new task."""
    print("\n➕ Adding a new task...")
    task_name = input("Enter the task name: ").strip()
    task_type = select_task_type()
    task_time = select_time()

    if task_type and task_time:
        add_task(task_name, task_type, task_time)  # Assumes `add_task` in db_utils handles the database insertion
        print(f"✅ Task '{task_name}' added successfully as {task_type} for {task_time}.")
    else:
        print("❌ Task creation canceled due to invalid input.")


def update_task_menu():
    """Update an existing task."""
    print("\n✏️ Updating a task...")
    tasks = get_tasks_by_date(datetime.date.today().isoformat())

    if not tasks:
        print("No tasks available to update.")
        return

    task_to_update = select_task(tasks)
    if not task_to_update:
        print("Update canceled.")
        return

    task_id = task_to_update[0]  # Extract ID from task tuple
    print("Choose a new status:")
    print("1) Done ✅")
    print("2) Failed ❌")
    print("3) Moved 📦")
    print("4) Cancelled 🚫")
    
    new_status_options = {"1": "Done ✅", "2": "Failed ❌", "3": "Moved 📦", "4": "Cancelled 🚫"}
    new_status_choice = input("Enter the number of the new status: ").strip()

    new_status = new_status_options.get(new_status_choice)
    if new_status:
        update_task_status(task_id, new_status)  # Call the update function
        print(f"✅ Task '{task_to_update[1]}' updated successfully to '{new_status}'.")
    else:
        print("❌ Update canceled due to invalid input.")


def delete_task_menu():
    """Delete a task."""
    print("\n🗑️ Deleting a task...")
    tasks = get_tasks_by_date(datetime.date.today().isoformat())

    if not tasks:
        print("No tasks available to delete.")
        return

    task_to_delete = select_task(tasks)
    if not task_to_delete:
        print("Delete canceled.")
        return

    confirm = input(f"Are you sure you want to delete the task '{task_to_delete}'? (y/n): ").strip().lower()
    if confirm == 'y':
        delete_task(task_to_delete)
        print(f"✅ Task '{task_to_delete}' deleted successfully.")
    else:
        print("❌ Delete canceled.")

def copy_task_menu():
    """Copy an existing task."""
    print("\n📋 Copying a task...")
    tasks = get_tasks_by_date(datetime.date.today().isoformat())

    if not tasks:
        print("No tasks available to copy.")
        return

    task_to_copy = select_task(tasks)
    if not task_to_copy:
        print("Copy canceled.")
        return

    new_time = select_time()
    if new_time:
        add_task(task_to_copy, "Copied Task", new_time)  # Adds the copied task with the new time
        print(f"✅ Task '{task_to_copy}' copied successfully to {new_time}.")
    else:
        print("❌ Copy canceled due to invalid input.")

def master_list_menu():
    """Access the master list of recurring tasks."""
    print("\n📚 Accessing the Master List...")
    # Logic to view and interact with the master list
    pass

def waiting_list_menu():
    """Access the waiting list of unscheduled tasks."""
    print("\n⏳ Accessing the Waiting List...")
    # Logic to view and interact with the waiting list
    pass

# Placeholder Functions for Reports
def daily_report():
    """Generate a daily report."""
    print("\n📅 Generating daily report...")
    # You will call get_tasks_by_date() or similar here
    pass

def weekly_report():
    """Generate a weekly report."""
    print("\n📅 Generating weekly report...")
    # Logic to fetch tasks for the week
    pass

def monthly_report():
    """Generate a monthly report."""
    print("\n📅 Generating monthly report...")
    # Logic to fetch tasks for the month
    pass

def see_log():
    """View the activity log."""
    print("\n📜 Viewing the log...")
    # Logic to fetch and display log entries
    pass

# Entry Point
if __name__ == "__main__":
    main_menu()
