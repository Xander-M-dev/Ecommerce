"""Тесты для модуля models."""

import pytest

from src.models import Category, Product


def test_product_creation() -> None:
    """Тест создания товара."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_category_creation() -> None:
    """Тест создания категории."""
    product1 = Product("Товар1", "Описание1", 100.0, 2)
    product2 = Product("Товар2", "Описание2", 200.0, 3)

    category = Category("Электроника", "Техника", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2


def test_counters() -> None:
    """Тест счетчиков категорий и товаров."""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем категорию с 2 товарами
    product1 = Product("Т1", "Д1", 10.0, 1)
    product2 = Product("Т2", "Д2", 20.0, 2)
    _ = Category("Кат1", "Оп1", [product1, product2])  # Используем _

    assert Category.category_count == 1
    assert Category.product_count == 2

    # Создаем вторую категорию с 1 товаром
    product3 = Product("Т3", "Д3", 30.0, 3)
    _ = Category("Кат2", "Оп2", [product3])  # Используем _

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_product_types() -> None:
    """Тест типов данных товара."""
    product = Product("Test", "Desc", 99.99, 10)

    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)


def test_empty_category() -> None:
    """Тест создания пустой категории."""
    Category.category_count = 0
    Category.product_count = 0

    _ = Category("Пустая", "Описание", [])  # Используем _

    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_with_single_product() -> None:
    """Тест категории с одним товаром."""
    Category.category_count = 0
    Category.product_count = 0

    product = Product("Один товар", "Только один", 50.0, 1)
    category = Category("Одиночная", "Категория с одним товаром", [product])

    assert category.name == "Одиночная"
    assert len(category.products) == 1
    assert category.products[0].name == "Один товар"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_multiple_categories() -> None:
    """Тест нескольких категорий с товарами."""
    Category.category_count = 0
    Category.product_count = 0

    # Первая категория
    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    cat1 = Category("Cat1", "Desc1", [p1, p2])

    # Вторая категория
    p3 = Product("P3", "D3", 30.0, 3)
    cat2 = Category("Cat2", "Desc2", [p3])

    # Проверяем счетчики
    assert Category.category_count == 2
    assert Category.product_count == 3

    # Проверяем, что категории разные
    assert cat1.name == "Cat1"
    assert cat2.name == "Cat2"
    assert len(cat1.products) == 2
    assert len(cat2.products) == 1


if __name__ == "__main__":
    # Запускаем тесты напрямую, если нужно
    pytest.main(["-v"])
