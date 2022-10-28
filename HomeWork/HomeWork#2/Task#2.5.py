# Вопрос который могут задавать на собеседованиях
print(
    '''
    5.Реализуйте алгоритм перемешивания списка.
    '''
)

import random

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
for i in range(10):
    temp = array[i]
    index = random.randint(0, 9)
    array[i] = array[index]
    array[index] = temp
print(array)

from random import randrange

# randrange аналог range

num = int(input("Введите данные: "))
num_list = list(range(num))
len_list = len(num_list)

print(num_list)

for i in range(len_list):
    n_1 = randrange(len_list)
    n_2 = randrange(len_list)
    num_list[n_1], num_list[n_2] = num_list[n_2], num_list[n_1]

print(num_list)
