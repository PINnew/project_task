# project_task/task_4/main.py
import csv
from db_utils import create_connection, create_table, insert_employee, find_employees_by_position, update_salary


def read_employees_from_csv(filename="employees.csv"):
    """Читает данные о сотрудниках из CSV-файла."""
    employees = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                employees.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return employees


def main():
    """Основная логика скрипта."""
    # 1. Подключение к базе данных
    conn = create_connection()
    if conn is None:
        return

    # 2. Создание таблицы
    create_table(conn)

    # 3. Чтение данных из CSV-файла
    employees = read_employees_from_csv()
    if not employees:
        return

    # 4. Запись данных в базу данных
    for employee in employees:
        insert_employee(conn, employee)

    # 5. Поиск сотрудников по должности
    position_to_find = "разработчик"
    developers = find_employees_by_position(conn, position_to_find)
    print(f"Сотрудники с должностью '{position_to_find}':")
    for dev in developers:
        print(dev)

    # 6. Обновление зарплаты сотрудника
    employee_name = "Анна"
    new_salary = 50000
    updated_rows = update_salary(conn, employee_name, new_salary)
    if updated_rows > 0:
        print(f"Зарплата сотрудника '{employee_name}' успешно обновлена до {new_salary}.")
    else:
        print(f"Не удалось обновить зарплату сотрудника '{employee_name}'.")

    # 7. Закрытие соединения с базой данных
    conn.close()


if __name__ == "__main__":
    main()