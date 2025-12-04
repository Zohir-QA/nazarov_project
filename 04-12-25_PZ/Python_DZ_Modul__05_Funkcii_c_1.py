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
# 5
def range_limits(range_1, range_2):
    val_1 = max(range_1, range_2)
    val_2 = min(range_1, range_2)
    print(f"Верхняя граница - {val_1}, а нижняя граница равна - {val_2}")

number_1 = int(input("Введите первое число диапазона: "))
number_2 = int(input("Введите второе число диапазона: "))
range_limits(number_1 , number_2)

























