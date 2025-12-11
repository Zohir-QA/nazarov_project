# 1
# class Car:
#     def __init__(self, model, year, manufacturer):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.__engine_volume = ""
#         self.__color = ""
#         self.__price = ""
#
#     def get_car_info(self):
#         info = (f"Модель = {self.model} \n"
#                 f"Год выпуска = {self.year} \n"
#                 f"Производитель = {self.manufacturer} \n"
#                 f"Объем двигателя = {self.__engine_volume} \n"
#                 f"Цвет = {self.__color} \n"
#                 f"Цена = {self.__price}")
#         print(info)
#
#     def set_engine_volume(self, engine_volume):
#         self.__engine_volume = engine_volume
#
#     def set_color(self, color):
#         self.__color = color
#
#     def set_price(self, price):
#         self.__price = price
#
# def get_car():
#     car = Car(model="Cybertruck", year="2012", manufacturer="Italy")
#     car.set_engine_volume("350cm/2")
#     car.set_color("Red")
#     car.set_price("99999$")
#     car.get_car_info()
#
# get_car()

# 2
# class Book:
#     def __init__(self, title, year, publisher):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.__genre = ""
#         self.__author = ""
#         self.__price = ""
#
#     def get_book(self):
#         info = (f"Название книги = {self.title} \n"
#                 f"Год выпуска = {self.year} \n"
#                 f"Издатель = {self.publisher} \n"
#                 f"Жанр = {self.__genre} \n"
#                 f"Автор = {self.__author} \n"
#                 f"Цена = {self.__price}")
#         print(info)
#
#     def set_genre(self, genre):
#         self.__genre = genre
#
#     def set_price(self, price):
#         self.__price = price
#
#     def set_author(self, author):
#         self.__author = author
#
# def get_book():
#     book = Book(title="Fifty Shades of Grey", year="2007", publisher="Buka")
#     book.set_genre("Horror")
#     book.set_author("Joanne Rowling")
#     book.set_price("49,99")
#     book.get_book()
#
# get_book()

# 3
class Stadium:
    def __init__(self, name, country, city):
        self.name = name
        self.__date = ""
        self.country = country
        self.city = city
        self.__capacity = ""

    def get_stadium(self):
        info = (f"Название стадиона = {self.name} \n"
                f"Дата открытия = {self.__date} \n"
                f"Страна = {self.country} \n"
                f"Город = {self.city} \n"
                f"Вместимость = {self.__capacity}")
        print(info)

    def set_date(self, date):
        self.__date = date

    def set_capacity(self, capacity):
        self.__capacity = capacity

def get_stadium():
    stadium = Stadium(name="Megaton", country="USA", city="Big Town")
    stadium.set_date("2099")
    stadium.set_capacity("5000")
    stadium.get_stadium()

get_stadium()