# 1
# class Person:
#     human_count = 0
#     def __init__(self, surname, first_name, patronymic, phone):
#         self.surname = surname
#         self.first_name = first_name
#         self.patronymic = patronymic
#         self.__birth_date = ""
#         self.phone = phone
#         self.__city = ""
#         self.__country = ""
#         self.__address = ""
#         Person.human_count +=1
#
#     def get_info_person(self):
#         info = (f"Фамилия = {self.surname} \n"
#                 f"Имя = {self.first_name} \n"
#                 f"Отчество = {self.patronymic} \n"
#                 f"Дата рождения = {self.__birth_date} \n"
#                 f"Контактный телефон = {self.phone} \n"
#                 f"Город = {self.__city} \n"
#                 f"Страна = {self.__country} \n"
#                 f"Домашний адрес = {self.__address}")
#         print(info)
#
#     def set_birth_date(self, birth_date):
#         self.__birth_date = birth_date
#
#     def set_city(self, city):
#         self.__city = city
#
#     def set_country(self, country):
#         self.__country = country
#
#     def set_address(self, address):
#         self.__address = address
#
#     @staticmethod
#     def get_count():
#         return Person.human_count
#
# def get_person():
#     person = Person(surname="Parker", first_name="Peter", patronymic="Benjamin", phone="+79630155452")
#     person.set_birth_date("05.12.1988")
#     person.set_city("New York")
#     person.set_country("USA")
#     person.set_address("Forest Hills")
#     person.get_info_person()
#     print(f"Количество созданных людей = {Person.get_count()}")
#
# get_person()

# 2
# class CountingGeometric:
#     geometric_count = 0
#     def __init__(self):
#         CountingGeometric.geometric_count += 1
#
#     @staticmethod
#     def area_rectangle(a, b):
#         S = a * b
#         return S
#
#     @staticmethod
#     def area_square(a):
#         S = a * a
#         return S
#
#     @staticmethod
#     def area_rhombus(a, h):
#         S = a * h
#         return S
#
#     @staticmethod
#     def area_triangle(a, h):
#         S = (a * h) / 2
#         return S
#
#     @staticmethod
#     def counter():
#         return CountingGeometric.geometric_count
#
# print(f"Площадь прямоугольника - {CountingGeometric.area_rectangle(15, 5)}")
# print(f"Площадь квадрата - {CountingGeometric.area_square(15)}")
# print(f"Площадь ромба - {CountingGeometric.area_rhombus(15, 20)}")
# print(f"Площадь треугольника - {CountingGeometric.area_triangle(50, 80)}")
# 3
class Math:
    @staticmethod
    def max(a, b, c, d):
        number = [a, b, c, d]
        number_max = max(number)
        return number_max

    @staticmethod
    def min(a, b, c, d):
        number = [a, b, c, d]
        number_max = min(number)
        return number_max

    @staticmethod
    def average(a, b, c, d):
        number = [a, b, c, d]
        number_max = sum(number) / len(number)
        return number_max

    @staticmethod
    def factorial(a):
        number = 1
        for i in range(1, a+1):
            number *= i
        return number

print(f"Максимум из четырех - {Math.max(1, 5, 9, 6)}")
print(f"Минимум из четырех - {Math.min(1, 5, 9, 6)}")
print(f"Cреднеарифметическое из четырех - {Math.average(1, 5, 9, 6)}")
print(f"Факториал - {Math.factorial(3)}")


