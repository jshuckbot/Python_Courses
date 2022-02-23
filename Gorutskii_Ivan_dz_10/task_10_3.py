def entry_class(method):
    """Декоратор на принадлежность к классу"""
    def wrapper(*args):
        for item in args:
            if not isinstance(item, Cell):
                raise TypeError(
                    'действие допустимо только для экземпляров того же класса'
                )
        return method(*args)

    return wrapper


class Cell:

    def __init__(self, cells: int):
        """Инициализация атрибутов"""
        self.cells = cells

    @entry_class
    def __add__(self, other):
        """Перегружаем метод целочисленного деления суммы"""
        return Cell(self.cells + other.cells)

    @entry_class
    def __sub__(self, other):
        """Перегружаем метод разности"""
        if (self.cells - other.cells) <= 0:
            raise ValueError('недопустимая операция')

        return Cell(self.cells - other.cells)

    @entry_class
    def __mul__(self, other):
        """Перегружаем метод произведения"""
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        """Перегружаем метод деления"""
        if isinstance(other, Cell):
            return Cell(self.cells // other.cells)
        else:
            raise TypeError(
                'действие допустимо только для экземпляров того же класса'
            )

    def __floordiv__(self, other):
        """Перегружаем метод целочисленного деления"""
        if isinstance(other, Cell):
            return Cell(self.cells // other.cells)
        else:
            raise TypeError(
                'действие допустимо только для экземпляров того же класса'
            )

    def make_order(self, number: int) -> str:
        """Формируем клетки в ряд в количестве number"""
        cells_str = ''
        cells = self.cells
        num_cell = 1

        while (num_cell <= cells):
            if num_cell == number and cells - num_cell != 0:
                cells_str += '*\n'
                cells -= num_cell
                num_cell = 1
            else:
                cells_str += '*'
                num_cell += 1

        return cells_str


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)
