def type_of_number():  # Тип номера
    result = input()
    while type(result) != int:
        try:
            result = int(result)
        except:
            result = input('Ошибка! Вы неверно ввели номер из списка! Попробуйте еще раз. ')
    return result
