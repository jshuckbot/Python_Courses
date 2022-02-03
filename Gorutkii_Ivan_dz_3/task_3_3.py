def thesaurus(*args) -> dict:
    """Алгоритм составления словаря как ключ первая буква имени значение имя"""
    dict_out = {name[0]: [] for name in args }
    for item in args:
        for k in dict_out:
            if item[0] == k:
                dict_out[k].append(item)

    return sort_dict(dict_out)

def sort_dict(dict_out: dict) -> dict:
    """Сортирует словарь"""
    sorted_tuple = sorted(dict_out.items(), key=lambda x: x[0])

    return dict(sorted_tuple)

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
