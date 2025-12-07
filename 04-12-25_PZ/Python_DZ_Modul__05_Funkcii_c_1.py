# 3
# def kvadrat(dlina, simvol, peremen):
#     if peremen == False:
#         print(dlina * simvol)
#         if dlina > 1:
#             for i in range(dlina - 2):
#                 print(simvol + " " * (dlina - 2) + simvol)
#         print(dlina * simvol)
#     else:
#         for i in range (dlina):
#             print(simvol * dlina)
#
# kvadrat(10, "*", False)
#
# 4
# def function_min(number):
#     val = min(number)
#     print("Минимальное число:", val)
#
# my_number = input("Введите числа через пробел: ").split( )
# function_min(my_number)
#
# 5
# def range_limits(range_1, range_2):
#     val_max = max(range_1, range_2)
#     val_min = min(range_1, range_2)
#     print(f"Верхняя граница - {val_max}, а нижняя граница равна - {val_min}")
#
# number_1 = int(input("Введите первое число диапазона: "))
# number_2 = int(input("Введите второе число диапазона: "))
# range_limits(number_1 , number_2)
#
# 6
# def count_digits(number):
#     val = abs(number)
#     val_count = len(str(val))
#     return val_count
#
# print(count_digits(-3456))
#
# 7
def palindrome(text):
    text = text.lower()
    if text == text[::-1]:
        print("Это палиандром")
    else:
        print("Это не палиандром")

mu_text = input()
palindrome(mu_text)






















