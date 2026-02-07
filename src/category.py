"""Модуль с классом Category (Категория товаров)."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list,
    ) -> None:
        """Инициализирует новый объект Category."""
        self.name = name
        self.description = description
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def __str__(self) -> str:
        """Магический метод для строкового представления категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: "Product") -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строки."""
        result_lines = []
        for product in self.__products:
            # Гарантируем, что price - float и форматируем
            price_value = float(product.price)
            price_str = f"{price_value:.1f}"
            line = f"{product.name}, {price_str} руб. Остаток: {product.quantity} шт."
            result_lines.append(line)

        return "\n".join(result_lines)
