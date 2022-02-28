from date_const import DATE


class Date:
    __date_dict = {}

    def __init__(self, date: str):
        """Инициализация даты"""
        self.date = date

    @classmethod
    def extract_date_(cls, date: str) -> dict:
        """Извлекаем дату в виде чисел и помещаем ее в словарь класса"""
        cls.__date_dict.setdefault('day', int(date[:2]))
        cls.__date_dict.setdefault('mounth', int(date[3:5]))
        cls.__date_dict.setdefault('year', int(date[6:]))

        return Date.validation_date(cls.__date_dict)

    @staticmethod
    def validation_date(date_dict: dict):
        """Валидация полученной даты"""
        day = date_dict['day']
        mounth = date_dict['mounth']
        year = date_dict['year']
        correct_date = False

        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and year > 0:
            if mounth in DATE and day > 0 and day <= DATE[mounth]:
                correct_date = True
            elif mounth == 2 and day > 0 and day <= DATE[mounth] + 1:
                correct_date = True
            else:
                raise ValueError('Дата введена с ошибками')
        elif mounth in DATE and day > 0 and day <= DATE[mounth] and year > 0:
            correct_date = True

        if correct_date:
            return 'Дата введена корректно'
        else:
            raise ValueError('Дата введена с ошибками')

    def proccessing_date_validation(self):
        """Получаем дату для обработки и производим валидацию"""
        return self.extract_date_(self.date)


if __name__ == '__main__':
    d = Date('29-02-2001')
    print(d.proccessing_date_validation())
