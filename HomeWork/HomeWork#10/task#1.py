# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]

# Декораторы функций — вызываемые объекты, которые принимают другую функцию в качестве аргумента.
# с использованием замыкания
def my_decorator(*args,**kwargs):
    i = 1
    while i<=n:
        print(i)
        i += 1


@my_decorator
def seq(n):
    b = (1+n)**n
    print(b)

seq(3)

# def seq(n):
#     i = 1
#     while i<=n:
#         print(i)
#         i += 1
# seq(3)
# seq(5)
# seq(10)
# seq(9)
# seq(7)


    