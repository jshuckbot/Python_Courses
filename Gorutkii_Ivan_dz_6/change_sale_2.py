import sys


def edit_bakery(num_line: str, value: str):
    """Помещаем каждую строку в словарь"""
    save_lines = {
        line.split()[0]: line.split()[1]
        for line in open('bakery_2.csv', 'r', encoding='utf-8')
    }
    if len(save_lines) >= int(num_line):
        save_lines[num_line] = value
        save_bakery(save_lines)
    else:
        print('Номера строки со значениями не существует')


def save_bakery(save_lines: dict):
    """Сохранение в файл измененного значения"""
    with open('bakery_2.csv', 'w', encoding='utf-8') as fw:
        for num, value in save_lines.items():
            fw.write(f'{num} {value}\n')


if __name__ == '__main__':
    edit_bakery(sys.argv[-2], sys.argv[-1])
