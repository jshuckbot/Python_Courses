def convert_number(items: str) -> bool:
    """Алгоритм проверки строки """
    count = 0
    for item in items:
        if (item == '+' and count % 2 == 0) or\
            (item == '-' and count % 2 == 0) or\
            (item.isdigit() and count % 2 == 1):
            count += 1
            if count == 2:
                return True
        elif item.isdigit():
            return True
        else:
            return False


def format_str(list_in: list) -> str:
    """Форматируюем список в строку"""
    str_ = ''
    opf = True
    for item in list_in:
        if item != '"' and  not item.isdigit() and\
             item[0] != '+' and item[0] != '-':
            str_ += f'{item} '
        elif item.isdigit():
            str_ += f'{item}'
        elif item[0] == '+' or item[0] == '-':
            str_ += f'{item}'
        elif item == '"' and opf:
            opf = False
            str_ += f'{item}'
        elif item == '"' and not opf:
            opf = True
            str_ += f'{item} '

    return(str_)


def convert_list_in_str(list_in: list) -> str:
    """Обосляет каждое целое число кавычками, добавляя кавычку до и после элемента
    списка, являющегося числом, и дополняет нулем до двух целочисленных разрядов.
    Формирует из списка результирующую строковую переменную и возвращает."""
    i = 0
    len_list = len(list_in)
    while i <= len_list:
        item = convert_number(list_in[i])
        if item:
            if list_in[i].isdigit() and len(list_in[i]) < 2:
                list_in[i] = f"0{list_in[i]}"

            if list_in[i][0] == '+' and len(list_in[i]) < 3 or\
                list_in[i][0] == '-' and len(list_in[i]) < 3:
                list_in[i] = f"{list_in[i][0]}0{list_in[i][1]}"

            list_in.insert(i+1, '"')
        i += 1

    i = len(list_in)
    while i >= 0:
        item = convert_number(list_in[i-1])
        if item:
            list_in.insert(i-1, '"')
        i -= 1

    return format_str(list_in)


my_list = ['в', '0', 'часов', '17', 'минут', 'температура',
    'воздуха', 'была', '-52', 'градусов']

 x in L:
    print('at index', L.index(x))
else:
    print(x, 'not found')result = convert_list_in_str(my_list)
print(result)
