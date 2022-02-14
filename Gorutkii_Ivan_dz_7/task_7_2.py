import os


def collent_path_file(dirs: list) -> list:
    """Делаем список кортежей без форматирования строки dir, file"""
    path_dirs_files = []
    collent_path = ''
    for i in range(1, len(dirs)):
        if dirs[i].count('.') == 0:
            if dirs[i].count('|') > 1:
                collent_path += dirs[i]
            else:
                collent_path = dirs[i]
        else:
            path_file = format_path_file(collent_path, dirs[i])
            path_dirs_files.append(path_file)

    return path_dirs_files


def format_path_file(path_dir: str, file: str) -> tuple:
    """Форматирование списка кортежей  пути"""
    path_dir = path_dir.replace('|--', '/').strip().replace('|', '')
    file = file.replace('|--', '/').strip().replace('|', '')

    return (path_dir, file)


dirs = [line.replace(' ', '')
        for line in open('config.yaml', 'r', encoding='utf-8')]
dirs = [line.strip() for line in dirs]
root_name = dirs[0][3:]

for dir_, file in collent_path_file(dirs):
    path_dir = os.path.join(root_name, dir_[1:])
    # print(path_dir, file)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    with open(f'{path_dir}{file}', 'a', encoding='utf-8') as f:
        f.write('')
