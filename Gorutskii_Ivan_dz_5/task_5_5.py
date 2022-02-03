def get_uniq_numbers(src: list) -> list:
    """
    Находит значения из списка и сохраняем в новый сохраняя оригинальную последовательность
    """
    uniq_set_numbers = set()
    tmp = set()
    for number in src:
        if number not in tmp:
            uniq_set_numbers.add(number)
        else:
            uniq_set_numbers.discard(number)

        tmp.add(number)

    return [nbr for nbr in src if nbr in uniq_set_numbers]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
