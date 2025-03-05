import psycopg2

# Параметры подключения к базе данных
DB_NAME = "products_db"
DB_USER = "postgres"  # Измените, если у вас другой пользователь
DB_PASSWORD = "your_password"  # Измените на ваш пароль
DB_HOST = "localhost"
DB_PORT = "5432"


def connect_to_db():
    """Подключается к базе данных PostgreSQL."""
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        return conn
    except psycopg2.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None


def create_table(conn):
    """Создает таблицу products."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            CREATE TABLE IF NOT EXISTS products (  
                id SERIAL PRIMARY KEY,  
                name VARCHAR(255) NOT NULL,  
                price DECIMAL(10, 2) NOT NULL,  
                quantity INTEGER NOT NULL  
            )  
        """)
        conn.commit()
        print("Таблица 'products' успешно создана.")
    except psycopg2.Error as e:
        print(f"Ошибка при создании таблицы: {e}")


def insert_products(conn):
    """Добавляет 10 тестовых продуктов."""
    products = [
        ("Laptop", 1200.00, 5),
        ("Mouse", 25.00, 50),
        ("Keyboard", 75.00, 20),
        ("Monitor", 300.00, 8),
        ("Headphones", 100.00, 12),
        ("Webcam", 50.00, 15),
        ("USB Drive", 15.00, 100),
        ("External Hard Drive", 150.00, 7),
        ("Printer", 200.00, 3),
        ("Speakers", 80.00, 9)
    ]
    try:
        cursor = conn.cursor()
        for product in products:
            cursor.execute("""  
                INSERT INTO products (name, price, quantity)  
                VALUES (%s, %s, %s)  
            """, product)
        conn.commit()
        print("10 тестовых продуктов успешно добавлены.")
    except psycopg2.Error as e:
        print(f"Ошибка при добавлении продуктов: {e}")


def get_products_below_quantity(conn, quantity=10):
    """Возвращает список продуктов, у которых количество меньше заданного."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            SELECT * FROM products WHERE quantity < %s  
        """, (quantity,))
        products = cursor.fetchall()
        return products
    except psycopg2.Error as e:
        print(f"Ошибка при получении списка продуктов: {e}")
        return None


def update_product_price(conn, product_name, new_price):
    """Обновляет цену продукта по его имени."""
    try:
        cursor = conn.cursor()
        cursor.execute("""  
            UPDATE products SET price = %s WHERE name = %s  
        """, (new_price, product_name))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Цена продукта '{product_name}' успешно обновлена до {new_price}.")
        else:
            print(f"Продукт с именем '{product_name}' не найден.")
    except psycopg2.Error as e:
        print(f"Ошибка при обновлении цены продукта: {e}")


def main():
    """Основная логика скрипта."""
    conn = connect_to_db()
    if conn is None:
        return

    create_table(conn)
    insert_products(conn)

    # Получение списка продуктов с количеством меньше 10
    products_below_10 = get_products_below_quantity(conn, quantity=10)
    print("\nПродукты с количеством меньше 10:")
    if products_below_10:
        for product in products_below_10:
            print(product)
    else:
        print("Нет продуктов с количеством меньше 10.")

    # Обновление цены продукта
    product_name = "Laptop"
    new_price = 1300.00
    update_product_price(conn, product_name, new_price)

    conn.close()


if __name__ == "__main__":
    main()