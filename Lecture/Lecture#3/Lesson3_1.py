# def f(x):
#     x**2

# g = f

# print(f(1))
# print(g(1))

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# def calc(x):
#     return x+10

# print(calc(10))

# def calc2(x):
#     return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc, 10)

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y

def mylt(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(lambda x, y: x + y, 4, 5)

