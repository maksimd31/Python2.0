
![image](https://user-images.githubusercontent.com/106627508/194627608-8c05f444-1c76-4cd3-a7a3-571ae623bf86.png)

 
Очень сложное домашнее задание !

# HOMEWORK # 5
### Входные и выходные данные хранятся в отдельных текстовых файлах.
## 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
```python
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
```

## 2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""

```python
#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# вариант человек против человека:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 300: "))
    while x < 1 or x > 300:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 300:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# file = open('Task5.2.txt','w', encoding='utf-8')
# file.write(player1)
# file.write(player2)
# file.write(str(value))
# file.write(str(flag))
# file.close()

file = open('Task5.2.txt','w', encoding='utf-8')
file.write(f'{player1}\n')
file.write(f'{player2}\n')
file.write(f'{value}\n')
file.write(f'{flag}\n')
file.close()
```
## 3. Создайте программу для игры в ""Крестики-нолики"".

```python
## 3. Создайте программу для игры в ""Крестики-нолики"".

# print(chr(11093)) # нолик
# print(chr(10060)) # крестик
# print(chr(127942)) # кубок
# print(chr(128075)) # приветствие

print(chr(128075), ' Давайте начнем игру!')

field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def draw_field(field):
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-------------')

# draw_field(field)

def move_in_game(player_move):
    value = False
    while not value:
        player_choice = input(f'Ход делает {player_move}: ')
        try:
            player_choice = int(player_choice)
        except:
            print('Вы ввели некорректное значение. Попробуйте еще раз.')
            continue
        if 9>= player_choice >= 1:
            if(str(field[player_choice - 1]) not in ('XO')):
                field[player_choice - 1] = player_move
                value = True
            else:
                print('Невозможно выполнить ход в уже заполненную ячейку. Попробуйте еще раз.')
        else:
            print('Такой ячейки не существует. Попробуйте еще раз.')

def winning_positions(field):
    winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for all in winning_coordinates:
        if field[all[0]] == field[all[1]] == field[all[2]]:
            return field[all[0]]
    return False

def game(field):
    count = 0
    victory = False
    while not victory:
        draw_field(field)
        if count % 2 == 0:
            move_in_game('X')
        else:
            move_in_game('O')
        count += 1
        if count > 4:
            temp = winning_positions(field)
            if temp:
                print(temp)
                print('Поздравляем! Победа! ', chr(127942))
                victory = True
                break
        if count == 9:
            print('Ничья!')
            break
    draw_field(field)
                
game(field)

file = open('Task5.3.txt','w', encoding='utf-8')
file.write(f'{field}\n')
file.close()
```

## 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

```python
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")

file = open('Task5.4.txt','w', encoding='utf-8')
file.write(f'{coding(s)}\n')
file.write(f'{decoding(coding(s))}\n')
file.close()

 # ```python
    # #что бы открыть и прочитать файл спользуем фунцию open 
    # file = open('my_file.txt') #открывет файл на чтение
    # #открывает файл my_file.txt
    # print(file.read()) # прочитает файл и выведет на экран 
    # #Но будет выводится что то нечитаемое из за неправильной кодировки, 
    # #Решает проблему присвоение кодировки - **encoding='utf-8'**
    # # Пример 
    # file = open('my_file.txt', encoding='utf-8')
    # print(file.read())
    # >>> Читаемый текст
    # ```
    
    # | file.speek(0) | Прочитывает файл с начала |
    # | --- | --- |
    # | file.readline() | по умолчанию выводит первую сточку файла |
    # | file.readlines() |  выводит весь текст из файла в одну строку |
    # | file.close() | ОБЯЗАТЕЛЬНО! - закрывает файл после использования! |
    
    # ```python
    # #перебрать файл построчно 
    # file = open('my_file.txt', encoding='utf-8')
    # for line in file:
    #     print(line,end='')
    # ```
```
