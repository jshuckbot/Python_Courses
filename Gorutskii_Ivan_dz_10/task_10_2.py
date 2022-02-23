from abc import ABC, abstractmethod


class Clothes(ABC):
    """Базовй класс одежда"""

    @abstractmethod
    def calculate(self):
        """Метод для определения расхода ткани"""
        pass  # тут не производятся никакие действия, просто определили метод


class Coat(Clothes):
    """Класс типа одежды пальто"""

    def __init__(self, size: float):
        """Инициализация атрибутов пальто"""
        self.size = float(size)

    @property
    def calculate(self):
        """Метод для определ расхода ткани"""
        rate_coat = self.size / 6.5 + 0.5

        return float(f'{rate_coat:.2F}')


class Costume(Clothes):
    """Класс типа одежды костюм"""

    def __init__(self, height: float):
        """Инициализация атрибутов пальто"""
        self.height = float(height)

    @property
    def calculate(self):
        """Метод для определ расхода ткани"""
        rate_costume = 2 * self.height + 0.3
        return float(f'{rate_costume:.2F}')


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)
    print(costume.calculate)
