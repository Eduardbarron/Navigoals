import sqlite3

def connect_to_db(db_name="navigoals.db"):
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(db_name)

def execute_query(query, params=(), db_name="navigoals.db"):
    """Execute a query with optional parameters."""
    try:
        with connect_to_db(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def add_task(name, category, date=None, list_type="daily", db_name="navigoals.db"):
    """Add a task to the specified list."""
    if list_type == "daily":
        # Calculate the next daily_id for the given date
        query_get_id = "SELECT MAX(daily_id) FROM tasks WHERE date = ?"
        result = execute_query(query_get_id, (date,), db_name)
        daily_id = (result[0][0] or 0) + 1

        # Insert the new task into the daily tasks table
        query = """
        INSERT INTO tasks (date, daily_id, name, category, status)
        VALUES (?, ?, ?, ?, 'pending')
        """
        execute_query(query, (date, daily_id, name, category), db_name)
    elif list_type == "master":
        # Insert into master_list
        query = """
        INSERT INTO master_list (name, category)
        VALUES (?, ?)
        """
        execute_query(query, (name, category), db_name)
    elif list_type == "waiting":
        # Insert into waiting_list
        query = """
        INSERT INTO waiting_list (name, category)
        VALUES (?, ?)
        """
        execute_query(query, (name, category), db_name)


def get_tasks_by_date(date, db_name="navigoals.db"):
    """Retrieve tasks for a specific date."""
    query = "SELECT daily_id, name, category, status FROM tasks WHERE date = ? ORDER BY daily_id"
    return execute_query(query, (date,), db_name)

def update_task_status(daily_id, status, date, db_name="navigoals.db"):
    """Update the status of a task in the database."""
    query = "UPDATE tasks SET status = ? WHERE daily_id = ? AND date = ?"
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (status, daily_id, date))
            conn.commit()  # Ensure changes are saved
    except sqlite3.Error as e:
        print(f"Error updating task: {e}")

def delete_task(task_id, table="tasks", db_name="navigoals.db"):
    """Delete a task from the specified table."""
    query = f"DELETE FROM {table} WHERE id = ?"
    execute_query(query, (task_id,), db_name)


def get_master_list(db_name="navigoals.db"):
    """Retrieve all tasks from the Master List."""
    query = "SELECT id, name, category FROM master_list"
    return execute_query(query, (), db_name)

def get_waiting_list(db_name="navigoals.db"):
    """Retrieve all tasks from the Waiting List."""
    query = "SELECT id, name, category FROM waiting_list"
    return execute_query(query, (), db_name)

def get_tasks_by_range(start_date, end_date, db_name="navigoals.db"):
    """Fetch tasks within a specific date range."""
    query = """
    SELECT daily_id, name, category, status, date 
    FROM tasks
    WHERE date BETWEEN ? AND ?
    ORDER BY date, daily_id
    """
    return execute_query(query, (start_date, end_date), db_name)

