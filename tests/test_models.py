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


def test_private_products_access() -> None:
    """Тест приватного доступа к списку товаров."""
    product = Product("Товар", "Описание", 100.0, 1)
    category = Category("Категория", "Описание", [product])

    # Проверяем, что нельзя получить доступ к приватному атрибуту
    with pytest.raises(AttributeError):
        _ = category.__products


def test_add_product_method() -> None:
    """Тест метода добавления товара."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар1", "Описание1", 100.0, 2)
    category = Category("Категория", "Описание", [product1])

    # Проверяем начальное состояние
    assert Category.product_count == 1

    # Добавляем новый товар
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    category.add_product(product2)

    # Проверяем, что счетчик увеличился
    assert Category.product_count == 2


def test_products_getter_format() -> None:
    """Тест формата вывода товаров."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    category = Category("Электроника", "Техника", [product])

    result = category.products
    expected = "Телефон, 1000.0 руб. Остаток: 5 шт."

    assert result == expected


def test_new_product_classmethod() -> None:
    """Тест класс-метода создания товара."""
    product_data = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 150000.0,
        "quantity": 3,
    }

    product = Product.new_product(product_data)

    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 150000.0
    assert product.quantity == 3


def test_price_setter_positive() -> None:
    """Тест сеттера цены с положительным значением."""
    product = Product("Товар", "Описание", 100.0, 5)

    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_zero() -> None:
    """Тест сеттера цены с нулевым значением."""
    product = Product("Товар", "Описание", 100.0, 5)

    product.price = 0
    assert product.price == 100.0


def test_price_setter_negative() -> None:
    """Тест сеттера цены с отрицательным значением."""
    product = Product("Товар", "Описание", 100.0, 5)

    # Пытаемся установить отрицательную цену
    product.price = -50.0
    # Цена не должна измениться
    assert product.price == 100.0


def test_private_price_access() -> None:
    """Тест приватного доступа к цене."""
    product = Product("Товар", "Описание", 100.0, 5)

    # Проверяем, что нельзя получить доступ к приватному атрибуту
    with pytest.raises(AttributeError):
        _ = product.__price


def test_multiple_products_in_category() -> None:
    """Тест нескольких товаров в категории."""
    product1 = Product("Товар1", "Описание1", 100.0, 2)
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    product3 = Product("Товар3", "Описание3", 300.0, 4)

    category = Category("Категория", "Описание", [product1, product2])
    category.add_product(product3)

    result = category.products
    assert "Товар1" in result
    assert "Товар2" in result
    assert "Товар3" in result
    assert "100.0 руб." in result
    assert "Остаток: 4 шт." in result


def test_category_count_increment() -> None:
    """Тест увеличения счетчика категорий."""
    Category.category_count = 0
