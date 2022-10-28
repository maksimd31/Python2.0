print(
    '''
 _____            _           _ _             ___         
|_   _| __ _  ___| |__       | | |           | __|        
  | |  / _` |(_-/| / /       |_  _|    _     |__ \        
  |_|  \__/_|/__/|_\_\         |_|    (_)    |___/        

    '''
)
print(
    '''
    ## 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
    '''
)

with open('task5_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('task5_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('task5_1.txt','r') as file:
    task5_1 = file.readline()
    list_of_task5_1_1 = task5_1.split()


with open('task5_2.txt','r') as file:
    task5_2 = file.readline()
    list_of_task5_2_2 = task5_2.split()

print(f'{list_of_task5_1_1} + {list_of_task5_2_2}')
sum_task5 = list_of_task5_1_1 + list_of_task5_2_2

with open('sum_task5.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_task5_1_1} + {list_of_task5_2_2}')

# Что такое SymPy? Это библиотека символьной математики языка Python.
# Она является реальной альтернативой таким математическим пакетам как Mathematica или
# Maple и обладает очень простым и легко расширяемым кодом. SymPy написана исключительно на языке
# Python и не требует никаких сторонних библиотек.
# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import choice


def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second): # проверка на совпадение количества строк в файлах
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
                for i, v in enumerate(first): # enumerate возвращает кортеж, содержащий отсчет от start и значение, полученное из итерации
                    my_f_3.write(f"{v[:-5]} + {second[i]}") # удаляем с его помощью последние 5 элементов из строки первого файла (= пробел 0 /n)
        else:
            print("The contents of the files do not match!")


# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly_2.txt")