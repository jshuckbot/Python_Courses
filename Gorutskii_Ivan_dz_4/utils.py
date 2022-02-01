from requests import get, utils
import datetime


def currency_rates(code: str) -> tuple:
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

    return result_value, responce.text


def currency_rates_adv(code: str) -> tuple:
    """Узнает дату по курсу"""
    kurs, context = currency_rates(code)
    inx_ = context.find('name=')
    context = context[:inx_]
    inx_ = context.find('Date=')
    context = context[inx_:]
    inx_ = context.find('=') +1
    context = context[inx_:]
    context = context.replace('"', '').strip()
    day_ = int(context[:2])
    month_ = int(context[3:5])
    year_ = int(context[6:10])
    date_value = datetime.date(year_, month_, day_)
    
    return kurs, date_value
