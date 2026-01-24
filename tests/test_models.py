import pytest
from src.models import Product, Category


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест корректной инициализации объекта Product."""
        product = Product("Тестовый товар", "Описание", 1000.0, 10)

        assert product.name == "Тестовый товар"
        assert product.description == "Описание"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_product_attributes_types(self):
        """Тест типов данных атрибутов Product."""
        product = Product("Тест", "Описание", 500.0, 5)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)


class TestCategory:
    """Тесты для класса Category."""

    @pytest.fixture
    def sample_products(self):
        """Фикстура для создания тестовых товаров."""
        return [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3)
        ]

    def test_category_initialization(self, sample_products):
        """Тест корректной инициализации объекта Category."""
        category = Category("Тестовая категория", "Описание категории", sample_products)

        assert category.name == "Тестовая категория"
        assert category.description == "Описание категории"
        assert len(category.products) == 2
        assert category.products[0].name == "Товар 1"

    def test_category_count_increment(self, sample_products):
        """Тест подсчета количества категорий."""
        # Сбрасываем счетчик для чистого теста
        Category.category_count = 0
        Category.product_count = 0

        category1 = Category("Категория 1", "Описание 1", sample_products)
        assert Category.category_count == 1

        category2 = Category("Категория 2", "Описание 2", sample_products)
        assert Category.category_count == 2

    def test_product_count_increment(self, sample_products):
        """Тест подсчета количества товаров."""
        # Сбрасываем счетчик для чистого теста
        Category.category_count = 0
        Category.product_count = 0

        category1 = Category("Категория 1", "Описание 1", sample_products)
        assert Category.product_count == 2

        # Добавляем еще одну категорию с 3 товарами
        more_products = [
            Product("Товар 3", "Описание", 300.0, 1),
            Product("Товар 4", "Описание", 400.0, 2),
            Product("Товар 5", "Описание", 500.0, 3)
        ]
        category2 = Category("Категория 2", "Описание 2", more_products)
        assert Category.product_count == 5

    def test_empty_category(self):
        """Тест создания категории без товаров."""
        Category.category_count = 0
        Category.product_count = 0

        category = Category("Пустая категория", "Описание", [])

        assert Category.category_count == 1
        assert Category.product_count == 0
        assert len(category.products) == 0
