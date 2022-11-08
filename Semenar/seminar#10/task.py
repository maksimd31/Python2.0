import datetime


def my_func(x, y):
    print(f'{x = }')
    print(f'{y = }')
    return x * y


# my_func(5, 3)


def my_func2(x, y, *args):
    print(f'{x = }')
    print(f'{y = }')
    other = args
    print(f'{other = }')


# my_func2(5, 4, 15, 35, 12)

def my_func3(x, y, *, a, b, c):
    print(f'{x = }')
    print(f'{y = }')
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')

# f = '15'
# my_func3(5, f, b=4, c=f, a=10)


def my_func4(*args, **kwargs):
    a, b, *c = args
    d = kwargs
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')
    print(f'{d = }')


my_func4(1, 2, 3, 4, 5, z=12, x=15, v=14)