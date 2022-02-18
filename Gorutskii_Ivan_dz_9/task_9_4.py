class Car:
    """Описание машины"""

    is_police: bool = False
    __directions = ('направо', 'налево', 'прямо', 'назад',)

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        """Увеличивает значение скорости на 15"""
        self.speed += 15
        return f'Машина {self.name} повысила скорость на 15: {self.speed}'

    def stop(self) -> None:
        """При вызове метода скорость становится равной '0'"""
        self.speed = 0
        return f'Машина {self.name} остановилась'

    def turn(self, direction: str) -> None:
        """Принимает направление движения автомобиля"""
        direction = direction.lower()
        if direction in self.__directions:
            return f'{self.name} движется {direction}'
        else:
            raise ValueError('нераспознанное направление движения')

    def show_speed(self) -> None:
        """Проверка текущей скорости автомобиля"""
        if isinstance(self, PoliceCar):
            self.is_police = True
        else:
            self.is_police = False

        if self.is_police:
            return f'{self.name}: текущая скорость {self.speed}\n'\
                'Вруби мигалку и забудь про скорость!'
        else:
            return f'{self.name}: текущая скорость {self.speed}'


class TownCar(Car):
    """Описание городского автомобиля"""

    def show_speed(self) -> None:
        """Проверка текущей скорости автомобиля"""
        if self.speed < 60:
            return super().show_speed()
        else:
            return 'Alarm!!! Speed!!!'


class SportCar(Car):
    """Описание городского автомобиля"""


class WorkCar(Car):
    """Описание городского автомобиля"""

    def show_speed(self) -> None:
        """Проверка текущей скорости автомобиля"""
        if self.speed < 40:
            return super().show_speed()
        else:
            return 'Alarm!!! Speed!!!'


class PoliceCar(Car):
    """Описание городского автомобиля"""


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    print(town_car.go())
    print(town_car.show_speed())
    print(work_car.show_speed())
    print(town_car.stop())
    print(police_car.show_speed())
    print(sport_car.turn('назад'))
    print(sport_car.turn('right'))

"""
Не стал делать вывод на экран в классе, на сколько помню, вы Анотолий говорили
что print нужно делать лучше не из функций или класса
 """
