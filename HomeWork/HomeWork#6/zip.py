# zip создает кортежи стоящие на одинаковых индексах
# через zip нельзя вызавть len а также вызвать индекс
# zip можно итерировать только один раз

# есть два списка
a = [5, 6, 7, 8, 9]

b = [100, 200, 300, 30, 65]

c = 'sdsd', 'sdsdd', 'sdsdsd', 'sdwedwse', 'sdsdsdcf'

d = 'ABCDF'

# for i in range(5):
#     print(a[i], b[i])

print(list(zip(a, b, c, d)))

# массовое присвоение через zip

for a1, b1, c1, d1 in zip(a, b, c, d):
    print(a1, b1, c1, d1)

# Получение списков через zip. сортирует по спискам

result = zip(a, b, c, d)

a2, b2, c2, d1 = zip(*result)
print(a2, b2, c2, d1)

# print(a2,b2,c2,d1 = zip(*result))

# * - выполняет распаковку элементов
