'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №3.05
Самостоятельная работа по уроку "Рекурсия"
'''


# Определение функции
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    return first


# Обращения к функции
result = get_multiplied_digits(40203)
print(result)