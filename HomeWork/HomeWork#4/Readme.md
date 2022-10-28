<img width="483" alt="Снимок экрана 2022-10-08 в 17 02 54" src="https://user-images.githubusercontent.com/106627508/194711449-728871dc-db34-4ea7-aa50-b7ec6d8dd806.png">


# Домашнее задание 4
# Очень сложное домашнее задание, для решение его прибегал к гуглу.
# Также к людям из параллельных групп        

## 1. Вычислить число c заданной точностью d
пример 
d = 0.001, π = 3.141 10-1 <= d <= 10-10
```python
print(
    '''
 _  _                        __      __           _           _ _    
| || | ___  _ __   ___       \ \    / / ___  _ _ | |__       | | |   
| __ |/ _ \| '  \ / -_)       \ \/\/ / / _ \| '_|| / /       |_  _|  
|_||_|\___/|_|_|_|\___|        \_/\_/  \___/|_|  |_\_\         |_|   

    '''
)
print(
    """
     1. Вычислить число c заданной точностью d
пример 
d = 0.001, π = 3.141 10-1 <= d <= 10-10
    """
)

from cmath import pi

d = int(input("Введите точность числа Пи "))
print(f"Число Пи с заданной точностью {d} равно {round(pi,d)}")
```
## 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
```python
print(
    '''
 _              _           _ _              ___  
| |_  __ _  ___| |__       | | |            |_  ) 
|  _|/ _` |(_-/| / /       |_  _|    _       / /  
 \__|\__/_|/__/|_\_\         |_|    (_)     /___| 

    '''
)
print(
    """
    2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
    """
)

num = int(input("Введите число: "))
i = 2  # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")

```
## 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
```python
print(
    """
 _____            _           _ _              ____ 
|_   _| __ _  ___| |__       | | |            |__ / 
  | |  / _` |(_-/| / /       |_  _|    _       |_ \ 
  |_|  \__/_|/__/|_\_\         |_|    (_)     |___/ 

    """
)
print(
    """
    ## 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
    """
)

from random import randint

a = [1, 2, 2, 2, 2, 3, 1, 4]

print("Множества: ", set(a))
print(type(a))
# set - множества(удаление дублей)
#Так же все работает и с строками 
#является не упорядоченным элементом 

```
## 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
Пример
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
```python
print(
    '''
 _____            _           _ _             _ _    
|_   _| __ _  ___| |__       | | |           | | |   
  | |  / _` |(_-/| / /       |_  _|    _     |_  _|  
  |_|  \__/_|/__/|_\_\         |_|    (_)      |_|   

    '''
)
print(
    """
    4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
Пример
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
    """
)


from random import choice


def polynomial(num: int):
    if num < 1:
        return 0

    poly = ""  # пустая строка
    num_list = range(0, 10)  # список итерированный

    with open("Task4_1.txt", "a", encoding="utf-8") as my_f:
        for i in range(num, 0, -1):
            value = choice(num_list)  # выбрать объект из итерированного списка
            if value:  # если объект не 0
                poly += f"{value}*x^{i} {choice('+-')} "  # сделать запись в строку с выбором + -

        my_f.write(f"{poly}{choice(num_list)} = 0\n")  # сделать запись в файл


for _ in range(3):
    polynomial(int(input('Введите данные: ')))

```
## 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
```python
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


```