from storage import Storage
import fill_object

supplies = []

storage_1 = Storage()

while True:
    object = input('Выбирете пункт какого класса вы хотите внести оборудование?\n'
                   '1) - принтер\n'
                   '2) - сканер\n'
                   '3) - ксерокс\n'
                   'q) - для выхода\n'
                   )
    if object == 'q':
        break
    object = fill_object.define_class_object(object)
    if object:
        supplies.append(object)
    else:
        print('Вы ввели некорректно данные. Повторите попытку\n')

storage_1.acceptance_of_equipment(supplies)
# storage_1.transfer_to_division('сканеры', 1)
storage_1.inventory_objects()
