# 1
# def qitata_author():
#     qitata= "\"Don't let the noise of others' opinions drown out your own inner voice.\""
#     author = "— Steve Jobs"
#     print(qitata)
#     print(author)
# qitata_author()
# 2
# def ne_chet(number_start, number_end):
#     for i in range(number_start, number_end + 1):
#         if i % 2 != 0:
#             print(i)
# ne_chet(1,10)
# 3
# def linii (dlina, napravlenie, simvol):
#     if napravlenie == "horizontal":
#         print(simvol * dlina)
#     elif napravlenie == "vertical":
#         for i in range(1, dlina+1):
#             print(simvol)
# linii(10,"horizontal","*")
# 4
# def max_number(number_1, number_2, number_3, number_4):
#     val = max(number_1, number_2, number_3, number_4)
#     print(val)
# max_number (15,1,55,111)
# 5
# def summ_number(number_start, number_end):
#     val = 0
#     for i in range(number_start, number_end+1):
#         val +=i
#     print(val)
# summ_number(1, 10)
# 6
def prostoe_number(number_1):
    if number_1 <= 1:
        return False
    if number_1 == 2:
        return True
    if number_1 % 2 == 0:
        return False
prostoe_number(1)