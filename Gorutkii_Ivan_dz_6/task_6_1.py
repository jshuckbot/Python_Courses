from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсии IP адрес спамера и количество отправленных им запросов
    по данным файт строку на атрибуты и возвращает кортеж атрибутов
    (<remote_addr>, <request_type>, <requested_resource>)"""
    out_ = line.split()
    ip_ = out_[0]
    request_ = out_[5].replace('"', '')
    path_ = out_[6]

    return ip_, request_, path_


list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    list_in = fr.readlines()

for line in list_in:
    list_out.append(get_parse_attrs(line))

pprint(list_out)

"""
Сделал профилирование с readline и readlines()
время показало разницу очень незначительную в сторону readlines(). взял его.
я так думаю если будет большой объем информации то нужно наш текстовый объект
помещать в генератор и вытягивать по одной строчке когда нужно будет.
Тем самым мы освободим ОЗУ от лишних затрат
"""
