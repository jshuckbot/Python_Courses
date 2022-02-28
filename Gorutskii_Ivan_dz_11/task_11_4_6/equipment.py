class OfficeEquipment:
    """"""
    def __init__(self, name: str, model: str, type_device: str):
        """Инициализация стандартных атрибутов оргтехники"""
        self.name = name
        self.model = model
        self.type_device = type_device


class Printer(OfficeEquipment):
    """Описание принтера"""

    def __init__(self, name: str, model: str, type_device: str,
                 print_color: str, cartridge_resource: int, paper_size: str):
        """Инициализация принтера"""
        super().__init__(name, model, type_device)
        self.print_color = print_color
        self.cartridge_resource = cartridge_resource
        self.paper_size = paper_size


class Scaner(OfficeEquipment):
    """Описание сканера"""

    def __init__(self, name: str, model: str, type_device: str, permission: str, sensor_type: str, color_depth: str):
        """Инициализация сканера"""
        super().__init__(name, model, type_device)
        self.permission = permission
        self.sensor_type = sensor_type
        self.color_depth = color_depth


class Xerox(OfficeEquipment):
    """Описание ксерокса"""

    def __init__(self, name: str, model: str, type_device: str,
                 permission: str, cartridge_resource: int, paper_size: str):
        """Инициализация ксерокса"""
        super().__init__(name, model, type_device)
        self.permission = permission
        self.cartridge_resource = cartridge_resource
        self.paper_size = paper_size
