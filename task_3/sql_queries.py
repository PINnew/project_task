# 1. Найти общую сумму заказов для каждого клиента.
query_1 = """  
SELECT customer_id, SUM(amount) AS total_amount  
FROM orders  
GROUP BY customer_id;  
"""

# 2. Найти клиента с максимальной суммой заказов.
query_2 = """  
SELECT customer_id  
FROM orders  
GROUP BY customer_id  
ORDER BY SUM(amount) DESC  
LIMIT 1;  
"""

# 3. Найти количество заказов, сделанных в 2023 году.
query_3 = """  
SELECT COUNT(*)  
FROM orders  
WHERE strftime('%Y', order_date) = '2023';  
"""

# 4. Найти среднюю сумму заказа для каждого клиента.
query_4 = """  
SELECT customer_id, AVG(amount) AS average_amount  
FROM orders  
GROUP BY customer_id;  
"""

# Для примера, можно вывести запросы в консоль при запуске файла
if __name__ == "__main__":
    print("Query 1:\n", query_1)
    print("\nQuery 2:\n", query_2)
    print("\nQuery 3:\n", query_3)
    print("\nQuery 4:\n", query_4)