"""Модуль с основными классами для интернет-магазина."""


class Product:
    """Класс для представления товара в магазине."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализирует новый объект Product."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса (общие для всех категорий)
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализирует новый объект Category."""
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики при создании категории
        Category.category_count += 1
        Category.product_count += len(products)
