import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>,
    'domain': <значение за символом @>} | ValueError
    """
    # RE_MAIL = re.compile(r'(?P<username>\w*[^@])@(?P<domain>[^@]\w*\.\w*)')
    RE_MAIL = re.compile(r'(?P<username>\w*)@(?P<domain>\w*\.\w*)')

    assert RE_MAIL.match(email), f'wrong email: {email}'
    print(RE_MAIL.search(email).groupdict())


if __name__ == '__main__':
    # email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
