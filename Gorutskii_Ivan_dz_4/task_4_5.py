def main(argv):
    """Ввод через консоль"""
    kurs, date_value = currency_rates_adv(*argv[1:])
    print(f'{kurs}, {date_value.strftime("%d.%m.%Y")}')

    return 0


if __name__ == '__main__':
    import sys
    import datetime
    from utils import currency_rates_adv

    exit(main(sys.argv))
