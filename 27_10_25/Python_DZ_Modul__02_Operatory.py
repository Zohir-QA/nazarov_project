# 1 Задание
# my_number_1 = int(input("Введите номер дня недели (1-7): "))
# if my_number_1 == 1:
#     print("Понедельник")
# elif my_number_1 == 2:
#     print("Вторник")
# elif my_number_1 == 3:
#     print("Среда")
# elif my_number_1 == 4:
#     print("Четверг")
# elif my_number_1 == 5:
#     print("Пятница")
# elif my_number_1 == 6:
#     print("Суббота")
# elif my_number_1 == 7:
#     print("Воскресенье")
# else:
#     print("Введите число от 1 до 7.")
# 2 Задание
# my_number_1 = int(input("Введите номер месяца (1-12): "))
# if my_number_1 == 1:
#     print("Январь")
# elif my_number_1 == 2:
#     print("Февраль")
# elif my_number_1 == 3:
#     print("Март")
# elif my_number_1 == 4:
#     print("Апрель")
# elif my_number_1 == 5:
#     print("Май")
# elif my_number_1 == 6:
#     print("Июнь")
# elif my_number_1 == 7:
#     print("Июль")
# elif my_number_1 == 8:
#     print("Август")
# elif my_number_1 == 9:
#     print("Сентябрь")
# elif my_number_1 == 10:
#     print("Октябрь")
# elif my_number_1 == 11:
#     print("Ноябрь")
# elif my_number_1 == 12:
#     print("Декабрь")
# else:
#     print("Введите число от 1 до 12.")
# 3 Задание
# my_number_1 = int(input("Введите число: "))
# if my_number_1 > 0:
#     print("Number is positive")
# elif my_number_1 < 0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")
# 4 Задание
my_number_1 = int(input("Введите число 1: "))
my_number_2 = int(input("Введите число 2: "))
if my_number_1 == my_number_2:
    print("Числа равны")
else:
    min_number = min(my_number_1, my_number_2)
    max_number = max(my_number_1, my_number_2)
    print("Числа в порядке возрастания:", min_number, max_number)