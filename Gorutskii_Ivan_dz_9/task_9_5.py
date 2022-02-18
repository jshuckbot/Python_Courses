class Stationery:
    """Описание концелярии"""

    def __init__(self, title: str) -> None:
        """Инициализация атрибутов"""
        self.title = title

    def draw(self) -> None:
        """Метод отрисовки"""
        print('Запуск отрисовки')


# определите классы ниже согласно условий задания
class Pen(Stationery):
    """Описание ручки"""

    def draw(self) -> None:
        """Метод отрисовки"""
        print('Запуск отрисовки')
        print(f'{Pen.__name__}: приступил к отрисовке объкта "{self.title}"')


class Pencil(Stationery):
    """Описание карандаша"""

    def draw(self) -> None:
        """Метод отрисовки"""
        print('Запуск отрисовки')
        print(f'{Pencil.__name__}: приступил к отрисовке объкта "{self.title}"')


class Handle(Stationery):
    """Описание маркера"""

    def draw(self) -> None:
        """Метод отрисовки"""
        print('Запуск отрисовки')
        print(f'{Handle.__name__}: приступил к отрисовке объкта "{self.title}"')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """
