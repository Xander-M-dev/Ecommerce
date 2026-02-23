"""Модуль с тестами для классов интернет-магазина."""

import pytest
from src import (
    BaseProduct, Product, Category, Smartphone, LawnGrass,
    ProductLogMixin
)
from abc import ABC


def test_smartphone_creation() -> None:
    """Тест создания объекта Smartphone."""
    phone = Smartphone(
        name="Samsung S23",
        description="Смартфон",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )
    assert phone.name == "Samsung S23"
    assert phone.description == "Смартфон"
    assert phone.price == 180000.0
    assert phone.quantity == 5
    assert phone.efficiency == 95.5
    assert phone.model == "S23 Ultra"
    assert phone.memory == 256
    assert phone.color == "Серый"


def test_lawn_grass_creation() -> None:
    """Тест создания объекта LawnGrass."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_addition_same_class_smartphone() -> None:
    """Проверка сложения двух объектов Smartphone."""
    phone1 = Smartphone("P1", "", 100.0, 2, 90.0, "M1", 128, "Red")
    phone2 = Smartphone("P2", "", 200.0, 3, 85.0, "M2", 256, "Blue")
    result = phone1 + phone2
    expected = 100 * 2 + 200 * 3  # 200 + 600 = 800
    assert result == expected


def test_addition_same_class_grass() -> None:
    """Проверка сложения двух объектов LawnGrass."""
    grass1 = LawnGrass("G1", "", 50.0, 5, "RU", "7 дней", "Green")
    grass2 = LawnGrass("G2", "", 60.0, 3, "USA", "5 дней", "DarkGreen")
    result = grass1 + grass2
    expected = 50 * 5 + 60 * 3  # 250 + 180 = 430
    assert result == expected


def test_addition_different_classes() -> None:
    """Проверка сложения объектов разных классов."""
    phone = Smartphone("P", "", 100.0, 2, 90.0, "M", 128, "Red")
    grass = LawnGrass("G", "", 50.0, 5, "RU", "7 дней", "Green")
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = phone + grass


# def test_add_product_with_wrong_type() -> None:
# """Проверка метода add_product: при попытке добавить объект не-Product
# должна выбрасываться ошибка TypeError.
# """
# category = Category("Test", "Desc", [])
# with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
# category.add_product("не продукт")


def test_add_product_smartphone_to_category() -> None:
    """Проверка добавления смартфона в категорию."""
    Category.category_count = 0
    Category.product_count = 0
    phone = Smartphone("P", "", 100.0, 2, 90.0, "M", 128, "Red")
    category = Category("Test", "Desc", [])
    category.add_product(phone)
    assert Category.product_count == 1
    assert phone.name in category.products


def test_add_product_grass_to_category() -> None:
    """Проверка добавления газонной травы в категорию."""
    Category.category_count = 0
    Category.product_count = 0
    grass = LawnGrass("G", "", 50.0, 5, "RU", "7 дней", "Green")
    category = Category("Test", "Desc", [])
    category.add_product(grass)
    assert Category.product_count == 1
    assert grass.name in category.products


def test_product_creation() -> None:
    """Тест создания обычного товара (Product)."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_category_creation() -> None:
    """Тест создания категории."""
    p1 = Product("Товар1", "Описание1", 100.0, 2)
    p2 = Product("Товар2", "Описание2", 200.0, 3)
    category = Category("Электроника", "Техника", [p1, p2])
    assert category.name == "Электроника"
    assert category.description == "Техника"


# def test_private_products_access() -> None:
# """Проверка приватности атрибута __products."""
# product = Product("Товар", "Описание", 100.0, 1)
# category = Category("Категория", "Описание", [product])
# with pytest.raises(AttributeError):
# _ = category.__products


def test_add_product_method() -> None:
    """Проверка метода add_product для обычного продукта."""
    Category.category_count = 0
    Category.product_count = 0
    p1 = Product("Товар1", "Описание1", 100.0, 2)
    category = Category("Категория", "Описание", [p1])
    assert Category.product_count == 1
    p2 = Product("Товар2", "Описание2", 200.0, 3)
    category.add_product(p2)
    assert Category.product_count == 2


def test_products_getter_format() -> None:
    """Проверка формата геттера products."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    category = Category("Электроника", "Техника", [product])
    result = category.products
    expected = "Телефон, 1000.0 руб. Остаток: 5 шт."
    assert result == expected


def test_new_product_classmethod() -> None:
    """Тест класс-метода new_product."""
    data = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 150000.0,
        "quantity": 3
    }
    product = Product.new_product(data)
    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 150000.0
    assert product.quantity == 3


def test_price_setter_positive() -> None:
    """Проверка установки положительной цены."""
    product = Product("Товар", "Описание", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_zero() -> None:
    """Проверка установки нулевой цены."""
    product = Product("Товар", "Описание", 100.0, 5)
    product.price = 0
    assert product.price == 100.0


def test_price_setter_negative() -> None:
    """Проверка установки отрицательной цены."""
    product = Product("Товар", "Описание", 100.0, 5)
    product.price = -50.0
    assert product.price == 100.0


# def test_private_price_access() -> None:
# """Проверка приватности атрибута __price."""
# product = Product("Товар", "Описание", 100.0, 5)
# with pytest.raises(AttributeError):
# _ = product.__price


def test_product_str() -> None:
    """Проверка строкового представления товара."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    assert str(product) == "Телефон, 1000.0 руб. Остаток: 5 шт."


def test_category_str() -> None:
    """Проверка строкового представления категории."""
    p1 = Product("Товар1", "Описание1", 100.0, 2)
    p2 = Product("Товар2", "Описание2", 200.0, 3)
    category = Category("Электроника", "Техника", [p1, p2])
    assert str(category) == "Электроника, количество продуктов: 5 шт."


def test_product_addition_product() -> None:
    """Проверка сложения двух обычных продуктов."""
    p1 = Product("P1", "", 100.0, 10)
    p2 = Product("P2", "", 200.0, 2)
    assert p1 + p2 == 100 * 10 + 200 * 2


def test_empty_category_str() -> None:
    """Строковое представление пустой категории."""
    category = Category("Пустая", "Нет товаров", [])
    assert str(category) == "Пустая, количество продуктов: 0 шт."


def test_category_str_large_quantity() -> None:
    """Категория с несколькими продуктами."""
    products = [Product(f"Товар{i}", "", 100.0 * i, i) for i in range(1, 6)]
    category = Category("Большая", "Много", products)
    assert str(category) == "Большая, количество продуктов: 15 шт."


def test_products_getter_uses_str() -> None:
    """Геттер products использует __str__ продукта."""
    product = Product("Телефон", "Смартфон", 1000.0, 5)
    category = Category("Электроника", "Техника", [product])
    assert category.products == str(product)


def test_product_str_with_zero_quantity() -> None:
    """Товар с нулевым количеством."""
    product = Product("Товар", "Описание", 100.0, 0)
    assert str(product) == "Товар, 100.0 руб. Остаток: 0 шт."


def test_product_str_price_format() -> None:
    """Проверка форматирования цены (округляется до одного знака)."""
    product = Product("Товар", "Описание", 99.99, 1)
    assert "100.0" in str(product)


def test_category_count_increment() -> None:
    """Проверка увеличения счётчика категорий."""
    Category.category_count = 0
    Category.product_count = 0
    _ = Category("Кат1", "Описание", [])
    assert Category.category_count == 1
    _ = Category("Кат2", "Описание", [])
    assert Category.category_count == 2


def test_counters() -> None:
    """Проверка счётчиков категорий и товаров."""
    Category.category_count = 0
    Category.product_count = 0
    p1 = Product("Т1", "Д1", 10.0, 1)
    p2 = Product("Т2", "Д2", 20.0, 2)
    _ = Category("Кат1", "Описание", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2
    p3 = Product("Т3", "Д3", 30.0, 3)
    _ = Category("Кат2", "Описание", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_base_product_is_abstract() -> None:
    """Проверка, что BaseProduct является абстрактным классом."""
    assert issubclass(BaseProduct, ABC)
    with pytest.raises(TypeError):
        _ = BaseProduct()


def test_product_inherits_from_base_and_mixin() -> None:
    """Проверка, что Product наследует от BaseProduct и содержит миксин."""
    assert issubclass(Product, BaseProduct)
    assert issubclass(Product, ProductLogMixin)


def test_mixin_logging_on_creation(capsys) -> None:
    """Проверка, что при создании продукта печатается лог."""
    product = Product("Тест", "Описание", 100.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
    assert "name='Тест'" in captured.out
    assert "price=100.0" in captured.out


def test_smartphone_logging(capsys) -> None:
    """Проверка логирования для смартфона."""
    phone = Smartphone(
        "Samsung", "Описание", 200.0, 3,
        95.0, "S23", 256, "Black"
    )
    captured = capsys.readouterr()
    assert "Создан объект Smartphone с параметрами:" in captured.out


def test_lawn_grass_logging(capsys) -> None:
    """Проверка логирования для травы."""
    grass = LawnGrass(
        "Grass", "Описание", 50.0, 10,
        "Россия", "7 дней", "Зелёный"
    )
    captured = capsys.readouterr()
    assert "Создан объект LawnGrass с параметрами:" in captured.out


def test_base_product_has_abstract_methods() -> None:
    """Проверка наличия абстрактных методов в BaseProduct."""
    abstract_methods = BaseProduct.__abstractmethods__
    assert 'price' in abstract_methods
    assert '__str__' in abstract_methods
    assert '__add__' in abstract_methods


if __name__ == "__main__":
    pytest.main(["-v"])
