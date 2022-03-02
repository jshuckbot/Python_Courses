def fill_list_cube(dataset: list) -> int:
    """Наполнение списка кубами"""
    for i in range(1, 1001):
        if i % 2 != 0:
            dataset.append(i ** 3)


def sum_digit_number(number: int) -> int:
    """Алгоритм реализации суммы цифр числа"""
    sum_ = 0
    str_number = str(number)
    for digit in str_number:
        sum_ += int(digit)

    if sum_ % 7 == 0:
        return number
    else:
        return 0


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр делится на нацело на 7"""
    sum_number = 0
    for item_ds in dataset:
        sum_digit = sum_digit_number(item_ds)
        sum_number += sum_digit

    return sum_number


def summ_list_2(dataset: list) -> int:
    """к каждому элементу списка добавляет 17 и высисляет сумму чисел списка,
        сумма цифр которые которых делится нацело на 7"""
    for i in range(len(dataset)):
        dataset[i] += 17

    return sum_list_1(dataset)


my_list = []
fill_list_cube(my_list)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = summ_list_2(my_list)
print(result_2)