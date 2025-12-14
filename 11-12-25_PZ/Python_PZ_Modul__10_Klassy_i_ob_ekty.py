# 1
# class Person:
#     def __init__(self, surname, first_name, patronymic, phone):
#         self.surname = surname
#         self.first_name = first_name
#         self.patronymic = patronymic
#         self.__birth_date = ""
#         self.phone = phone
#         self.__city = ""
#         self.__country = ""
#         self.__address = ""
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
# def get_person():
#     person = Person(surname="Parker", first_name="Peter", patronymic="Benjamin", phone="+79630155452")
#     person.set_birth_date("05.12.1988")
#     person.set_city("New York")
#     person.set_country("USA")
#     person.set_address("Forest Hills")
#     person.get_info_person()
#
# get_person()
#
# 2
# class City:
#     def __init__(self, name, region, country, population):
#         self.name = name
#         self.region = region
#         self.country = country
#         self.population = population
#         self.__postal_index = ""
#         self.__phone_code = ""
#
#     def get_info_city(self):
#         info = (f"Название города = {self.name} \n"
#                 f"Название региона = {self.region} \n"
#                 f"Название страны = {self.country} \n"
#                 f"Количество жителей = {self.population} \n"
#                 f"Почтовый индекс = {self.__postal_index} \n"
#                 f"Телефонный код = {self.__phone_code}")
#         print(info)
#
#     def set_population(self, population):
#         if population >= 0:
#             self.population = population
#         else:
#             print("Ошибка: население не может быть отрицательным")
#
#     def set_postal_index(self, postal_index):
#         self.__postal_index = postal_index
#
#     def set_phone_code(self, phone_code):
#         self.__phone_code = phone_code
#
# def get_person_city():
#     city = City(name="New York", region="Albany", country="US", population="50000")
#     city.set_postal_index("12201–12232")
#     city.set_phone_code("+9")
#     city.get_info_city()
# get_person_city()

# 3
# class Country:
#     def __init__(self, name, continent, population):
#         self.name = name
#         self.continent = continent
#         self.population = population
#         self.__phone_code = ""
#         self.__capital = ""
#         self.__cities = ""
#
#     def get_info_country(self):
#         info = (f"Название страны = {self.name} \n"
#                 f"Название континента = {self.continent} \n"
#                 f"Количество жителей = {self.population} \n"
#                 f"Телефонный код страны = {self.__phone_code} \n"
#                 f"Название столицы = {self.__capital} \n"
#                 f"Название городов страны = {self.__cities}")
#         print(info)
#
#     def set_phone_code(self, phone_code):
#         self.__phone_code = phone_code
#
#     def set_capital(self, capital):
#         self.__capital = capital
#
#     def set_cities(self, cities):
#         self.__cities = cities
#
# def get_person_country():
#     country = Country(name="Russia", continent="Eurasia", population="50000")
#     country.set_phone_code("+7")
#     country.set_capital("Moscow")
#     country.set_cities("""Москва, Санкт-Петербург, Новосибирск, Екатеринбург""")
#     country.get_info_country()
#
# get_person_country()
#
# 4
