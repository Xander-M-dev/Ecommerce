"""Модуль с миксином для логирования создания объектов."""


class ProductLogMixin:
    """Миксин, который при создании объекта печатает информацию о нём."""

    def __init__(self, *args, **kwargs) -> None:
        """Конструктор миксина. Вызывает родительский __init__, затем печатает лог."""
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект {self.__class__.__name__} с параметрами: {self._get_init_params()}"
        )

    def _get_init_params(self) -> str:
        """Возвращает строку с параметрами, переданными в конструктор."""
        return f"name='{self.name}', price={self.price}, quantity={self.quantity}"
