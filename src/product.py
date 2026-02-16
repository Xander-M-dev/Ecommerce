"""Модуль с классом Product (Товар)."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


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
        self.__price = float(price)
        self.quantity = quantity

    def __str__(self) -> str:
        """Магический метод для строкового представления товара."""
        price_formatted = f"{self.price:.1f}"
        return f"{self.name}, {price_formatted} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Нельзя складывать товары разных классов."""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Класс-метод для создания товара из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установки цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(new_price)
