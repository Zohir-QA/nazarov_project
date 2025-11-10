# 1 задание
# my_number_1 = int(input("Введите число: "))
# for i in range (1, 10+1):
#     counter = my_number_1 * i
#     print(my_number_1, "*", i, "=", counter)
# 2 задание
# print("Из какой валюты хотите конвертировать: 1. RUB\n", "2. USD", sep=" "*39)
# my_number_1 = int(input("Введите цифру валюты: "))
# my_number_2 = int(input("Введите сумму: "))
# if my_number_1 == 1:
#     print("Конвертация валют: 1. USD\n", "2. EUR\n", "3. KZT\n", "4. CNY", sep=" "*19)
#     my_number_3 = int(input("Введите цифру на какую валюту хотите конвертировать: "))
#     USD = 0.012311
#     EUR = 0.010657
#     KZT = 6.49
#     CNY = 0.088058
#     if my_number_3 == 1:
#         val = my_number_2 * USD
#         print("Результат:", val)
#     elif my_number_3 == 2:
#         val = my_number_2 * EUR
#         print("Результат:", val)
#     elif my_number_3 == 3:
#         val = my_number_2 * KZT
#         print("Результат:", val)
#     elif my_number_3 == 4:
#         val = my_number_2 * CNY
#         print("Результат:", val)
#     else:
#         print("Ошибка! Неправильный ввод")
# elif my_number_1 == 2:
#     print("Конвертация валют: 1. RUB\n", "2. EUR\n", "3. KZT\n", "4. CNY", sep=" "*19)
#     my_number_3 = int(input("Введите цифру на какую валюту хотите конвертировать: "))
#     RUB = 80.87
#     EUR = 0.86
#     KZT = 524.77
#     CNY = 7.12
#     if my_number_3 == 1:
#         val = my_number_2 * RUB
#         print("Результат:", val)
#     elif my_number_3 == 2:
#         val = my_number_2 * EUR
#         print("Результат:", val)
#     elif my_number_3 == 3:
#         val = my_number_2 * KZT
#         print("Результат:", val)
#     elif my_number_3 == 4:
#         val = my_number_2 * CNY
#         print("Результат:", val)
#     else:
#         print("Ошибка! Неправильный ввод")
# else:
#     print("Ошибка! Неправильный ввод")
# 3 задание
# number_start = int(input("Введите начало диапазона: "))
# number_end = int(input("Введите конец диапазона: "))
# my_number = int(input("Введите число: "))
# avg = (number_start + number_end) // 2 # не смог придумать что делать, если число четное делится 2
# while True:
#     if my_number == avg:
#         break
#     else:
#         my_number = int(input("Число вне диапазона! Попробуйте снова: "))
# for i in range(number_start, number_end + 1):
#     if i == my_number:
#         print("!", i, "!", sep="", end=" ")
#     else:
#         print(i, end=" ")
# 4 задание
import random
import time
print("Угадай число от 1 до 500", "(0 - выход)")
val= random.randint(1,500)
popytka = 0
start_time = time.time()
while True:
    my_number_1 = int(input("Введите число: "))
    popytka += 1
    if my_number_1 == 0:
        print("Игра прервана!")
        break
    elif my_number_1 < val:
        print("Загаданное число больше")
    elif my_number_1 > val:
        print("Загаданное число меньше")
    else:
        end_time = time.time()
        now = (end_time - start_time) // 1
        print("Поздравляем! Вы угадали за", popytka, "попыток и", now, "секунд!")
        break


