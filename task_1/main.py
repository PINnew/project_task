import db_utils


def main():
    """Основная функция для выполнения операций с базой данных."""
    conn = db_utils.create_connection()
    if conn is None:
        return

    db_utils.create_table(conn)

    # Добавляем тестовые записи
    db_utils.insert_employee(conn, "Иван", "Разработчик", 55000)
    db_utils.insert_employee(conn, "Петр", "Аналитик", 48000)
    db_utils.insert_employee(conn, "Анна", "Менеджер", 62000)
    db_utils.insert_employee(conn, "Ольга", "Тестировщик", 51000)
    db_utils.insert_employee(conn, "Дмитрий", "Дизайнер", 49000)

    # Выводим сотрудников с зарплатой больше 50000
    employees = db_utils.get_employees_with_salary_greater_than(conn, 50000)
    print("\nСотрудники с зарплатой больше 50000:")
    for employee in employees:
        print(employee)

    # Обновляем зарплату сотрудника "Иван"
    db_utils.update_employee_salary(conn, "Иван", 60000)

    # Удаляем сотрудника "Анна"
    db_utils.delete_employee(conn, "Анна")

    # Закрываем соединение
    conn.close()


if __name__ == "__main__":
    main()