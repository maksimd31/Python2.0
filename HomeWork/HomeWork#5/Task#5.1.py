# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# В тексте используется разделитель пробел.
# - **random.sample**

#     Возвращает новый список состоящий из неповторяющихся элементов, выбрано случайным образом.

import random

user_number = int(input('Введите количество слов: '))


def get_offer(user_number):
    word = 'абв'
    result = []
    for i in range(user_number):
        temp = random.sample(word, k=3)
        result.append(''.join(temp))
    my_list = ' '.join(result)
    return my_list


# .join объединяем список в строку

def clean_list(arr):
    word = 'абв'
    arr = arr.split(' ')
    for i in arr:
        if word in arr:
            arr.remove(word)
    my_list = ' '.join(arr)
    return my_list


my_list = get_offer(user_number)
print(my_list)
print(clean_list(my_list))
# split разделитель (необязательный параметр) – строка разбивается на части с помощью указанного символа.
# Если разделитель не задан, то любая пробельная строка (пробел, новая строка и т.д.)
# считается разделителем;
file = open('Task5.1.txt','w', encoding='utf-8')
file.write(f'{my_list}\n')
file.write(clean_list(my_list))
#print(file.read())#считывает файл целиком
file.close()

# file = open('my_file.txt', encoding='utf-8')
# for line in file:
#     print(line,end='')

# r - открывает файл только для чтения,
# w - открыт для записи (перед записью файл будет очищен),
# x - эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
# a - открыт для добавления в конец файла (на некоторых Unix-системах пишет в конец файла вне зависимости от позиции курсора)
# + - символ обновления (чтение + запись).
# t - символ текстового режима.
# b - символ двоичного режима (для операционных систем, которые различают текстовые и двоичные файлы).