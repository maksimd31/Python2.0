arr = open('D:/Домашнее задание GeekBrains/Python_start_lectures/Lesson3/Lesson3_3.txt', 'r')
my_list = arr.read() + ' '
arr.close()

numbers = []

while my_list != '':
    space_pos = my_list.index(' ')
    numbers.append(int(my_list[:space_pos]))
    my_list = my_list[space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)