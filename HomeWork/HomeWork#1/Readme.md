# Решение домашнего задания к Семинару №1 

## №1 По двум заданным числам проверить является ли одно квадратом второго.
```python
# 1 По двум заданным числам проверить является ли одно квадратом второго.
print('1. По двум заданным числам проверить является ли одно квадратом второго.')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a**2 == b: #Введеное число возводится в вторую степень и сравнивается с вторым числом. 
    print('Второе квадрат первого')
elif b**2 == a:
    print('Первое квадрат второго')
else: # Если не подходят варианты 
    print('Числа не является квадратом другого')
```
## №2 Найти максимальное из пяти чисел.
```python
# 2 Найти максимальное из пяти чисел.
print('Найти максимальное из пяти чисел.')
A=int(input('Введите Число №1 ==> '))
B=int(input('Введите Число №2 ==> '))
C=int(input('Введите Число №3 ==> '))
D=int(input('Введите Число №4 ==> '))
F=int(input('Введите Число №5 ==> '))
imax=0 #Счетчик 
if B > imax: #Сравнения всех переменных 
    imax=B
if C > imax:
    imax =C
if D > imax:
    imax = D
if A>imax:
    imax = A
if F>imax:
    imax = F
print('Наибольшее число: ',imax)
```
## №3 Вывести на экран числа от -N до N.

```python
# 3 Вывести на экран числа от -N до N.

print('# 3 Вывести на экран числа от -N до N.')

number = int(input(" Введите число : "))

number_two = number*-1

for i in range(number_two, number+1): #Пробежка по циклу
    print(i)
 
```
## №4. Показать первую цифру дробной части числа.

```python
# 4. Показать первую цифру дробной части числа.
import math

print('4. Показать первую цифру дробной части числа.')

# number_Three = float(input("Введите число: "))

# rez = number_Three - math.floor(number_Three)

# print(math.floor(rez*10))

number_Three = float(input("Введите число: "))
print('Первая цифра дробного числа ',end='')
print((int((number_Three *10)%10)))

# end='' - Вывод строки print в одну строку 

```

## №5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30
```python
# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

print('5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30')
number_four = int(input("Введите число :"))

if (number_four % 5 == 0 and number_four % 10 == 0 or number_four % 15 == 0) and number_four % 30 != 0:
    print("Кратно")
else:
    print("Не кратно")
 
```

## №6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

```python
# 6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

nymberDay = int(input("ВВедите число от 1 до 7: "))


def number(n):
    if nymberDay == 1:
        print("День недели понедельник день тяжелый идти на работу")
    elif nymberDay == 2:
        print("День недели вторник день тяжелый идти на работу")
    elif nymberDay == 3:
        print("День недели среда день тяжелый идти на работу")
    elif nymberDay == 4:
        print("День недели четверг день тяжелый идти на работу")
    elif nymberDay == 5:
        print("День недели пятница день тяжелый идти на работу")
    elif nymberDay == 6:
        print("День недели суббота Выходной")
    elif nymberDay == 7:
        print("День недели воск-е Выходной")
    else:
        print("Сказали же ввести число от 1 до 7")


number(nymberDay)
```
## №7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

```python
# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z)==(not x and not y and not z):
                print(x,y,z)

                
```

## №8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.

```python
# 8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.

a = int(input("введите кординаты X: "))
b = int(input("введите кординаты Y: "))

if a > 0 and b > 0:
    print("1 четверть")
elif a < 0 and b < 0:
    print("3 четверть")
elif a > 0 and b < 0:
    print("4 четверть")
elif a < 0 and b > 0:
    print("2 четверть")
else:
    print("Вы на кординатных осях")
```
## №9 Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти. 

```python
# 9 Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти. 

N = int(input('Введите номер четверти плоскости: '))
if(N == 1):
    print('0 < x < +бесконечность и 0 < y < +бесконечность')
elif(N == 2):
    print('-бесконечность < x < 0 и 0 < y < +бесконечность')
elif(N == 3):
    print('-бесконечность < x < 0 и -бесконечность < y < 0')
elif(N == 4):
    print('0 < x < +бесконечность и -бесконечность < y < 0')
else:
    print('Error.', N, '- такой четверти плоскости не существует!')
```

## №10 Найти расстояние между двумя точками пространства.

```python
# 10 Найти расстояние между двумя точками пространства.

x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('Расстояние между точками = ', round(distance, 2))


from random import random
numbers = []
for j in range(6):
    numbers.append(int(random()*6))
print(numbers)
numbers =sorted(numbers) 
```