import sqlite3

def initialize_database(db_name="navigoals.db"):
    # Define the schema for the database
    schema = """
    -- Main Table: Tasks with assigned dates
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, -- Task name
        date DATE NOT NULL, -- Assigned date for the task
        status TEXT DEFAULT 'pending', -- Task status: 'pending', 'completed', 'failed'
        category TEXT, -- Category: 'study', 'work', 'social', 'personal'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Last update timestamp
    );

    -- Table: Master List (Recurring tasks)
    CREATE TABLE master_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, -- Name of the recurring task
        category TEXT, -- Category: 'study', 'work', 'social', 'personal'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Creation timestamp
    );

    -- Table: Waiting List (Tasks without assigned dates)
    CREATE TABLE waiting_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, -- Name of the task without a defined date
        category TEXT, -- Category: 'study', 'work', 'social', 'personal'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Creation timestamp
    );

    -- Table: Logs (Action records on tasks)
    CREATE TABLE logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER, -- ID of the affected task
        action TEXT, -- Action performed: 'created', 'updated', 'moved', 'deleted'
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Action timestamp
        FOREIGN KEY(task_id) REFERENCES tasks(id) -- Relationship with the tasks table
    );
    """

    try:
        # Connect to the database (it will be created if it doesn't exist)
        with sqlite3.connect(db_name) as conn:
            # Execute the schema
            conn.executescript(schema)
        print(f"Database '{db_name}' created and initialized successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while initializing the database: {e}")

if __name__ == "__main__":
    initialize_database()
