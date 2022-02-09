import sys


def sales_bakary(num_1=None, num_2=None):
    """Вывод определенного количества сумм"""
    sales = {
        line.split()[0]: line.split()[1]
        for line in open('bakery_2.csv', 'r', encoding='utf-8')
    }

    if len(sales) <= num_2:
        num_2 = len(sales)
    if num_1 is None:
        for sale in sales.values():
            print(sale.strip())
    elif num_2 is None:
        for _ in range(num_1, len(sales) + 1):
            print(sales[str(_)])
    else:
        for _ in range(num_1, num_2):
            print(_)
            print(sales[str(_)])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sales_bakary(int(sys.argv[-1]))
    elif len(sys.argv) == 3:
        sales_bakary(int(sys.argv[1]), int(sys.argv[-1]))
    else:
        sales_bakary()
