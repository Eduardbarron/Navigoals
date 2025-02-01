# Navigoals - Personal Goal Tracker

#### Video Demo: [https://youtu.be/R9B_jZDJZSA?si=BkNWonmVRejDr1Fr](https://youtu.be/R9B_jZDJZSA?si=BkNWonmVRejDr1Fr)

## Description:

Navigoals is a command-line productivity tool that helps users efficiently plan, manage, and track their tasks on a daily, weekly, and monthly basis. Built with Python and SQLite, Navigoals provides structured task visualization, completion tracking, and efficiency reporting.

The program is designed to be lightweight yet powerful, incorporating performance tracking and efficiency metrics to help users stay on top of their goals.

Navigoals is a to-do list that allows users to continuously track their tasks without losing sight of past accomplishments. By integrating task management with efficiency tracking, Navigoals gives users real-time feedback on their productivity.

This tool is designed for busy professionals, students, and goal-oriented individuals who need a structured yet flexible system to keep up with their tasks. With dynamic reporting and an intuitive task management system, Navigoals ensures that every effort counts, helping users stay focused, efficient, and motivated.

## Example Workflow:

A user typically starts by installing Navigoals and setting up the database. Once installed, they begin adding tasks through the command-line interface, categorizing them by date and type (work, study, social, personal). Daily, weekly, and monthly reports help the user review their progress and adjust their schedule accordingly.

For example, a student may enter tasks for different assignments and track their completion status, while a freelancer can schedule client projects and measure their efficiency over time. Also, the Master and Waiting Lists allow users to keep track of long-term or recurring tasks, ensuring that nothing is forgotten. By consistently using Navigoals, users integrate it into their routine and develop a more structured approach to managing their goals.

## Features:

- **Task Management**: Allows users to create, modify, delete, and duplicate tasks. This ensures efficient workload management by keeping the to-do list organized and up to date.
    
- **Reports & Analytics**: Helps users track their productivity by generating reports on a daily, weekly, and monthly basis. It provides insights into completed tasks, pending work, and overall efficiency.
    
- **Efficiency Tracking**: Automatically calculates how effectively a user completes their tasks. This helps users assess their performance and make adjustments to improve their workflow.
    
- **Master & Waiting Lists**: The Master List stores recurring tasks that users perform frequently, while the Waiting List holds tasks that do not have a specific deadline yet. This helps users organize their workload efficiently and ensures that no task is forgotten.
    
- **Dynamic Time Management**: Allows users to reschedule and move tasks to different dates based on priority or availability, making it easier to adapt to changing schedules.
    
- **Database-Driven Persistence**: Uses SQLite to store tasks permanently, preventing data loss and allowing users to track their progress over long periods.
    

## Files and Their Functions:

### 1. `main.py` - Core program

Handles user interactions, task management, and reports.

### 2. `db_utils.py` - Database operations

- Manages task storage and retrieval.
    
- Provides methods for adding, updating, and deleting tasks.
    

### 3. `utils.py` - Helper functions

- Provides selection menus for task type and time management.
    
- Computes efficiency scores based on task completion.
    

### 4. `schema.sql` - Database schema

Defines the structure for task management, including daily tasks, master lists, and waiting lists.

### 5. `README.md` - Project documentation

Provides instructions, descriptions, and future development plans.

## Prerequisites:

- **Python 3.x**: Required to run the script since Navigoals is built using Python.
    
- **SQLite**: A lightweight database system used for storing and managing task data efficiently.
    
- **Datetime**: A built-in Python library used for handling task deadlines, timestamps, and report generation.
    
- **Tabulate**: A library used to format data into readable tables in the command-line interface, improving report visualization.
    

## Installation:

```
git clone https://github.com/yourusername/navigoals.git
cd navigoals
```

## Initialize database:

```
python initialize_db.py

```

## Running the Program:

```
python main.py

```

## Basic Usage:

1. Manage Tasks → Add Task → Update Tasks ( Mark tasks as Done, Failed, Moved, or Cancelled) → Cancel task → Copy Task.
    
2. Generate Reports → View Reports → Choose Daily, Weekly, or Monthly Report.
    
3. Watch Lists: → View daily list → View Master & Waiting list → Copy task fast.
    
4. Exit → exits the program.
    
## In conclusion...

Navigoals is a productivity tool designed to help users manage their daily, weekly, and monthly tasks efficiently. It tracks task completion, calculates efficiency scores, and provides detailed reports to help users improve their productivity over time.


## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Acknowledgments

Navigoals was developed as the final project for Harvard’s CS50 course, blending programming knowledge with practical problem-solving skills.

Special thanks to Professor David Malan, Harvard University and the entire CS50 staff for sharing their invaluable knowledge.

If you have feedback, ideas, or simply want to connect, feel free to reach out:
- **Name**: [Jesús Eduardo Barrón Aguilar]
- **Email**: [xeduardo.barron@gmail.com]
- **GitHub**: [https://github.com/Eduardbarron]

If you found this project useful and want to support future developments, please consider buying me coding fuel (aka coffee) at  
[Buy Me a Coffee](https://www.buymeacoffee.com/Eduardbarron) (optional, but greatly appreciated!)

Thank you for exploring Navigoals. I hope it's useful to you.

