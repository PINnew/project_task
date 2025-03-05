# project_task/task_4/db_utils.py
import sqlite3


def create_connection(db_name="employees.db"):
    """Создает подключение к базе данных SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None


def create_table(conn):
    """Создает таблицу employees, если она не существует."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            CREATE TABLE IF NOT EXISTS employees (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT NOT NULL,  
                position TEXT NOT NULL,  
                salary REAL NOT NULL  
            )  
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")


def insert_employee(conn, employee):
    """Вставляет данные о сотруднике в таблицу."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            INSERT INTO employees (name, position, salary)  
            VALUES (?, ?, ?)  
        """, (employee["name"], employee["position"], employee["salary"]))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при вставке данных: {e}")

def find_employees_by_position(conn, position):
    """Находит сотрудников по должности."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            SELECT * FROM employees WHERE position = ?  
        """, (position,))
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Ошибка при поиске сотрудников: {e}")
        return None

def update_salary(conn, name, new_salary):
    """Обновляет зарплату сотрудника по имени."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            UPDATE employees SET salary = ? WHERE name = ?  
        """, (new_salary, name))
        conn.commit()
        return cursor.rowcount  # Возвращает количество обновленных строк
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении зарплаты: {e}")
        return 0