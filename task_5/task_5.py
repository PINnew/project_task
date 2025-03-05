def analyze_list(input_list):
    """
    Анализирует список чисел и возвращает:
    1. Количество уникальных чисел.
    2. Второе по величине число в списке.
    3. Список чисел, которые делятся на 3 без остатка.
    """

    # 1. Количество уникальных чисел
    unique_numbers = set(input_list)
    unique_count = len(unique_numbers)

    # 2. Второе по величине число в списке
    sorted_unique_numbers = sorted(list(unique_numbers), reverse=True)
    second_largest = sorted_unique_numbers[1] if len(sorted_unique_numbers) > 1 else None

    # 3. Список чисел, которые делятся на 3 без остатка
    divisible_by_3 = [num for num in input_list if num % 3 == 0]

    return unique_count, second_largest, divisible_by_3


# Пример использования
if __name__ == "__main__":
    input_list = [10, 20, 30, 40, 50, 30, 20]
    unique_count, second_largest, divisible_by_3 = analyze_list(input_list)

    print(f"Уникальные числа: {unique_count}")
    print(f"Второе по величине число: {second_largest}")
    print(f"Числа, делящиеся на 3: {divisible_by_3}")