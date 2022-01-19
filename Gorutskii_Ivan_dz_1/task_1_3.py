def transform_string(number: int) -> str:
    """Возващает строку вида 'N процентов' с учета склонения по указаному number"""
    if number % 100 // 10 != 1 and number % 10 == 1:
        return f"{number} процент"
    else:
        if number % 100 // 10 != 1 and number in [2, 3, 4]:
            return f"{number} процента"
        else:
            return f"{number} процентов"


for n in range(1, 101):
    print(transform_string(n))