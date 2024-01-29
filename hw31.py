import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_name TEXT,
        emp_age INTEGER
    )
''')

data_employees = [
  ('Avtandil Javrishvili', 17),
    ('Nini Jabanashvili', 18),
    ('Giorgi Pataridze', 16),
    ('Elza ositashvili', 47),
    ('Nika Cicqishvili', 25)
]

cursor.executemany('INSERT INTO employees (emp_name, emp_age) VALUES (?, ?)', data_employees)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee_tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_description TEXT,
        emp_id INTEGER,
        FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
    )
''')


data_employee_tasks = [
    ('Task 1', 1),
    ('Task 2', 2),
    ('Task 3', 3),
    ('Task 4', 4),
    ('Task 5', 5)
]

cursor.executemany('INSERT INTO employee_tasks (task_description, emp_id) VALUES (?, ?)', data_employee_tasks)

cursor.execute('UPDATE employees SET emp_age = 31 WHERE emp_name = "Jane Smith"')

cursor.execute('DELETE FROM employee_tasks WHERE task_description = "Task 3"')

cursor.execute('''
    CREATE VIEW combined_view AS
    SELECT employees.emp_id, emp_name, emp_age, task_id, task_description
    FROM employees
    LEFT JOIN employee_tasks ON employees.emp_id = employee_tasks.emp_id
''')

conn.commit()
conn.close()
