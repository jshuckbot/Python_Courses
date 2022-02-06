def get_parse_attrs(line: str, spam_ip: set):
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>,
     <request_type>, <requested_resource>)"""
    out_ = line.split()
    ip_ = out_[0]
    if ip_ not in spam_ip:
        spam_ip[ip_] = 1
    else:
        spam_ip[ip_] += 1


list_out = list()
spam_ip = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    genenerator = (line.strip() for line in fr)
    for line in genenerator:
        get_parse_attrs(line, spam_ip)

print(max(spam_ip), str(max(spam_ip.values())))
