# 1
# print("Проверьте является ли введенная строка палиндромом.")
# text = input("Введите строку: ")
# text = text.lower()
# if text == text[::-1]:
#     print("Это палиндром")
# else:
#     print("Это не палиндром")
# 2
# text = input("Введите текст: ")
# text_2 = input("Введите список зарезервированных слов: ").split() # разбивает введенную строку на отдельные слова
# for i in text_2:
#     text = text.replace(i, i.upper())
# print(text)
# 3
text = input("Введите текст: ")
text_1 = text.count('.')
text_2 = text.count('!')
text_3 = text.count('?')
count = text_1 + text_2 + text_3
if text[-1] != "." and text[-1] != "!" and text[-1] != "?":
    count += 1
    print("Количество предложений:", count)
else:
    print("Количество предложений:", count)