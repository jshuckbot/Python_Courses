class ComplexNumber:
    """Описание комплексного числа"""

    def __init__(self, x: int = 0, y: int = 0):
        """Инициализация комплексного числа"""
        self.compex = x + y * 1j

    def __add__(self, other):
        """Сложение двух комплексных чисел"""
        return ComplexNumber(self.compex + other.compex)

    def __mul__(self, other):
        """Умножение двух комплексных чисел"""
        return ComplexNumber(self.compex * other.compex)

    def __str__(self):
        """Вывод результата с двумя комплексными числами"""
        return f'Результат работы алгоритма:{self.compex}'


a = ComplexNumber(3, 7)
b = ComplexNumber(2, 8)
print(a + b)
print(a * b)
