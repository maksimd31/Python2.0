# 2 Найти максимальное из пяти чисел.
print('Найти максимальное из пяти чисел.')
A = int(input('Введите Число №1 ==> '))
B = int(input('Введите Число №2 ==> '))
C = int(input('Введите Число №3 ==> '))
D = int(input('Введите Число №4 ==> '))
F = int(input('Введите Число №5 ==> '))
imax = 0  # Счетчик
if B > imax:  # Сравнения всех переменных
    imax = B
if C > imax:
    imax = C
if D > imax:
    imax = D
if A > imax:
    imax = A
if F > imax:
    imax = F
print('Наибольшее число: ', imax)
