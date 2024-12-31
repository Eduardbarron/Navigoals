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

def add_task(name, category, date, status="pending", db_name="navigoals.db"):
    """Add a task to the tasks table."""
    query = """
    INSERT INTO tasks (name, category, date, status)
    VALUES (?, ?, ?, ?)
    """
    execute_query(query, (name, category, date, status), db_name)

def get_tasks_by_date(date, db_name="navigoals.db"):
    """Retrieve tasks for a specific date."""
    query = "SELECT id, name, category, status FROM tasks WHERE date(date) = ?"
    return execute_query(query, (date,), db_name)

def update_task_status(task_id, status, db_name="navigoals.db"):
    """Update the status of a task in the database."""
    query = "UPDATE tasks SET status = ? WHERE id = ?"
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (status, task_id))
            conn.commit()  # Ensure changes are saved
    except sqlite3.Error as e:
        print(f"Error updating task: {e}")

def delete_task(task_id, db_name="navigoals.db"):
    """Delete a task from the tasks table."""
    query = "DELETE FROM tasks WHERE id = ?"
    execute_query(query, (task_id,), db_name)
