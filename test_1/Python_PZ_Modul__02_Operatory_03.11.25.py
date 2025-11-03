# 1 задание
# my_number_1 = int(input("Введите целое шестизначное число: "))
# a = my_number_1 // 100000
# b = my_number_1 // 10000 % 10
# c = my_number_1 // 1000 % 10
# abc = a+b+c
# a1 = my_number_1 % 10
# b1 = my_number_1 % 100 // 10
# c1 = my_number_1 % 1000 // 100
# a1b1c1 = a1+b1+c1
# if my_number_1 < 1000000 and my_number_1 > 99999:
#     if abc == a1b1c1:
#         print("Счастливое число")
#     else:
#         print("Несчастливое число")
# else:
#     print("Ошибка: требуется ввести шестизначное число")
# 2 задание
# my_number_1 = int(input("Введите шестизначное число: "))
# a = my_number_1 // 100000
# b = my_number_1 // 10000 % 10
# c = my_number_1 // 1000 % 10
# a1 = my_number_1 % 10
# b1 = my_number_1 % 100 // 10
# c1 = my_number_1 % 1000 // 100
# if my_number_1 < 1000000 and my_number_1 > 99999:
#     print(a1,b1,c,c1,b,a)
# else:
#     print("Ошибка: требуется ввести шестизначное число")
# 3 задание
my_number_1 = int(input("Введите номера месяца(1-12): "))
if my_number_1 == 1 or my_number_1 == 2 or my_number_1 == 12:
    print("Winter")
elif my_number_1 == 3 or my_number_1 == 4 or my_number_1 == 5:
    print("Spring")
elif my_number_1 == 6 or my_number_1 == 7 or my_number_1 == 8:
    print("Summer")
elif my_number_1 == 9 or my_number_1 == 10 or my_number_1 == 11:
    print("Autumn")
else:
    print("Ошибка: требуется ввести значение в диапазоне от 1 до 12")