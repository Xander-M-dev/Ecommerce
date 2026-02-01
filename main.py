"""Основной файл для демонстрации работы классов."""

from src.models import Category, Product

if __name__ == "__main__":
    # Создаем товары
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Выводим товары (используется геттер)
    print("Товары в категории:")
    print(category1.products)

    print("\n" + "=" * 50 + "\n")

    # Добавляем новый товар через метод
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("Товары после добавления:")
    print(category1.products)

    # Выводим общее количество товаров
    print(f"\nОбщее количество товаров в магазине: {Category.product_count}")

    print("\n" + "=" * 50 + "\n")

    # Создаем товар через класс-метод
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    print("Созданный через класс-метод товар:")
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    print("\n" + "=" * 50 + "\n")

    # Тестируем сеттер цены
    print("Тестируем изменение цены:")

    new_product.price = 800
    print(f"Новая цена: {new_product.price}")

    # Пытаемся установить отрицательную цену
    print("Пытаемся установить отрицательную цену (-100):")
    new_product.price = -100
    print(f"Цена после попытки: {new_product.price}")

    # Пытаемся установить нулевую цену
    print("Пытаемся установить нулевую цену:")
    new_product.price = 0
    print(f"Цена после попытки: {new_product.price}")

    print("\n" + "=" * 50)
    print("Демонстрация завершена!")
