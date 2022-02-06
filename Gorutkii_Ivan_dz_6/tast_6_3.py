import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
    ключ — ФИО, значение — данные о хобби (список строковых переменных):
    param path_users_file: путь до файла, содержащий ФИО пользователей,
    разделенных запятой по строке: param path_hobby_file: путь до файла,
    содержащий хобби, разделенные запятой по строке:return:
    Dict(str: Union[List[str]|None])
    """
    # Ваш код пишите здесь

    return  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
