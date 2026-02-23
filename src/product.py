"""Модуль с классом Product (основной товар)."""

from typing import TYPE_CHECKING

from .base_product import BaseProduct
from .mixins import ProductLogMixin

if TYPE_CHECKING:
    from .category import Category


class Product(ProductLogMixin, BaseProduct):
    """Класс для представления товара в магазине."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализирует объект Product."""
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        price_formatted = f"{self.price:.1f}"
        return f"{self.name}, {price_formatted} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает стоимость всех экземпляров двух товаров, выдаёт TypeError: если классы объектов разные."""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

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
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой на положительность."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(new_price)

    def _get_init_params(self) -> str:
        """Переопределение метода миксина.Возвращает строку с параметрами, переданными в конструктор."""
        return (
            f"name='{self.name}', description='{self.description}', "
            f"price={self.price}, quantity={self.quantity}"
        )
