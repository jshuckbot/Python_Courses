from equipment import Printer, Scaner, Xerox


class Storage:
    """Описание склада"""

    _storage = {}

    def acceptance_of_equipment(self, supplies: list):
        """Прием оргтехники на склад"""
        for supply in supplies:
            if isinstance(supply, Printer):
                self._storage.setdefault('принтеры', [])
                self._storage['принтеры'].append(supply)
            elif isinstance(supply, Scaner):
                self._storage.setdefault('сканеры', [])
                self._storage['сканеры'].append(supply)
            elif isinstance(supply, Xerox):
                self._storage.setdefault('ксероксы', [])
                self._storage['ксероксы'].append(supply)

    def transfer_to_division(self, name_obj: str, number: int):
        """Передача оргтехники в определённое подразделение компании"""
        name_obj = name_obj.lower()
        if name_obj in self._storage and number > 0:
            len_obj = self.numbers_objects(self._storage[name_obj])
            if number <= len_obj:
                for _ in range(number):
                    self._storage[name_obj].pop()
                print(f'Со склада были выданы {name_obj}:\n'
                      f'\tколичество: {number} шт. \n'
                      f'\tостаток: '
                      f'{self.numbers_objects(self._storage[name_obj])} шт.')
            else:
                print(f'Невожможно выдать {name_obj} в количестве: {number} шт. '
                      f'на складе хранится - {len_obj} шт.')
        else:
            print('Некорректно заданы параметры!')

    def numbers_objects(self, objects: list):
        """Подсчет количества оборудования"""
        return len(objects)

    def inventory_objects(self):
        """Показывает состояние склада на текущий момент"""
        for obj, value in self._storage.items():
            print(f'{obj.title()}:')
            for el in self._storage[obj]:
                print(f'\tимя: {el.name} модель: {el.model}')
            print(f'Количество: {self.numbers_objects(self._storage[obj])}')


"""
Я, не стал создавать подразделения, то есть пришлость бы создвать новый класс,
который отвечает за приемку товара в подраздиление и сколько там объектов
на учете. По этому мной было принято решение. Когда объекты отправляют в
подразделения просто минусовать оборудование.
"""
