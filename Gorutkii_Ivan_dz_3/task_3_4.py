def thesaurus(*args) -> dict:
    """Алгоритм составления словаря как ключ первая буква фамилии и имени значение имя"""
    dict_out = {
        l_name.split()[1][0]: {
            name.split()[0][0]: [] for name in args
            if l_name.split()[1][0] == name.split()[1][0]
            }
        for l_name in args
        }
    # print(dict_out)
    for full_name in args:
        full_name = full_name.split()
        fill_dict_list(full_name, dict_out)

    return(sort_dict(dict_out))

def fill_dict_list(full_name: list, dict_out: dict):
    """Заполняет  списками словаря"""
    for l_name in dict_out:
        if l_name == full_name[1][0]:
            for name in dict_out[l_name]:
                if name == full_name[0][0]:
                    dict_out[l_name][name].append(' '.join(full_name))


def sort_dict(dict_out: dict) -> dict:
    """Сортирует словарь"""
    sorted_tuple = sorted(dict_out.items(), key=lambda x: x[0])

    return dict(sorted_tuple)


print("Иван Сергеев", "Инна Серова", "Петр Алексеев",
    "Илья Иванов", "Анна Савельева")
print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев",
    "Илья Иванов", "Анна Савельева"))
