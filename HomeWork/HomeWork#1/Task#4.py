# 4. Показать первую цифру дробной части числа.
import math

print('4. Показать первую цифру дробной части числа.')

# number_Three = float(input("Введите число: "))

# rez = number_Three - math.floor(number_Three)

# print(math.floor(rez*10))

number_Three = float(input("Введите число: "))
print('Первая цифра дробного числа ', end='')
print((int((number_Three * 10) % 10)))

# end='' - Вывод строки print в одну строку
