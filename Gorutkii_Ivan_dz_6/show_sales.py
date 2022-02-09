import sys


def sales_bakary(num_1=None, num_2=None):
    """Вывод определенного количества сумм"""
    sales = (line for line in open('bakery.csv', 'r', encoding='utf-8'))

    if num_1 is None:
        for sale in sales:
            print(sale.strip())
    elif num_2 is None:
        for _ in range(num_1 - 1):
            next(sales)
        for sale in sales:
            print(sale.strip())
    else:
        for _ in range(num_1 - 1):
            next(sales)
        for _ in range(num_1 - 1, num_2):
            try:
                print(next(sales).strip())
            except StopIteration:
                break


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sales_bakary(int(sys.argv[-1]))
    elif len(sys.argv) == 3:
        sales_bakary(int(sys.argv[1]), int(sys.argv[-1]))
    else:
        sales_bakary()
