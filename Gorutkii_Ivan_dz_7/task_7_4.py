import os


def count_size_file(size_file: int, size_file_dict: dict):
    """Алгоритм посчета количества файлов кратных 10"""
    size_low = 0
    size_up = 0

    if size_file == 0:
        size_file_dict.setdefault(0, 0)
        size_file_dict[0] += 1
    while size_file:
        border_low = size_low
        border_up = size_up
        if border_low < size_file and size_file <= border_up:
            size_file_dict.setdefault(border_up, 0)
            size_file_dict[border_up] += 1
            size_file = False
        size_low = size_up
        size_up = 10 if size_up == 0 else size_up * 10


folder = 'my_project/'
size_file_dict = {}

for root, _, files in os.walk(folder):
    for file in files:
        size_file = os.stat(os.path.join(root, file)).st_size
        count_size_file(size_file, size_file_dict)

print(dict(sorted(size_file_dict.items(), key=lambda x: x[0])))
