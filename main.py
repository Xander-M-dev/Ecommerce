"""Основной файл для запуска приложения."""

from src.models import Category, Product


def create_sample_data() -> tuple[list[Product], list[Category]]:
    """Создает тестовые данные."""
    # Создаем товары
    phone = Product("iPhone 15", "Смартфон Apple", 90000.0, 10)
    laptop = Product("MacBook Pro", "Ноутбук Apple", 150000.0, 5)
    tablet = Product("iPad Air", "Планшет Apple", 60000.0, 8)
    tv = Product("Samsung QLED", "Телевизор 4K", 80000.0, 3)

    # Создаем категории
    electronics = Category(
        "Электроника Apple",
        "Техника компании Apple",
        [phone, laptop, tablet],
    )

    tv_category = Category(
        "Телевизоры",
        "Современные телевизоры",
        [tv],
    )

    return [phone, laptop, tablet, tv], [electronics, tv_category]


def display_products(products: list[Product]) -> None:
    """Отображает список товаров."""
    print("\n" + "=" * 50)
    print("СПИСОК ВСЕХ ТОВАРОВ:")
    print("=" * 50)
    for i, product in enumerate(products, 1):
        print(f"{i}. {product.name}")
        print(f"   Описание: {product.description}")
        print(f"   Цена: {product.price:.2f} руб.")
        print(f"   В наличии: {product.quantity} шт.")
        print("-" * 50)


def display_categories(categories: list[Category]) -> None:
    """Отображает список категорий с товарами."""
    print("\n" + "=" * 50)
    print("КАТЕГОРИИ И ТОВАРЫ:")
    print("=" * 50)

    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товаров в категории: {len(category.products)}")
        print("Товары:")

        for product in category.products:
            print(f"  • {product.name} - {product.price:.2f} руб.")


def display_statistics() -> None:
    """Отображает статистику по магазину."""
    print("\n" + "=" * 50)
    print("СТАТИСТИКА МАГАЗИНА:")
    print("=" * 50)
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
    print("=" * 50)


def main() -> None:
    """Основная функция приложения."""
    print("ДОБРО ПОЖАЛОВАТЬ В ИНТЕРНЕТ-МАГАЗИН!")
    print("=" * 50)

    # Создаем тестовые данные
    products, categories = create_sample_data()

    # Отображаем информацию
    display_products(products)
    display_categories(categories)
    display_statistics()

    print("\nРабота программы завершена успешно!")


if __name__ == "__main__":
    main()
