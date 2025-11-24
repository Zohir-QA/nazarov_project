# 1
list = [41, 24, 15, 6, 20, -10, 48, -23, 31, -25, 30, -14, 1, 7, 15, 40, 34, 47, -14, 41]
# sum_minus = 0
# sum_chet = 0
# sum_ne_chet = 0
# sum_3 = 0
list_max = list.index(max(list))
list_min = list.index(min(list))
start_index = min(list_min, list_max) + 1
end_index = max(list_min, list_max)
min_max = 1
# for i in list:
#     if i < 0:
#         sum_minus += i
#     if i % 2 == 0:
#         sum_chet += i
#     if i % 2 != 0:
#         sum_ne_chet += i
#     if i % 3 == 0:
#         sum_3 += i
if start_index < end_index:
    for i in range(start_index, end_index):
        min_max *= list[i]

print("Сумма отрицательных чисел:", sum_minus)
print("Сумма четных чисел:", sum_chet)
print("Сумму нечетных чисел:", sum_ne_chet)
print("Произведение элементов с индексами кратными 3:", sum_3)
print("Произведение элементов между минимальным и максимальным элементом:", min_max)


