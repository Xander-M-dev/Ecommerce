"""Тесты для модуля models."""

import pytest

from src import Category, Product


def test_product_str() -> None:
    """Тест строкового представления товара."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    assert str(product) == "Телефон, 1000.0 руб. Остаток: 5 шт."


def test_category_str() -> None:
    """Тест строкового представления категории."""
    product1 = Product("Товар1", "Описание1", 100.0, 2)
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    category = Category("Электроника", "Техника", [product1, product2])
    assert str(category) == "Электроника, количество продуктов: 5 шт."


def test_product_addition() -> None:
    """Тест сложения товаров."""
    product1 = Product("Товар1", "Описание1", 100.0, 10)
    product2 = Product("Товар2", "Описание2", 200.0, 2)
    result = product1 + product2
    assert result == 1400.0


def test_product_addition_different_objects() -> None:
    """Тест сложения товаров с разными количествами."""
    product1 = Product("Товар1", "Описание1", 50.0, 4)
    product2 = Product("Товар2", "Описание2", 75.0, 3)
    result = product1 + product2
    assert result == 425.0


def test_product_addition_with_wrong_type() -> None:
    """Тест сложения товара с объектом другого типа."""
    product = Product("Товар", "Описание", 100.0, 5)
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса Product"
    ):
        _ = product + 100


def test_empty_category_str() -> None:
    """Тест строкового представления пустой категории."""
    category = Category("Пустая категория", "Нет товаров", [])
    assert str(category) == "Пустая категория, количество продуктов: 0 шт."


def test_category_str_large_quantity() -> None:
    """Тест категории с большим количеством товаров."""
    products = [Product(f"Товар{i}", f"Описание{i}", 100.0 * i, i) for i in range(1, 6)]
    category = Category("Большая категория", "Много товаров", products)
    assert str(category) == "Большая категория, количество продуктов: 15 шт."


def test_products_getter_uses_str() -> None:
    """Тест, что геттер products использует __str__ товаров."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    category = Category("Электроника", "Техника", [product])
    assert category.products == str(product)


def test_product_str_with_zero_quantity() -> None:
    """Тест строкового представления товара с нулевым количеством."""
    product = Product("Товар", "Описание", 100.0, 0)
    assert str(product) == "Товар, 100.0 руб. Остаток: 0 шт."


def test_product_str_price_format() -> None:
    """Тест формата цены в строковом представлении."""
    product = Product("Товар", "Описание", 99.99, 1)
    result = str(product)
    # Цена 99.99 округляется до одного знака после запятой = 100.0
    assert "100.0" in result


def test_private_products_access() -> None:
    """Тест приватного доступа к списку товаров."""
    product = Product("Товар", "Описание", 100.0, 1)
    category = Category("Категория", "Описание", [product])
    with pytest.raises(AttributeError):
        _ = category.__products


def test_add_product_method() -> None:
    """Тест метода добавления товара."""
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("Товар1", "Описание1", 100.0, 2)
    category = Category("Категория", "Описание", [product1])
    assert Category.product_count == 1
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    category.add_product(product2)
    assert Category.product_count == 2


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
    product.price = -50.0
    assert product.price == 100.0


def test_private_price_access() -> None:
    """Тест приватного доступа к цене."""
    product = Product("Товар", "Описание", 100.0, 5)
    with pytest.raises(AttributeError):
        _ = product.__price


if __name__ == "__main__":
    pytest.main(["-v"])
