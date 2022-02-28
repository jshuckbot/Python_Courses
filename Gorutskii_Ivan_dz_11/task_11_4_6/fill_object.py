from equipment import Printer, Scaner, Xerox

papers_size = ('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6',)


def fill_object_printer() -> object:
    """Наполняем и создаем объект принтер"""
    name = input('Введите название принтера: ')
    model = input('Введите введите модель: ')
    type_device = input('Введите тип устройства: ')
    print_color = input('Введите тип печати: ')
    cartridge_resource = input('Введите на сколько хватает картриджа: ')
    paper_size = input('Введите формат бумаги: ')

    if not(name or model or type_device or print_color or
           cartridge_resource or paper_size):
        return False

    if not cartridge_resource.isdigit() or paper_size not in papers_size:
        return False

    object = Printer(name, model, type_device, print_color,
                     cartridge_resource, paper_size)
    return object


def fill_object_scaner() -> object:
    """Наполняем и создаем объект сканер"""
    name = input('Введите название сканера: ')
    model = input('Введите введите модель: ')
    type_device = input('Введите тип устройства: ')
    permission = input('Введите разрешение сканирования: ')
    sensor_type = input('Введите тип сенсора: ')
    color_depth = input('Введите глубину цвета: ')

    if not(name or model or type_device or permission or
           sensor_type or color_depth):
        return False

    object = Scaner(name, model, type_device, permission,
                    sensor_type, color_depth)
    return object


def fill_object_xerox() -> object:
    """Наполняем и создаем объект ксерокс"""
    name = input('Введите название ксерокса: ')
    model = input('Введите введите модель: ')
    type_device = input('Введите тип устройства: ')
    permission = input('Введите разрешение сканирования: ')
    cartridge_resource = input('Введите на сколько хватает картриджа: ')
    paper_size = input('Введите формат бумаги: ')

    if not(name or model or type_device or permission or
           cartridge_resource or paper_size):
        return False

    if not cartridge_resource.isdigit() or paper_size not in papers_size:
        return False

    object = Xerox(name, model, type_device, permission,
                   cartridge_resource, paper_size)
    return object


def define_class_object(object: str) -> object:
    """Определяем какой класс у оборудования"""
    if object == '1':
        object = fill_object_printer()
        if object:
            return object
        else:
            return False
    elif object == '2':
        return fill_object_scaner()
    elif object == '3':
        object = fill_object_xerox()
        if object:
            return object
        else:
            return False
    else:
        return False
