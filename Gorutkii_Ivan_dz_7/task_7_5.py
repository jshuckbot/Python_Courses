import os

size_file_dict = {}  # подсчет количества файлов с кратностью 10
file_ext_dict = {}  # фиксирует расширения определенного размера


def count_size_file_ext(path: str):
    """Алгоритм посчета количества файлов кратных 10 и расширения"""
    size_low = 0
    size_up = 0
    _, ext = os.path.splitext(path)
    size_file = os.stat(path).st_size

    if size_file == 0:
        size_file_dict.setdefault(0, 0)
        file_ext_dict.setdefault(0, [])
        size_file_dict[0] += 1
        if ext not in file_ext_dict[0]:
            file_ext_dict[0].append(ext)

    while size_file:
        border_low = size_low
        border_up = size_up
        # распределяем относительно границ размер и расширение
        if border_low < size_file and size_file <= border_up:
            size_file_dict.setdefault(border_up, 0)
            file_ext_dict.setdefault(border_up, [])
            size_file_dict[border_up] += 1
            if ext not in file_ext_dict[border_up]:
                file_ext_dict[border_up].append(ext)
            size_file = False
        size_low = size_up
        size_up = 10 if size_up == 0 else size_up * 10


def union_count_ext() -> dict:
    """В словаре объединяем коржеж из количества и расширения"""
    union_dict = {}
    for item in size_file_dict:
        union_dict.setdefault(item, (size_file_dict[item], file_ext_dict[item]))

    return dict(sorted(union_dict.items(), key=lambda x: x[0]))


folder = 'my_project/'

for root, _, files in os.walk(folder):  # поиск файлов по дереву
    for file in files:
        path = os.path.join(root, file)
        count_size_file_ext(path)

print(union_count_ext())
