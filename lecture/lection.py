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
# from tkinter.font import names
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
## обьектно передаются видно не изменемые виды данных а ссылочно изменямые
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
# fruits = ["яблоко", "апельсин", "банана", "нанасий"] # изменить индекс
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
# spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# spisok.remove(1)
# spisok.remove(9)
# spisok.append(5)
# spisok.insert(0,5)
# print(spisok)
#
# """strings_and_lists"""
#
# list2 = list [:] # - копия списка
#
# перация со списками
#
# list3 = list + list2
# print(lost3) # объединение списков
#
# print (list3 * 3) # умножение списков
#
# print("text" in list3) # проверка вхождения
#
# included_list = [[1, 2, 3, 4], ["текст1", "текст2"]]# вложенные списки
# print(included_list[0][1])
# for i in included_list:
#     for subject in i:
#
#  """Методы списков"""
#
# my_list = []
# my_list.append("Мы учим Python") # добавление в конец списка
# print(my_list)
#
# my_list.extend([1, 2, 3]) # расширение списка
# print(my_list)
#
# my_list.insert(0,"Сегодня") # вставка по индексу
# print(my_list)
#
# my_list.remove(1) # удаление объекта
# print(my_list)
#
# my_list.pop(0) # удаление по индексу
# print(my_list)
#
# my_list.clear() # чистка списка
#
# val = my_list.count() # подсчет вхождения элемента в списке
# print(val)
#
# my_list1 = [1, 5, 6, 3, 7, 455, 323, 11, 146]
# my_list.sort(reverse=True) # сортировка списка
# print(my_list)
#
# my_list1.reverse() # перевернуть список
# print(my_list1)
#
# counter = 0
# while counter < len(my_list1): # перебор списка
#     print(my_list1[counter])
#     counter +=1
#
# while counter < len(my_list1):
#     val = my_list1[counter]
#     if val == 324:
#         print("Мы нашли число 323")
#         break
#     counter +=1
#
# text.replace(1,1) # замена
#
# регулярные выражения - regular expressions
#
# text = "Я живу в 2025 и"
# import re
# # \d+
# # \d*
# # ^\d+$
# #
# pattern = re.compile(r"\d+")
# #
# re.search(pattern, text) -# - находит первое совпадение с шаблоном,
# #  возвращает math-объект с информацией о искомом фрагменте, если ничего не нашли -> none
#
# re.match(pattern,text) # - ищет совпадение в начале строки
#
# re.findall(pattern, text) # - выполняет поиск всех пересекающихся совпадений шаблон pattern d строке
#
# re.fullmatch(pattern, text) # - проверяет совпадает ли вся строка указанному шаблону, возвращает
# # math-объект в случае совпадения
#
# re.finditer(pattern, text) # делает тоже самое что и findall но возвращает итерируемый объект,
# # который содержит math-объкты всех совпадений с шаблоном
#
# re.split(pattern, text, maxsplit=1)  # - разбивает строку на части по указанному шаблону, возвращает список фрагментов
#
# re.sub(pattern, repl="text", string=text, count=0) # ищет все фрагменты подходящие пот паттерн
# # если мы указываем параметр count - то будет заменено не более того кол-ва строк, что указано в count
#
# val = re.search(pattern, text)
# val.group() # - позволяет получить фрагмент соответствует найденному шаблоном
# val.start() # - позволяет получить индекс где начинается искомый фрагмент
# val.end() # - позволяет получить индекс конца искомого фрагмента
#
# # . ^ $ * + & { } [ ] \ | ( ) - основной набор мета символов в регулярных выражениях
#
# """
#
# Якоря - символы которые обозначают границы в шаблоне поиска
# ^ - якорь начало строки, соответствует позиции перед самым первым символом строки,
# если шаблон начинается с него - совпадение возможно только в начале текста
#
# $ - якорь конца строки, совпадение возможно только в конце строки
#
# \b - граница слова. Особое условие которое соответствует позиции между символом (буква-цифра) и не-символом
# Например \bcat\b - найдет cat но не найдет  catalog
#
# \B - не-граница слова, соответствие позиции внутри слова (антоним якорю \b)
# . - соответствует любому одиночному символу (буква, цифра, знак препинания и т.д) кроме символа новой строки \n
# Пример a.b найдет acb, a-b, a b но не найдет a\nb, чтобы захватывать строки - используется флаг re.DOTALL
#
# Предопределенные символьные классы:
# \d - цифра, эквивалентно написанию [0-9]. В питоне \в по умолчанию захватывает не только арабские цифры но любые другие
# из Юни кода
#
# \D - любой символ кроме цифр
#
# \w - любой буквенно-цифровой символ. Включает так же символ подчеркивания "_"
#
# \W - антоним \w
#
# \s - любой пробельный символ (табуляция \t, пробел строки \n)
#
# \S - любой не-пробельный символ
#
# [0-9][0-9][0-9] -> \d{3}
# [A-Za-z-0-9] - > \w
#
# [...] - символьный класс, в нем можно перечислить набор символов. Любой символ из набора может стоять на позиции этого класса
# Например: шаблон [AEUIOY], диапазон задается через тире.
# Внутри символьного класса большинство мета символов утрачивают свои действия, например шаблон [*+?] означает любой из символов * + ?
# Однако символы -, ^ в символьном  классе имеют особый смысл "-" - это диапазон. "^" - это отрицание, т.е если этот символ находится
# в символьном классе - любой отсутствующий символ в классе, совпадает с шаблоном
# """
# alt entr
# pass
# import re
#
# text_1 = "fdgdgdfgdfg dgdgdfgd +79001234567 fdgdfgdfgdfg"
# text_2 = "dgdfgdfgdf 89001234567 dfgdfgdfg"
#
# pattern = re.compile(r"(\+7|8)\d{10}")
# val = re.findall(pattern, text_1)
# print(val)
from pygame.examples.music_drop_fade import music_file_list

# | - или пример 7|8
# () - группирующие скобки позволяют сгруппировать или объединить несколько выражении

# 1) Написать регулярку которая вытащит из текста слова полученные от пользователя

# import re
# text_1 = input("Введите слово: ")
# text = "По моему мнению, образование играет ключевую роль в развитии общества. Образованные люди более критично мыслят и способны создавать новые идеи."
# val = re.search(text_1, text)
# print(val.group())

# 2) Написать регулярное выражение для проверки соответствует ли строка формату даты ДД.ММ.ГГГГ
# где ДД - две цифры от 1 до 31
# ММ - две цифры от 1 до 12
# ГГГГ - четыре цифры любые

# 3) Убрать с помощью регулярки все пробелы из строки
# import re
# text = "По моему мнению, образование играет ключевую роль в развитии общества. Образованные люди более критично мыслят и способны создавать новые идеи."
# pattern = re.compile(r"[\s]+")
# val = re.sub(pattern, " ", text, count=0)
# print(val)
#
# import re
#
# text = ("Сегодня я выпил 4 чашки кофе. Вчера было 6.")
# pattern = re.compile(r"(Сегодня)+")
# val = re.search(pattern, text)
# for i in val:
#     print(i.group())
# print(val.group())
# """
# Квантификатор:
# * - повторение от нуля до бесконечности
# + - повторение до 1 до бесконечности
# ? - повторение от нуля до 1 раза (делает предыдущий элемент не обязательным)
# {n} - ровно n - повторений предыдущего элемента
# {m,n} - от m до n повторений
#
# Группировка и ссылки:
# (...) - группирующие скобки.
# (?P<name>...) - Именованная группа. после ?P<name> задается имя группы

# Альтерация:
# | - операция "или". Позволяет указывать несколько альтернативных шаблонов. Шаблон A|B - это значит текст
# может попадать либо под шаблон A либо под шаблон B
#
# Флаги функций модуля re:
# re.IGNORECASE - делает поиск нечуствительным к регистру
# re.MULTILINE - Изменяет поведение метасимволов ^ и $. Они начинают реагировать на неразрывные пробелы \n
# re.DOTALL - Делает так что точка матчит абсолютно любой символ, включая переносы строк.
# """
# Шаблоны
# import re
#
# text = ("Сегодня я выпил 4 чашки кофе. Вчера было 6.25")
# float_int = re.compile(r"[+-]?\d+(\.\d+)?") # поиск дробных чисел
# email_pattern = re.compile(r"\w+@\w+\.\w+") # поиск телефона
# props_search = re.compile(r"[^.!?]+[.!?]") # поиск предложения
# word_search = re.compile(rf"\bслова\b", re.IGNORECASE) # поиск слова
# re.sub(r"\s+","", text) # удаление пробелов
# val = re.search(pattern, text)
#
# Функций
#

# def some_function(number_1, number_2):
#     a = number_1 + number_2
#     return a
#
# val = some_function(15, 56)
# print(val)
#
# some_function(number_1=50, number_2=100)
#
# def greetings(name="Irina"):
#     print(f"Приветствуют тебя, {name}, на занятии по Python")
#     some_function(15,20)
#
# greetings("Дмитрий")

# def some_function(number_1):
#     a = number_1 * number_1
#     return a
# val = some_function(15)
# print(val)
#
# global_value = 0
#
# def some_function(number_1, number_2):
#     a = number_1 + number_2
#
# val = some_function(40)
#
# модули в paython и что такое
#
# это обычные файлы с расширением .pau
#
# import math
# import sys
# import os
# from datetime import datetime
# pi = 3.141592
# print(math.tau)
# print(pi)
# # пространство имен это отдельная область где находится все именна объекта, каждый модуль имеет собственное пространство имен
# print(sys.modules)

# from mathematic.calculator.summ import sum as plus # вызвали из папки)
# from mathematic.calculator.summ import * # импортируем все
# def sum():
#     print(2+2)
# sum()
# plus()
#
# import greetings
# greetings.say_hello()
#
# if __name__ == "__main__": # используется как галовной и его нельзя использовать
#     print("module greetings.py")

# mvnrepository - различные библиотеки для пайтона
# sys.path.append("C:\\Users\\student.IT\\my_new_module")
# print("\n".join(sys.path)) # входит состав к библиотекам пайтона, входит путь
# import my_new_module
# my_new_module.
#
# пакеты - это папки с модулями
# функций - print
#
# fruits = ["яблоко", "апельсин", "банан"]
# empty_list = []
# empty_list_v2 = list()
# for i in fruits[1]:
#     for val in i[-1]:
#         print(val)
#         break
#     break
#
# Объектно-ориентированное (ОО) программирование
#
# + инкапсуляция это возможность скрыть внутренее устройство обьекта его данные и предостовлять доступ к ним
# + множество экземпляров класс служет шаблоном по которому можно создавать любое количество объектов
# + наследование можно создавать новые классы на основе уже существующих
# + полиморфизм способность функции и методов работать с объектами разных классов если они подерживают необходимый интерфейс
# обьект это конкретный экзепляр класса обладающии характеристиками описаный в классе, возвращает свойства и поведения предусмотреные классом
#
#
# stack_list =[]
#
# def push(val):
#     stack_list.append(val)
#
# def pop():
#     print(stack_list)
#     val = stack_list[-1]
#     stack_list.pop()
#     return val
#
# push(3)
# push(5)
# push(10)
# print(stack_list)
# print(pop())
# print(stack_list)
#
# class SimpleClass:
#     pass
#
# my_first_object = SimpleClass()
# print(my_first_object)
#
# class Stack:
#     counter = 0
#
#     def __int__(self):
#         Stack.counter += 1
#         self.__stack_list = []
#         self.first = 1
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         print(self.__stack_list)
#         val = self.__stack_list[-1]
#         self.__stack_list.pop()
#         return val
#
#     def set_second(self):
#         self.second = 2
#
# stack_obj = Stack()
# print(f"Экземпляр класса {stack_obj} имеет переменные: ", stack_obj.__dict__)
# stack_obj.set_second()
# print(f"Экземпляр класса {stack_obj} имеет переменные: ", stack_obj.__dict__)
#
# print(getattr(stack_obj, "first"))
# print(stack_obj.__dict__)
#
# stack_obj_1 = Stack()
# print(f"Экземпляр класса {stack_obj_1} имеет переменные: ", stack_obj.__dict__)
# print("Всего создано объектов:", Stack.counter)
# stack_obj.push(3)
# stack_obj.push(156)
# stack_obj.push(734)
# print(stack_obj.pop())

# stack_obj_2.push(100)
# print(stack_obj_2.pop())

# stack_obj.stack_list.append(100)
# print(stack_obj.__int__)
#
# свойство обьектов, методы, атрибуты и наследование
# атрибуты экземпляра это свойство сопуствующему обьекту
# переманя класса это атрибуты пренадлежащему саму обьекту
# переманя класса это атрибуты пренаджлежащие саму классу а не отдельно самому классу
#
# наследование классов это способ получить все атрибуты и методы базового (родительского) класса под классу(дочернему классу)
# под класс это который расширяет и кторый уточняет функциональность под класса
# класс от которого наследуется называется супер клас а следуйщий который наследует под класс

# class SuperClass:
#     pass
# class SubClass(SuperClass):
#     pass
#
# class Animal:
#     def __int__(self):
#         self.can_breathe = True
#         self.average_age = 20
#         self.animal_sound = " "
#
#     def get_animal_info(self):
#         print(f"Base info: все животные дышат: {self.can_breathe}, их средний возраст равен: {self.average_age}.")
#
# class Mammals(Animal):
#     def __int__(self, eyes_count = 2):
#         super().__int__()
#         self.feet_count = 4
#         self.eyes_count = 2
#
# class Cats(Mammals):
#     def __int__(self, eyes_count=2):
#         super().__int__(eyes_count=eyes_count)
#         self.name = "Musa"
#         self.animal_sound = "meow"
#
#     def get_cat_info(self):
#         self.get_animal_info()
#         print(f"Кошку зовут: {self.name}, она имеет {self.eyes_count} глаз, у нее {self.feet_count} ноги")
#
#     # def get_cat_info(self):
#     #     print(f"Коты имеют: {self.feet_count} ног, издают звук: {self.animal_sound}, меют количество глаз равное: {self.eyes_count}"
#     #           f"В среднем живут {self.average_age} лет")
#
#
# cat_masha = Cats(eyes_count=1, name="Masha")
# cat_masha.get_cat_info()
#
# cat_barsik = Cats(eyes_count=2, name="Barsik")
# cat_barsik.get_cat_info()
# cats = Cats()
# cats.get_cat_info()
# mammals = Mammals
# print(mammals.__dict__)

# работа со словарями
# - изменяемая структура данных
age_of_names = {"Alice": 15}
# my_dict_1 = dict(Alice=15, Bob=55)
my_dict_1 = dict([("Alice", 15), ("Pavel", 32), ("Zohir", 28)])
empty_dict = {}

# my_list = ["Alice", "Bob", "Irina", "Pavel"]
# empty_dict = empty_dict.fromkeys(my_list, None)\
# name = "Alic"
# age_of_names[name] = 30
# print(name in age_of_names)
#
# print(empty_dict)
#
# print(age_of_names, my_dict_1)
#
# for key, val in my_dict_1.items():
#     print(f"{key} - {val}")

# получение какого значения слова по ключу
# value = my_dict_1.get("Pavel")
# print(value)

keys = my_dict_1.keys()
# возращает специальный обьект из словаря

values  = my_dict_1.values()

items = my_dict_1.items()

age_of_names.update(my_dict_1)
print(age_of_names)

# удаление ключей из словаря
# age_of_names.pop("Alice", None)
# print(age_of_names)

val = age_of_names.popitem()
# print(val)

# age_of_names.clear()

copy_dict = age_of_names.copy()

students = {
    "Alice": {
        "age": 15, "last_name": "w423", "courses": ["math", "biology"]
    },
    "Bob":{
        "age": 19, "last_name": "w423", "courses": ["math", "biology"]
    }
}

students["Alice"]["courses"].append("english")
print(students["Alice"]["courses"])