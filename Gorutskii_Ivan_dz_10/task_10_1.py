from typing import List


class Matrix:
    """Описание класса матрицы"""

    def __init__(self, matrix: List[List[int]]):
        """Инициализирует матрицу"""
        self.matrix = matrix
        self.__exception_error()

    def __exception_error(self):
        """Исключение ошибки"""
        len_ = len(self.matrix[0])
        for item in self.matrix:
            if len_ != len(item):
                raise ValueError('fail initialization matrix')

    def __format_matrix(self):
        """Форматируем матрицу к определенному виду"""
        items_list = []
        for item in self.matrix:
            els_list = []
            for el in item:
                els_list.append(el)
            str_ = f"| {' '.join(map(str, els_list))} |\n"
            items_list.append(str_)

        return ''.join(items_list)

    def __str__(self):
        """Перегружаем метод __str__"""
        return self.__format_matrix()

    def __add__(self, other):
        """Перегружаем метод __add__"""
        result = Matrix(
            [list(map(sum, zip(*items))) for items in zip(self.matrix, other.matrix)]
        )
        return result


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(first_matrix + second_matrix)
    # """
    fail_matrix = Matrix([[1, 2], [3, 6, 7], [5, 6]])
    print(fail_matrix)
