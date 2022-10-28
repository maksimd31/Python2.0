# Решение домашнего задания к Семинару №2

### добавил еще решений 
## 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

```python
print('''
1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
'''
)

def summiyogo(n): #Функция с аргументом 
    sum = 0 # Счетчик
    for i in number: # Цикл с пробужкой 
        sum += int(i) 
    return sum

number = input("Введите вещественное число: ").replace(".", "").replace(",", "")

print(summiyogo(number))
```

## 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

```python
print(
    '''
    2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*

  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
    '''
    )

import math
#С помощью встроенной функции 
print('Нахождение факториала ! ')
N=math.factorial(int(input('Введите факториал N: ')))
print('Факториал: ',N)


num = int(input('Введите факториал N: '))
factorial1 = 1
 
if(num%1==0 and num>=0):
    # Вычисляем факториал числа num
    for i in range(1, num+1):
        factorial1 = i*factorial1
        print(factorial1, end=' *')
    # Выводим результат на экран
    print(f'\n{num}! = {factorial1}')
# Если num - отрицательное или нецелое число, выводим сообщение об ошибке
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
```
## 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
*Пример:*

- Для n = 6:
    [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
    Сумма чисел = 14.0717
```python
print(
    '''
    3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
*Пример:*

- Для n = 6:
    [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
    Сумма чисел = 14.0717
    '''
)

def sequenceСalculation(n):
    res = {i:round((1 + 1 / i)**i, 2) for i in range(1, n+1)}
    return res

n = int(input("Введите число N: "))

print(sequenceСalculation(n))
```
## 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
```python
print(
    '''
    4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
    '''
)
#Взят пример с лекции 
# https://dzen.ru/media/id/5c1a663bb6a0da00aac86ae4/python-metody-spiska-append--extend--insert--43-5d405f5ddfdd2521aba93c66

from random import Random, randint


N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
    
print(numbers)
print(numbers[1] * numbers[3])

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления: ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)
```
## 5.Реализуйте алгоритм перемешивания списка.
```python
print(
    '''
    5.Реализуйте алгоритм перемешивания списка.
    '''
)

import random

array = [0, 1, 2 ,3 , 4, 5, 6, 7, 8, 9]
print(array)
for i in range(10):
    temp = array[i]
    index = random.randint(0,9)
    array[i] = array[index]
    array[index] = temp
print(array)
```