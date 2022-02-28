class NumberListError(Exception):
    """Исключение если в списке не число"""

    _default_messege = 'В список пытаетесь добавить элемент не относящийся к числу'

    def __init__(self, text=None):
        """Инициализация сообщения об ошибке  от пользователя"""
        if text:
            self._default_messege = text

    def __str__(self):
        """Перегрузка метода str"""
        return f'Исключение {NumberListError.__name__}: {self._default_messege}!!'


class ListNumber(list):
    """Класс список состоящий только из чисел"""

    def append(self, item: str):
        """Добавление числа в список"""
        if not item.isdigit():
            raise NumberListError()
        super().append(int(item))


array = ListNumber()

while True:
    el = input()
    if el == 'q':
        break
    try:
        array.append(el)
    except NumberListError as err:
        print(err)

print(array)
