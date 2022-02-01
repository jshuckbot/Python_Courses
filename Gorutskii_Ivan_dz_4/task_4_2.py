from requests import get, utils


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    responce = get('http://www.cbr.ru/scripts/XML_daily.asp')
    context = responce.text
    inx_code = context.find(code)
    value_ = context[inx_code:].find('</Value>')
    context = context[inx_code:][:value_]
    value_ = context.find('<Value>')
    context = context[value_:]
    value_ = context.find('>') + 1
    if context[value_:] != '':
        result_value = float(context.replace(',', '.')[value_:])
    else:
        return None

    return result_value


print(currency_rates("BYN"))
print(currency_rates("noname"))
