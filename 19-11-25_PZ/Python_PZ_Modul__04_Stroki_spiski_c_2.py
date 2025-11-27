# 1
# text = input("Введите текст: ")
# text = "зима любим0ое время года многих людей, потом2у что она приносит с собой сн3ег, праздники и уют. снег позволяет кататься на санках и лыжах, а предновогодняя суета наполняет дни радостным ожиданием. поэтому, несмотря на холод, зима является особенным и любимым временем года1!"
# val = ""
# my_list = []
# my_bool = False
# for char in text:
#     if (char.isalpha() and  my_bool == False) or char == ",":
#         val = val + char
#     elif char in [".", "!", "?"]:
#         val = val + char
#         my_list.append(val)
#         val = ""
#         my_bool = True
#     elif char == " " and my_bool == True:
#         my_bool = False
#     elif char == " " and my_bool == False:
#         val = val + char
# for i in my_list:
#     a = i.capitalize()
#     val = (val + " ") + a
# text_2 = 0
# for i in range (0, len(text)):
#     tex = text[i]
#     if tex.isdigit():
#         text_2 += 1
# text_3 = 0
# punctuation = '.,!?;:'
# for i in text:
#   if i in punctuation:
#     text_3 += 1
# text_4 = text.count('!')
# print("Измененный текст:", val, sep="")
# print("\nЦифры встречаются в тексте:", text_2, "\nЗнаки препинания встречаются:", text_3, "\nВосклицательных знаков:", text_4)
# 2
# text = input("Введите элементы списка через пробел: ").split()
# text_2 = input("Введите некоторое число для поиска: ")
# counter = text.count(text_2)
# print(counter)
# 3
number = input("Введите целые числа через пробел: ").split()
number_1 = []
for i in number:
    number_1.append(int(i))
total = 0
for i in number_1:
    total += i
average = total / len(number)
print("Сумма элементов:", total)
print("Среднее арифметическое:", average)