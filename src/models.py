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
        self.__price = float(price)
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установка цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(new_price)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Классметод для создания товара из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


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
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
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
