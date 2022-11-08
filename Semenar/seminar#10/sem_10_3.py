def decorator(func):
    def wrapper(*args):
        print('функция wrapper')
        return func(*args)
    return wrapper


@decorator
def my_func(x, y):
    print('функция my_func')
    return x * y


def my_func2(x, y):
    print('функция my_func2')
    return x * y


my_func_res = my_func(5, 4)
print(my_func_res)
print('=' * 45)

# Что происходит:
print('1. Имя функции:')
print(my_func2.__name__)
print('-' * 30)
mf = decorator(my_func2)
print('2. Имя функции:')
print(mf.__name__)
print('_' * 15)
print(mf(5, 4))


# **********************************************************************
print('*' * 70)


# декоратор с параметром:
def constructor(param):
    def decorator2(func):
        def wrapper2(*args):
            print('функция wrapper2')
            print(f'параметр декоратора: {param}')
            return func(*args)
        return wrapper2
    return decorator2


@constructor(0)
def my_func3(x, y):
    print('функция my_func3')
    return x * y


def my_func4(x, y):
    print('функция my_func4')
    return x * y


my_func_res = my_func4(3, 5)
print(my_func4.__name__)
print(my_func_res)
print('=' * 45)
print()

# Что происходит:
c = constructor(0)
mf4 = c(my_func4)
print(mf4(3, 5))

print('\nможно записать так:')
# можно записать так:
mf4 = constructor(0)(my_func4)
print(mf4(3, 5))
