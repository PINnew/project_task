def process_employees_data(employees):
    """
    Обрабатывает данные о сотрудниках и возвращает:
    1. Список имен сотрудников с зарплатой больше 50000.
    2. Среднюю зарплату всех сотрудников.
    3. Отсортированный список сотрудников по зарплате в порядке убывания.
    """

    # 1. Список имен сотрудников с зарплатой больше 50000
    high_paid_employees = [emp["name"] for emp in employees if emp["salary"] > 50000]

    # 2. Средняя зарплата всех сотрудников
    total_salary = sum(emp["salary"] for emp in employees)
    average_salary = total_salary / len(employees) if employees else 0

    # 3. Отсортированный список сотрудников по зарплате в порядке убывания
    sorted_employees = sorted(employees, key=lambda emp: emp["salary"], reverse=True)

    return high_paid_employees, average_salary, sorted_employees


# Пример использования (для тестирования)
if __name__ == "__main__":
    employees = [
        {"name": "Иван", "position": "разработчик", "salary": 55000},
        {"name": "Анна", "position": "аналитик", "salary": 48000},
        {"name": "Петр", "position": "тестировщик", "salary": 52000},
        {"name": "Мария", "position": "менеджер", "salary": 60000},
    ]

    high_paid, avg_salary, sorted_emps = process_employees_data(employees)

    print("Сотрудники с зарплатой > 50000:", high_paid)
    print("Средняя зарплата:", avg_salary)
    print("Сотрудники, отсортированные по зарплате (убывание):")
    for emp in sorted_emps:
        print(emp)