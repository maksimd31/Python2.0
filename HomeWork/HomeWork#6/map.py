# map - Python map() — это встроенная функция, которая позволяет обрабатывать и преобразовывать все элементы в итерируемом объекте без использования явного цикла for, методом, широко известным как сопоставление (mapping). map() полезен, когда вам нужно применить функцию преобразования к каждому элементу в коллекции или в массиве и преобразовать их в новый массив.

# список
# встроенные функции
# abs - меняет - на + и на оборот 
# map - может заменить for

# a = [-1, 2, -3, 4, 5]
# print(list(map(abs, a)))
#
#
# def f(x):
#     return x ** 2
#
#
# a = [1, 2, 3, 5, 6, 7, 8, 9, 0]
# print(list(map(f, a)))
#
# a = [1, 2, 3, 4, 5, 67, 8, 9, 9]
# vv = []
#
#
# def ff(x):
#     return x ** 2
#
#
# for x in a:
#     vv.append(ff(x))
#
# print(vv)
#
# # #вариант через map
# vv = list(map(ff, a))
# print(vv)

# with open('27.txt', 'r', encoding='utf-8') as f:
#     n = int(f.readline())
#     for i in range(n):
#         a, b = map(int, f.readline().split())
#         print(a, b)

# не работает
# я пытаюсь считать с файла данные цифры вытащить и сложить их
# with open('27.txt') as f:
#     n = int(f.readline())
#     for i in range(n):
#         a, b = map(int, f.readline().split())  # через map преобразовали str в int
#         print(a + b)

with open('27.txt') as f:
    n = int(f.readline())
    nums = (f.readline().split())
    for i in range(n):
        a, b = map(int, nums) # через map преобразовали str в int
        print(a + b)

# еше варианты с строками
# def upper(string):
#     return string.upper()
#
#
# listt = ['FeeAes', 'eseRese', 'seTREsese', 'seseseEFGESesea']
#
# print(list(map(upper, listt)))
# print([string.upper() for string in listt])
# # print(list(map(lambda string: string.upper(listt))))
# print(list(map(lambda string: string.upper(), listt)))
#
#
# def lowerr(string):
#     return string.lower()
#
#
# print(list(map(lowerr, listt)))
# print([string.lower() for string in listt])
# print(list(map(lambda string: string.lower(), listt)))
#
#
# def stripp(string):
#     return string.strip()
#
#
# print(list(map(stripp, listt)))
# print([string.strip() for string in listt])
# print(list(map(lambda string: string.strip(), listt)))
