import sqlite3

DATABASE_NAME = 'employees.db'


def create_connection():
    """Создает подключение к базе данных SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None


def create_table(conn):
    """Создает таблицу 'employees', если она не существует."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            CREATE TABLE IF NOT EXISTS employees (  
                id INTEGER PRIMARY KEY,  
                name TEXT NOT NULL,  
                position TEXT,  
                salary REAL  
            )  
        """)
        conn.commit()
        print("Таблица 'employees' успешно создана")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")


def insert_employee(conn, name, position, salary):
    """Добавляет нового сотрудника в таблицу."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            INSERT INTO employees (name, position, salary)  
            VALUES (?, ?, ?)  
        """, (name, position, salary))
        conn.commit()
        print(f"Сотрудник {name} успешно добавлен")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении сотрудника: {e}")


def get_employees_with_salary_greater_than(conn, salary):
    """Возвращает список сотрудников с зарплатой выше указанной."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            SELECT * FROM employees  
            WHERE salary > ?  
        """, (salary,))
        employees = cursor.fetchall()
        return employees
    except sqlite3.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []


def update_employee_salary(conn, name, salary):
    """Обновляет зарплату сотрудника по имени."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            UPDATE employees  
            SET salary = ?  
            WHERE name = ?  
        """, (salary, name))
        conn.commit()
        print(f"Зарплата сотрудника {name} успешно обновлена")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении зарплаты: {e}")


def delete_employee(conn, name):
    """Удаляет сотрудника по имени."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            DELETE FROM employees  
            WHERE name = ?  
        """, (name,))
        conn.commit()
        print(f"Сотрудник {name} успешно удален")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении сотрудника: {e}")