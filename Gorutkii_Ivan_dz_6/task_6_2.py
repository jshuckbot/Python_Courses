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

logs = (line for line in open('nginx_logs.txt', 'r', encoding='utf-8'))
for log in logs:
    list_out.append(get_parse_attrs(log, spam_ip))

print(max(spam_ip), str(max(spam_ip.values())))
