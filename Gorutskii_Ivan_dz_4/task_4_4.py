from utils import currency_rates_adv

kurs, date_value = currency_rates_adv("USD")
kurs, date_value = currency_rates_adv("AUD")
print(f'{kurs}, {date_value.strftime("%d.%m.%Y")}')

"""
jshuck@jshuck ~/D/g/P/Gorutskii_Ivan_dz_4> python task_4_4.py
54.57, 01.02.2022
jshuck@jshuck ~/D/g/P/Gorutskii_Ivan_dz_4>
"""
