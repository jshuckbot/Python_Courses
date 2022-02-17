from functools import wraps


def type_logger(func):
    """Декоратор логирования позиционных аргументов функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        if len(args) == 1:
            print(f'{name}({str(*args)}: {type(*args)})')
        else:
            for idx in range(len(args)):
                if idx + 1 != len(args):
                    print(
                        f'{name}({str(args[idx])}: {type(args[idx])}), ', end=''
                    )
                else:
                    print(f'{name}({str(args[idx])}: {type(args[idx])})')
        if len(kwargs) == 1:
            print(f'{name}({str(*kwargs.values())}: {type(*kwargs.values())})')
        else:
            idx = 1
            for value in kwargs.values():
                if idx != len(kwargs):
                    print(f'{name}({str(value)}: {type(value)}), ', end='')
                else:
                    print(f'{name}({str(value)}: {type(value)})', end='')
                idx += 1

    return wrapper


@type_logger
def calc_cube(x):
    """Вычисляем куб"""
    return x ** 3


a = calc_cube(12, e=32)
