"""Модуль с абстрактным базовым классом BaseProduct, определяет общий интерфейс для всех продуктов."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов, задаёт обязательные методы и свойства для каждого товара."""

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактное свойство: цена товара (геттер)."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный сеттер для цены."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения продуктов."""
        pass
