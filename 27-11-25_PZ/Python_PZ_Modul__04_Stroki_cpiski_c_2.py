# 1
# number = input("Введите арифметическое выражение: ")
# number = list(number)
# my_list = []
# my_list_1 = []
# simvol = 0
# my_bool = False
# for i in number:
#     if i in ["*","+","-","/"]:
#         simvol = i
#         my_bool = True
#     elif my_bool != True:
#         my_list.append(i)
#     elif my_bool != False:
#         my_list_1.append(i)
# num = ""
# for val in my_list:
#     num += val
# num_2 = ""
# for i in my_list_1:
#     num_2 += i
# if simvol == "+":
#     print(int(num) + int(num_2))
# elif simvol == "-":
#     print(int(num) - int(num_2))
# elif simvol == "*":
#     print(int(num) * int(num_2))
# else:
#     print(int(num) / int(num_2))
# 2
import random
# val= random.randint(-100,100)
count = 0
mu_list = []
while count < 10:
    val = random.randint(-100, 100)
    mu_list.append(val)
    count +=1
print(mu_list)
# list = [41, 24, 15, 6, 20, -10, 48, -23, 31, -25, 30, -14, 1, 7, 15, 40, 34, 47, 14, -21, 0]
# number_max = max(list)
# number_min = min(list)
# nul = list.count(0)
# plus = []
# for i in list:
#     if i < 0:
#         plus.append(i)
# minus = []
# for i in list:
#     if i > 0:
#         minus.append(i)
# print(f"Минимальное - {number_max} и максимальное - {number_min} элементы")
# print()
