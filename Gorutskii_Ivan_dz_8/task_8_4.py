from functools import wraps


def val_checker(val_func):
    def _val_cheker(func):
        @wraps(func)
        def wrapper(*args):
            for item in args:
                if not val_func(item):
                    raise ValueError(f'wrong {item}')

            return func(*args)

        return wrapper

    return _val_cheker


def test_func(x):
    """ алгортм проверки числА >= 0"""
    if isinstance(x, int) and x >= 0:
        return True

    return False


@val_checker(test_func)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
