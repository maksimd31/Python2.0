print(
    '''
    4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
    '''
)
# Взят пример с лекции
# https://dzen.ru/media/id/5c1a663bb6a0da00aac86ae4/python-metody-spiska-append--extend--insert--43-5d405f5ddfdd2521aba93c66

from random import Random, randint

N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N + 1))

print(numbers)
print(numbers[1] * numbers[3])

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления: ')
    if s == "":
        break
    f.write(s + "\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)
