def fill_list_cube(dataset: list) -> int:
    """Наполнение списка кубами"""
    for i in range(1, 1001):
        dataset.append(i ** 3)


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр делится на нацело на 7"""
    sum_ = 0
    for item_ds in dataset:
        if item_ds % 7 == 0:
            sum_ += item_ds
    
    return sum_


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