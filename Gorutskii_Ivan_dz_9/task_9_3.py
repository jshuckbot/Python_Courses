class Worker:
    """Класс описания работника"""

    def __init__(self, name: str, surname: str, position: str, income: dict):
        """Инициализация атрибутов для работника"""
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):
    """Класс должности работника"""

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f'{self.name.title()} {self.surname.title()}'

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        return sum(self._Worker__income.values())


if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())
    print(driver.get_full_name(), driver.get_total_income())
    print(scientist.get_full_name(), scientist.get_total_income())
