# декоратор с замыканием
from datetime import datetime
import logging
from functools import wraps


# не довел до ума логгер
def logger(func):
    def wrapper(*args, **kwargs):
        # logging.basicConfig(
        #     level=logging.INFO, filename='log.log',
        #     format='[%(l1)s] [%(decorator)s]',
        #     datefmt='%d.%m.%Y %H:%M:%S', encoding='utf-8')
        logging.basicConfig(filename='log.log', level=logging.DEBUG)
        start = datetime.now()
        result = func(*args, **kwargs)
        timer = datetime.now() - start
        logging.debug(f'params: {args} timer: {timer}')
        # logging.info(f'params: {args} timer: {timer}')
        return result
    return wrapper


def decorator(funk):
    @wraps(funk)  # вывод времени работы функции
    def wrapper(*args, **kwargs):
        stat = datetime.now()
        result = funk(*args, **kwargs)
        print(datetime.now() - stat)  # получаем разницу между началом и концом
        return result

    return wrapper


# def decorator(func):
#     def inner(*args, **kwargs):
#         print('Старт')
#         func(*args, **kwargs)
#         print('Стоп')
#
#     return inner

@logger
# @decorator
def seq(n):
    # stat = datetime.now()
    # result = 0
    lst = []
    for i in range(n):
        result = (1 + i) ** i
        lst.append(result)
    # print(datetime.now() - stat)  # получаем разницу между началом и концом
    return lst


# print(seq(5)
# у меня стоит лимит на 4300
# ValueError: Exceeds the limit (4300) for integer string conversion
l1 = seq(10)  # Запускает максимум  1000
print(l1)
# 5seq = decorator(seq)
#
# seq(6)
