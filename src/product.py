"""
Модуль с классом Product (основной товар).
"""

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
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        price_formatted = f"{self.price:.1f}"
        return f"{self.name}, {price_formatted} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(new_price)

    def _get_init_params(self) -> str:
        """Переопределяем метод миксина для более информативного вывода."""
        return f"name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity}"
