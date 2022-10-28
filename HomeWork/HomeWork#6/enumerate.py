# enumerate() 
# Синтаксис функции enumerate() выглядит следующим образом:
# enumerate(iterable, start)
# Функция enumerate() принимает два параметра: iterable и start.

# iterable — это итерируемый объект (список, кортеж и т.д.), который будет возвращен в виде пронумерованного объекта (объекта enumerate)

# start — это начальный индекс для возвращаемого объекта enumerate. Значение по умолчанию равно 0, поэтому, если вы опустите этот параметр, в качестве первого индекса будет использоваться 0.

a = ['14', '0', '4', '6', '22', '66', '44', '222', '3665', '5', '8', '444']
b = [14, 0, 4, 6, 22, 66, 44, 222, 3665, 5, 8, 444]
e = enumerate(a)
c = enumerate(b)

print(list(e))
print('-' * 40)
print(list(c))