# var = 7
# print(var > 8)
#
# var = 7
# my_bool = var > 8
# print(my_bool)
# if my_bool == False:
#     print("Привет!")
# else:
#     print("Пока!")
#
# and, or, not
#
# x = 5
# and:
# x > 0 and x < 10
#
# if username == "admin" and password == "secret_password"
#
#Возращает тру если хоть одно из условий истина
# x = 15
# or:
# x < 0 or x > 10
#
# not:
# инвертирует логическое условие
# is_valid = True
# not is_valid
#
# day = "Monday"
# prazdnik = True
#
# if day == "Monday" or not prazdnik:
#     print("Сегодня выходной день!")
# else:
#     print("Сегодня рабочий день!")
#
# x = 4
# x > 0 and x % 2 == 0
#
# if x == 1 or 2 не правильно
# if x == 1 or x == 2 правильно
#
# if условие=None:
#     блок_кода_true
# else:
#     блок_кода_not_true
#
# x = 8
# if x % 2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")
#
# if условие_1:
#     блок_кода_1
# elif условие_2:
#     блок_кода_2
# else:
#     блок_кода_3
#
# age = int(input("Возраст: "))
#
# if age < 7:
#     print("Вы школьник")
# elif age < 15:
#     print("Вы все еще школьник")
# elif age < 18:
#     print("Вы почти не школьник")
# elif age < 25:
#     print("Пора работать")
# else:
#     print("Вы пенсионер")
#
# is_raining = True
# temp = -1
#
# if is_raining:
#     if temp < 0:
#         print("Идет снег")
#     else:
#         print("Идет дождь")
# else:
#     if temp > 0:
#         print("Осадков нет но тепло")
#     else:
#         print("Осадков нет но холодно")
# 1
# number = int(input("Ведите число: "))
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
# 2
# number = int(input("Ведите число: "))
# if number % 7 == 0:
#     print("Number is multiple 7")
# else:
#     print("Number is not multiple 7")
# from itertools import count
#
# my_number_1 = int(input("Введите число 1:"))
# my_number_2 = int(input("Введите число 2:"))
# if number % 7 == 0:
#     print("Number is multiple 7")
# else:
#     print("Number is not multiple 7")
#
# a = 123456
# a1 = 123456 % 10
# b = a % 100
# b1 = b // 10
# v = a % 10000
# v1 = v // 1000
# print(a1,b1,v1)
# тернарный оператор
# a = False
# b = 100 if a == True else 1000
# print(b)
#
# print(bool(0)) #fols нулевое значение
# print(bool("")) # bool() - проверяет правда или лож
# print(bool(None))
# print(bool([]))
# print(bool({}))
# print(bool(())) # TUPL - кортеж
#
# while <логическая консрукция>:
#     <логика>
#     <логика>
#     ...
#
# while True:
#     print("Мы на уроке по python")
#
# counter = 5
# while counter != 0:
#     print("Мы на уроке по python")
#     counter = counter-1
#
# counter = 5
# while counter:
#     print("Мы на уроке по python")
#     counter = counter-1
#1
# my_number_1 = int(input("Введите число: "))
# counter = 1
# while counter != my_number_1+1:
#      print(counter)
#      counter = (counter+1)
#2
# my_number_1 = int(input("Введите число: "))
# counter = 1
# counter1 = 0
# while counter != my_number_1+1:
#     counter1 = counter + counter1
#     counter = (counter+1)
# print(counter1)
#
# for - цикл используется для перебора иэлементов в некоторой последовательности или итерируемого объекта
# for <переменая> in <последовательность>:
#     логика_1
#     логика_1
#     ...
#
# range(10)
#
# for numb in range(1, 11, "nun", "pop")
#     print(numb)
#
# i = 0
# while i < 11:
#     print(i)
#     i += 1
#
# for i in range(11):
#     print(i)
#
# print(range(10))
#
# for i in range(1, 100, 2):
#     print(i)
#
# val = "Python"
# val_2 = ""
# for i in val:
#     val_2 += i
# print(val_2)
#
# break
#
# var = "Hello, its a break"
# for i in [1,2,3,52,2,3]:
#     print(i)
#     if i == 52:
#         break
# print(var)
#
# my_number_1 = int(input("Введите число: "))
# counter = 1
# while counter != my_number_1+1:
#      print(counter)
#      counter = (counter+1)
# my_number_1 = int(input("Введите число: "))
# for i in range (1, my_number_1+1):
#     print(i)
# 3
# my_number_1 = int(input("Введите число: "))
# for i in range (1, my_number_1+1):
#     print(i)
#
# continue
#
# for i in range(1,101):
#     if i % 2 == 0:
#         continue
#     print(i)
#
# numbers = [1, 3, 5, 8, 9, 10]
# for num in numbers:
#     print(num)
#     if num == 7:
#         print("Ура, мы нашли число 7")
#         break
# else:
#     print("К сожалению числа 7 там нет")
#
# pass - заглушка в коде











