# n = int(input("Введите натуральное число n "))
# result = ""
# sign = 1
# for i in range(0, n):
#     result += str(3 ** i * sign)
#     result += ", "
#     sign = -sign
# print(result[0:(len(result) - 2)])

# print('----------------------')

# # метод для запроса у пользователя целых чисел с проверкой на целочисленность
# def input_int():
#     try:
#         num = int(input(f"Введите число: "))
#         return int(num) if int(num) > 0 else quit(print('Ошибка. Введите число больше нуля.'))
#     except ValueError:
#         quit(print('Ошибка. Вы ввели не целое число.'))


# # метод для заполнения списка длины N случайными числами от -100 до 100
# def fill_list(input_number):
#     list = []
#     i = 0
#     r = 1
#     # в зависимости от знака введенного числа запускаем цикл либо на увеличение, либо на уменьшение
#     while i < input_number:
#         r *= (-3)
#         list.insert(i, r)
#         i += 1
#     return list


# print(fill_list(input_int()))



# #2wwwwwwwwww
# n = int(input("Введите натуральное число n "))
# result = "1, "
# # sign = 1
# res = 1
# for i in range(1, n):
#     # result += str(i * (-3) )
#     # result += str(3 ** i * sign)
#     res *= (-3)
#     result += str(res)
#     result += ", "
#     # result += ", "
#     # sign = -sign
# print(result[0:(len(result) - 2)])

