# 1
# text = input("Введите строку: ")
# print(text[::-1])
# 2
# text = input("Введите строку: ")
# bycva = 0
# chislo = 0
# for i in text:
#     if i.isalpha():
#         bycva += 1
#     elif i.isdigit():
#         chislo += 1
# print(f"Количество букв: {bycva} и количество цифр: {chislo}")
# 3
# text = input("Введите строку: ")
# text2 = input("Введите символ: ")
# count = 0
# for i in text:
#     if i == text2:
#         count += 1
# print("Символ встречается в строке", count)
# 4
# text = input("Введите строку: ")
# text2 = input("Введите слово для поиска: ")
# count = text.count(text2)
# print("Слово встречается в строке", count)
# 5
text = input("Введите строку: ")
text2 = input("Введите слово для поиска: ")
text3 = input("Введите слово для замены: ")
print(text.replace(text2,text3))