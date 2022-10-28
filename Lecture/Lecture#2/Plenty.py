colors = {'red', 'green', 'blue'}
print(type(colors))
print(colors)

colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
# colors.remove('red') KeyError: 'red'
colors.discard('red')
print(colors)
colors.clear()
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}

q = a \
    .union()  \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a)  # неизменяемое множество
