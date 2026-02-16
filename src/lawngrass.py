"""Модуль с классом LawnGrass (Газонная трава)."""

from .product import Product


class LawnGrass(Product):
    """Класс для газонной травы, наследник Product."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ) -> None:
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
