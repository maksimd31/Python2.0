# list_comprehension

# def f (x):
#     return x>9 and x<100

# a = [14,0,4,6,22,66,44,222,3665,5,8,444]
# b = [i for i in a if i>9 and i<100]
# print(b)

# пример к следующему д/з

people = [{
    "first_name": "Василий",
    "last_name": "Марков",
    "birthday": "9/25/1984"
}, {
    "first_name": "Регина",
    "last_name": "Павленко",
    "birthday": "8/21/1995"
}]

birthdays = [
    person[term]
    for person in people
    for term in person
    if term == "birthday"
]

print(birthdays)

# В этом примере мы сперва перебираем people, присваивая каждый словарь person. После этого перебираем каждый идентификатор в словаре, присваивая ключи term. Если значение term равно birthday, то значение person[term] добавляет в list comprehension.
