import datetime
import time
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wraps docs
        :param args:
        :param kwargs:
        :return:
        """
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'функция: {func.__name__}\t'
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'результат: {res}\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


def log_func(log_lvl=0):
    def logger2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
            if log_lvl >= 1:
                log_msg += f'функция: {func.__name__}\t'
                if log_lvl == 2:
                    log_msg += f"параметры: {', '.join(map(str, args))}\t"
            res = func(*args, **kwargs)
            log_msg += f'результат: {res}\n'
            with open('log_file.log', 'a', encoding='utf-8') as fp:
                fp.write(log_msg)
            return res

        return wrapper

    return logger2


def html_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        log_msg = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Title</title></head><body>'
        log_msg += f"<p>Комната {' на '.join(map(str, args))}\t"
        log_msg += f'Площадь комнаты: {res} м2</p></body></html>'

        with open('log_file.html', 'w', encoding='utf-8') as fp:
            fp.write(log_msg)
        # print(f'Площадь комнаты: {res} м2')
        return res

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res

    return wrapper


def cacher(func):
    cach = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]

    return wrapper


# @log_func(2)
@cacher
def area_room(x, y):
    """
    Функция возвращает площадь комнаты
    :param x:
    :param y:
    :return:
    """
    return x * y


@timer
def cube(x, y, z):
    return x * y * z


def main():
    print(area_room(5, 4))
    print(area_room(1, 3))
    print(area_room(7, 6))
    print(area_room(5, 4))
    # print(cube(3, 4, 100))
    # print(area_room.__doc__)
    # help(area_room(3, 5))


if __name__ == '__main__':
    main()

# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
#
# seq(3)
# seq(8)
# seq(100)
# seq(8)
# seq(3)
# seq(100)

# def <конструктор декоратора>(<параметры декоратора>):
#
#     def <декоратор>(<декорируемая ф-ция>):
#         def <обёртка>(*args):
#             res = <декорируемая ф-ция>(*args)
#             return res
#         return <обёртка>
#
#     return <декоратор>

# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования
