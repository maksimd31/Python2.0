from turtle import right

print('''
1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
'''
      )

# def summ_iyogo(n): #Функция с аргументом 
#     sum = 0 # Счетчик
#     for i in number: # Цикл с пробужкой 
#         sum += int(i) 
#     return sum

# number = input("Введите вещественное число: ").replace(".", "").replace(",", "")

# print(summ_iyogo(number))

# Метод replace() возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.

# Метод в Python может принимать максимум 3 параметра: 
# old ‒ старая подстрока, которую нужно заменить; 
# new ‒ новая подстрока, которая заменит старую подстроку; 
# count (необязательно) ‒ сколько раз вы хотите заменить старую подстроку новой. Примечание: Если число не указано, метод заменяет все вхождения старой подстроки новой.
# Примечание: Если число не указано, метод заменяет все вхождения старой подстроки новой.

n = int(input('Введите вещественное число: '))
F = 1
for i in range(n):
    F *= -3
    print('Сгенерированые числа', F)
# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

# def number_of_lines_in_file(doc):
#     return len(open(doc).readlines())

# def merge_files(doc1, doc2, doc3):
#     if number_of_lines_in_file(doc1) == number_of_lines_in_file(doc2):
#         file1 = open(doc1, 'r')
#         file2 = open(doc2, 'r')
#         while True:
#             t1 = file1.readline().strip('\n')
#             t1 = t1.strip(" ")
#             t1 = t1.strip("0")
#             t1 = t1.strip(" ")
#             t1 = t1.strip("=")
#             t2 = file2.readline()
#             if not (t1 or t2):
#                 break
#             with open(doc3, 'a') as f3:
#                 f3.write(f"{t1}+ {t2}")
#     else:
#         print('The contents of the files do not match!')

# merge_files('D:/Домашнее задание GeekBrains/Seminar_python(start)/HomeWork4/Task4.txt', 'D:/Домашнее задание GeekBrains/Seminar_python(start)/HomeWork4/Task4_2.txt', 'D:/Домашнее задание GeekBrains/Seminar_python(start)/HomeWork4/Task5.txt')

from random import choice


def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second):  # проверка на совпадение количества строк в файлах
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
                for i, v in enumerate(
                        first):  # enumerate возвращает кортеж, содержащий отсчет от start и значение, полученное из итерации
                    my_f_3.write(
                        f"{v[:-5]} + {second[i]}")  # удаляем с его помощью последние 5 элементов из строки первого файла (= пробел 0 /n)
        else:
            print("The contents of the files do not match!")


# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly_2.txt")
# C возведением в степень Вариант №2
num = int(input('Введите числа: '))
for i in range(num):
    # print(3**i*(-1)**i)
    print('Сгенерированые числа', (-3) ** i)
