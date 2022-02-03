def get_numbers(src: list) -> list:
    """Алгоритм проверки значение элемента больше предыдушего"""
    result = [src[el] for el in range(1, len(src))
        if src[el-1] < src[el]]
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
