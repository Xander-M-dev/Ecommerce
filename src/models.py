class Product:
    """
    Класс для представления товара в магазине.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        quantity (int): Количество товара в наличии
    """

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int
    ) -> None:
        """Инициализирует новый объект Product."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""

    category_count = 0  # Количество всех категорий
    product_count = 0  # Количество всех товаров

    def __init__(
            self,
            name: str,
            description: str,
            products: list
    ) -> None:
        """Инициализирует новый объект Category."""
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)
