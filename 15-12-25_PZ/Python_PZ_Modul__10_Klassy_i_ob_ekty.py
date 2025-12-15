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
class СountingGeometric:
    Geometric_count = 0
    def __init__(self):
        СountingGeometric.Geometric_count += 1

    @staticmethod
    def area(self):

