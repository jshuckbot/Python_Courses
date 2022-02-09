import sys


def edit_bakery(num_line: int, value: str):
    """Помещаем каждую строку в словарь"""
    save_lines = {}
    with open('bakery.csv', 'r', encoding='utf-8') as fw:
        num = 1
        line = fw.readline().strip()
        while line:
            save_lines.setdefault(num, line)
            line = fw.readline().strip()
            num += 1
        if num >= num_line:
            save_lines[num_line] = value
            save_bakery(save_lines)
        else:
            print('Номера строки со значениями не существует')


def save_bakery(save_lines: dict):
    """Сохранение в файл измененного значения"""
    with open('bakery.csv', 'w', encoding='utf-8') as fw:
        for value in save_lines.values():
            fw.write(f'{value}\n')


if __name__ == '__main__':
    edit_bakery(int(sys.argv[-2]), sys.argv[-1])
