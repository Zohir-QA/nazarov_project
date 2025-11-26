# 1
# list = [41, 24, 15, 6, 20, -10, 48, -23, 31, -25, 30, -14, 1, 7, 15, 40, 34, 47, 14, -21]
# sum_minus = 0
# sum_chet = 0
# sum_ne_chet = 0
# sum_3 = 0
# for i in list:
#     if i < 0:
#         sum_minus += i
#     if i % 2 == 0:
#         sum_chet += i
#     if i % 2 != 0:
#         sum_ne_chet += i
#     if i % 3 == 0:
#         sum_3 += i
# list_max = list.index(max(list))
# list_min = list.index(min(list))
# if list_min < list_max:
#     start = list_min
#     end = list_max
# else:
#     start = list_max
#     end = list_min
# min_max = 1
# for i in range(start + 1, end):
#     min_max *= list[i]
# positive_index_start = 0
# for i in range(len(list)):
#     if list[i] > 0:
#         positive_index_start = i
#         break
# positive_index_end = 0
# for i in range(len(list) - 1, -1, -1):
#     if list[i] > 0:
#         positive_index_end = i
#         break
# sum_positive = 0
# for i in range(positive_index_start + 1, positive_index_end):
#         sum_positive += list[i]
# print("Сумма отрицательных чисел:", sum_minus)
# print("Сумма четных чисел:", sum_chet)
# print("Сумму нечетных чисел:", sum_ne_chet)
# print("Произведение элементов с индексами кратными 3:", sum_3)
# print("Произведение элементов между минимальным и максимальным элементом:", min_max)
# print(f"Сумму элементов, находящихся между первым ({list[positive_index_start]}) и последним ({list[positive_index_end]}) положительными элементами: {sum_positive}")
# 2
list = [41, 24, 15, 6, 20, -10, 48, -23, 31, -25, 30, -14, 1, 7, 15, 40, 34, 47, 14, -21]
chet = []
for i in list:
    if i % 2 == 0:
        chet.append(i)
no_chet = []
for i in list:
    if i % 2 != 0:
        no_chet.append(i)
negativ = []
for i in list:
    if i < 0:
        negativ.append(i)
positiv = []
for i in list:
    if i > 0:
        positiv.append(i)
print("Четные:", chet)
print("Нечетные:", no_chet)
print("Отрицательные:", negativ)
print("Положительные:", positiv)