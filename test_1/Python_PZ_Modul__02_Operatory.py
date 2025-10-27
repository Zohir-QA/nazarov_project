# 1
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
# 2
# number = int(input("Введите число: "))
# if number % 7 == 0:
#     print("Number is multiple 7")
# else:
#     print("Number is not multiple 7")
# 3
# my_number_1 = int(input("Введите число 1:"))
# my_number_2 = int(input("Введите число 2:"))
# if my_number_1 > my_number_2:
#     print("Максимальное: ", my_number_1)
# else:
#     print("Максимальное: ", my_number_2)
# 4
# my_number_1 = int(input("Введите число 1:"))
# my_number_2 = int(input("Введите число 2:"))
# if not my_number_1 > my_number_2:
#     print("Минимальное: ", my_number_1)
# else:
#     print("Минимальное: ", my_number_2)
# 5
my_number_1 = int(input("Введите число 1:"))
my_number_2 = int(input("Введите число 2:"))
print("Выберите операцию:")
print("1. Cумму двух чисел")
print("2. Разницу двух чисел")
print("3. Среднеарифметическое")
print("4. Произведение двух чисел")
mu_choice = input("Введите номер операции: ")
if mu_choice == "1":
    otvet = my_number_1 + my_number_2
    print("Результат: ", otvet)
elif mu_choice == "2":

    print("Результат: ", otvet)
elif mu_choice == "3":
    print("Результат: ", otvet)
elif mu_choice == "4":
    print("Результат: ", otvet)
else:
    print("Нужно вести число от 1 до 4")
