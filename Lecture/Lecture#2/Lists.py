list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print()


list1[0] = 123
list2[1] = 333


for e in list1:
    print(e)

print()

for e in list2:
    print(e)


print(len(list1))
print(list1.pop(2))
print(len(list1))
print((list1))
print(list1.pop())
print(len(list1))
print((list1))
print(list1.pop())
print(len(list1))
print((list1))

print(list1.insert(1, 11))
print(list1)

print(list1.append(11))
print(list1)