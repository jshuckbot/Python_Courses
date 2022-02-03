from random import uniform
from sys import getsizeof

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    str_out = ''
    for i in range(len(list_in)):
        money = str(list_in[i])
        rub_ = int(money[:2])
        cop_ = money[3:]
        if cop_ == '0':
            cop_ += '0'
        if len(cop_) < 2:
            cop_ = str(int(cop_) * 10)
        if i + 1 != len(list_in):
            str_out += f"{rub_} руб {cop_} коп, "
        else:
            str_out += f"{rub_} руб {cop_} коп"

    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


# зафиксировал здесь информацию по исходному списку my_list
id_ = id(my_list)
size_ = getsizeof(my_list)
result_2 = sort_prices(my_list)
# зафиксировал здесь доказательство, что результат result_2 остался тем же объектом
if id_ == id(my_list) and size_ == getsizeof(my_list):
    print(f'Адрес = {id_} и размер = {size_} неизменились.')

print(result_2)



def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = []
    count_ = 1
    for max_ in sorted(list_in, reverse=True):
        if count_ <= 5:
            list_out.append(max_)
        count_ += 1

    return sorted(list_out)


result_4 = check_five_max_elements(my_list)
print(result_4)