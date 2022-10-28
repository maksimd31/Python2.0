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