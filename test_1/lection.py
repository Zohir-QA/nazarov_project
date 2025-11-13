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
#
# строки, масивы, списки
# string - тип данных, символы
# string = "/.fhhfhfhfh"
# print(string)
# encode_string = string.encode("utf-16")
# print(encode_string)
#
# string = "/.fhhfhfhfh"
# print(id(string))
#
from tkinter.font import names
#
# string = "/.fhhfhfhfh"
# string_2 = "fjfjfjhj"
# print(string + string_2 * 5)
#
# index = [0][1][2][3]
#
# print(string[-1])
# for i in range(0, len(string)+1)
#     if string[i] == "o":
#         print("Мы нашли букву О")
#
# name = "petr"
# val = f"Меня зовут: {name}"
# print(val)
#
# Методы изменения регистра строк
# print(f"1. {string_2.capitalize()}") # - переводит первый символ в верхний регистр, остальное в нижний
# print(f"2. {string_2.lower()}") # - переводит все в нижний регистр
# print(f"3. {string_2.upper()}") # - переводит все в верхний регистр
# print(f"4. {string_2.title()}") # - переводит первые буквы каждого слова в верхний регистр
# print(f"5. {string_2.swapcase()}") # - меняет верхний регистр на нижний и нижний на верхний
#
# Методы проверки строк
# print(f"1. {string_2.isalnum()}") # - проверяет состоит ли строка только из цифр и букв
# print(f"2. {string_2.isalpha()}") # - проверяет состоит ли строка только из букв
# print(f"3. {string_2.isdigit()}") # - проверяет состоит ли строка только из цифр
# print(f"4. {string_2.islower()}") # - проверяет на нижний регистр
# print(f"5. {string_2.isupper()}") # - проверяет на верхний регистр
# print(f"6. {string_2.isspace()}") # - проверяет что строка не состоит из пробелов
# print(f"7. {string_2.istitle()}") # - проверяет что у каждого слова первая буква в верхнем регистре
#
# val_str = "Привет"
# val_int = 10
# val_float = 10.0
# val_tuple = (1, 2, 3) # можно изменять
# val_list = [1, 2, 3] # можно изменять
# val_dict = {"key": "value"}
#
# print(id(val_int))
# val_list.append(4)
# print(id(val_int))
#
## обьектно передаются видно не изменемые виды даных а ссылочно изменямые
#
# стрез строки (slice)
#
# a = """
# dgdgdfgdfgdfgd "dfgdfgd", "dgdg"
# """
# print(a)
#
# строка[начало:конец]
#
# val_str = "Привет"
# print(val_str[:3])
# print(val_str[1:3])
# print(val_str[3:])
# val_str = "Hello World!"
# print(val_str[2:-1])
#
# строка[начало:конец] [start:stop:step]
#
# val_str = "123456789"
# print(val_str[::-1]) # как перевнуть строку (задом на перед) (инвертирование)
#
# val_int = "123456789"
# print(val_int[2:8:2])
# print(val_int[8:2:-2])
#
# val_str = "Hello World!"
# print("Python" in val_str) # проверка
#
# s = "AB"
# S = S * 2 + "CD"
# print(s)
#
# age = input()
# print(type(age))
#
# text = input() # проверка является слово палиандром
# text = text.lower()
#
# if text == text[::-1]
#     print("это палиандром")
# else:
#     print("Это не палиандром")
#
# name = input("Введите имя: ")
# len_name = len(name)
# print("*" * (len_name + 4))
# print("* "+name+" *")
# print("*" * (len_name + 4))
#
# val_list = [1, "int", 3.0, True, [1, 2]]
#список или (лист) изменяемая упорядочная колекция обьектов с произвольным типом данных
#
# a = "Hello World"
# a_list = list(a)
# print(a_list)
# print(type(a_list))
# a_list = list(range(1, 10))
# b = [] # создать пустой список
# b = list() # создать пустой список
# print(b)
#
fruits = ["яблоко", "апельсин", "банана", "нанасий"] # изменить индекс
# fruits[2] = ["Банан"]
# print(fruits)
# print(id(fruits))
#
# fruits.append("помидор")# добавляет слово
# print(fruits)
#
# fruits.insert(0,"вишня")
# print(fruits)
#
# a = ["a", "b"]
# b = "привет"
# fruits.extend(a)
# print(fruits)
# print(id(fruits))
# print(fruits*2)
#
# fruits.remove("яблоко")
# print(fruits)
#
# fruits.pop()
# print(fruits)
#
# del fruits[:2]
# print(fruits)
#
# fruits.clear()
# print(fruits)
#
# value = input()
# if value in fruits:
#     print("яблоко это фрукт")
#
# matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# matrix.append([1, 2, 3])
# print(matrix)
#
spisok = [1,2,3,4,5,6,7,8,9]
spisok.remove(1)
spisok.remove(9)
spisok.append(5)
spisok.insert(0,5)
print(spisok)




