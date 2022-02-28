import sys


def division_numbers(*args):
    """Функция деления чисел"""
    _, num_1, num_2 = tuple(*args)
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise ZeroError()
    else:
        return num_1 / num_2


class ZeroError(Exception):
    """Класс по обработке исключения деления на ноль"""

    _default_messege: str = 'Ошибка деления на ноль'

    def __init__(self, text: str = None):
        """Инициализация сообщения об ошибке от пользователя"""
        if text:
            self._default_messege = text
        self.text = text

    def __str__(self):
        """Перегрузка метода str"""
        return f'Исключение {ZeroError.__name__}: {self._default_messege}!!'


try:
    a = division_numbers(sys.argv)
except ZeroError as err:
    print(err)
except ValueError:
    print('Ошибка, не корректрый задан тип')
else:
    print(a)
