DICT_VALUE = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four':  'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
    }


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    value = value.lower()

    if value in DICT_VALUE:
        str_out = DICT_VALUE[value]
    else:
        str_out = None

    return str_out


def num_translate_adv(value: str) -> str:
    """алгоритм проверки верхнего  регистра"""
    if value[0] == value[0].upper():
        return num_translate(value).title()
    else:
        return num_translate(value)

print(num_translate_adv('One'))
print(num_translate_adv('five'))
