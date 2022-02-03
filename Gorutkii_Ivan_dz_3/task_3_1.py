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


print(num_translate('nine'))
print(num_translate("eight"))
