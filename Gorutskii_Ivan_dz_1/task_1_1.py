def convert_time(duraction: int) -> str:
    """
    Алгоритм вывода информации о промежутке времени в зависимости
    от его продолжительности
    """
    if duraction < 60:
        sec_ = duraction % 60
        return f"{sec} сек"
    elif duraction < 3600:
        sec_ = duraction % 60
        min_ = duraction // 60
        return f"{min_} мин {sec_} сек"
    elif duraction < 86400:
        sec_ = duraction % 60
        min_ = duraction // 60 % 60
        hour_ = duraction // 3600
        return f"{hour_} час {min_} мин {sec_} сек"
    else:
        sec_ = duraction % 60
        min_ = duraction // 60 % 60
        hour_ = duraction // 3600 % 24
        day_ = duraction // 86400
        return f"{day_} дн {hour_} час {min_} мин {sec_} сек"


duration = 400153
result =convert_time(duration)
print(result)