# 1 задание
# number_start = int(input("Введите начало диапазона: "))
# number_end = int(input("Введите конец диапазона: "))
# for i in range(number_start, number_end + 1):
#     if i % 7 == 0:
#         print(i)
# 2 задание
# number_start = int(input("Введите начало диапазона: "))
# number_end = int(input("Введите конец диапазона: "))
# print("1. Все числа диапазона:", end=" ")
# for i in range(number_start, number_end + 1):
#     print(i, end=" ")
# print("\n2. Все числа диапазона в убывающем порядке:", end=" ")
# for i in range(number_end, number_start-1, -1):
#     print(i, end=" ")
# for i in range(number_start, number_end + 1):
#     if i % 7 == 0:
#         print("\n3. Все числа кратные 7:", i)
# for i in range(number_start, number_end + 1):
#     if i % 5 == 0:
#         print("4. Все числа кратные 5:", i)
# 3 задание
number_start = int(input("Введите начало диапазона: "))
number_end = int(input("Введите конец диапазона: "))
for i in range(number_start, number_end + 1):
    if (i % 5) == 0 and (i % 3) == 0:
        print("Fizz Buzz")
    elif (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    else:
        print(i)

