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
