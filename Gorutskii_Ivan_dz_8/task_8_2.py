import re


def log_parse(line: str) -> dict:
    """Парсинг файла логов web-сервера"""
    RE_REMOTE_ADDR = re.compile(r'([0-9]{1,3}\.){3}\d{1,3}')
    RE_REQUEST_DATATIME = re.compile(
        r'(\d{1,2}/\w*/\d{4}):(\d{2}:){2}\d{2}.\+\d{4}'
    )
    RE_REQUEST_TYPE = re.compile(r'\w{2,3}[A-Z]')
    RE_REQUEST_RESOURCE = re.compile(r'(\/\w*){2}_\d')
    RE_RESPONCE_CODE = re.compile(r'[^\.\/\+]\d{3}[^:\]]')
    RE_RESPONCE_SIZE = re.compile(r'(?:[^\.\/\+]\d{3}[^:\]]).(?:\d{0,2})')

    try:
        addr = RE_REMOTE_ADDR.match(line).group(0)

    except AttributeError as e:
        return f'Не корректные данные: {e}'
    else:
        datetime = RE_REQUEST_DATATIME.search(line).group(0)
        type = RE_REQUEST_TYPE.search(line).group(0)
        resource = RE_REQUEST_RESOURCE.search(line).group(0)
        code = RE_RESPONCE_CODE.search(line).group(0).strip()
        size = RE_RESPONCE_SIZE.search(line).group(0).split()[-1]

        return addr, datetime, type, resource, code, size


if __name__ == '__main__':
    with open('nginx_logs', 'r', encoding='utf-8') as f:
        context = f.readlines()
        for line in context:
            print(log_parse(line))
