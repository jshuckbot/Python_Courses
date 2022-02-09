import sys


def prepare_dataset(path_users_file: str, path_hobby_file: str):
    """
    Считывает данные из файлов и возвращает словарь, где:
    ключ — ФИО, значение — данные о хобби (список строковых переменных):
    param path_users_file: путь до файла, содержащий ФИО пользователей,
    разделенных запятой по строке: param path_hobby_file: путь до файла,
    содержащий хобби, разделенные запятой по строке:return:
    Dict(str: Union[List[str]|None])
    """
    users_hobby = 'users_hobby.txt'

    users = (line for line in open(path_users_file, 'r', encoding='utf-8'))
    hobby = (line for line in open(path_hobby_file, 'r', encoding='utf-8'))
    with open(users_hobby, 'a', encoding='utf-8') as fa:
        for user in users:
            user = user.strip()
            fa.write(try_hobby(user, hobby))
        try:
            if next(hobby).strip() != '':
                fa.write('1\n')
        except StopIteration:
            fa.write('')


def try_hobby(user: str, hobby: str) -> str:
    """Обработка исключения StopIteration и заполнение dict"""
    hobby_ = None
    line = ''
    try:
        hobby_ = next(hobby).strip()
    except StopIteration:
        line = f"{user.strip()}: {None}\n"
    if hobby_ is not None:
        line = f"{user.strip()}: {hobby_}\n"

    return line


if __name__ == '__main__':
    prepare_dataset(sys.argv[-2], sys.argv[-1])
