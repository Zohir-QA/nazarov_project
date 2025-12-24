# 1
# class Human:
#     def __init__(self):
#         self.name = ""
#         self.age = ""
#         self.weight = ""
#         self.height = ""
#
#     def get_info_human(self):
#         info = (f"Имя = {self.name} \n"
#                 f"Лет = {self.age} \n"
#                 f"Вес = {self.weight} \n"
#                 f"Рост = {self.height}")
#         return info
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_age(self, age):
#         self.age = age
#
#     def set_weight(self, weight):
#         self.weight = weight
#
#     def set_height(self, height):
#         self.height = height
#
# class Builder(Human):
#     def __init__(self, experience, injury):
#         super().__init__()
#         self.experience = experience
#         self.injury = injury
#
#     def get_info_builder(self):
#         info = (f"Опыт = {self.experience} \n"
#                 f"Травмы = {self.injury} \n"
#                 f"{self.get_info_human()}")
#         return info
#
# class Sailor(Human):
#     def __init__(self, rank, ship_type):
#         super().__init__()
#         self.rank = rank
#         self.ship_type = ship_type
#
#     def get_info_sailor(self):
#         info = (f"Ранг = {self.rank} \n"
#                 f"Тип судно = {self.ship_type} \n"
#                 f"{self.get_info_human()}")
#         return info
#
# class Pilot(Human):
#     def __init__(self, aircraft_type, flight_hours):
#         super().__init__()
#         self.aircraft_type = aircraft_type
#         self.flight_hours = flight_hours
#
#     def get_info_pilot(self):
#         info = (f"Тип самолета = {self.aircraft_type} \n"
#                 f"Время в полете = {self.flight_hours} \n"
#                 f"{self.get_info_human()}")
#         print(info)
#
# def get_sailor():
#     sailor = Sailor(rank=1, ship_type="m18")
#     sailor.set_name("Egor")
#     sailor.set_age("18")
#     sailor.set_height("160")
#     sailor.set_weight("60")
#     sailor.get_info_sailor()
#
# get_sailor()
# 2
# class Passport:
#     def __init__(self):
#         self.first_name = ""
#         self.last_name = ""
#         self.date_of_birth = ""
#         self.country = ""
#         self.series = ""
#         self.number = ""
#
#     def get_info_passport(self):
#         info = (f"Имя = {self.first_name} \n"
#                 f"Фамилия = {self.last_name} \n"
#                 f"Дата рождения = {self.date_of_birth} \n"
#                 f"Страна = {self.country} \n"
#                 f"Серия = {self.series} \n"
#                 f"Номер = {self.number}")
#         return info
#
#     def set_first_name(self, first_name):
#         self.first_name = first_name
#
#     def set_last_name(self, last_name):
#         self.last_name = last_name
#
#     def set_date_of_birth(self, date_of_birth):
#         self.date_of_birth = date_of_birth
#
#     def set_country(self, country):
#         self.country = country
#
#     def set_series(self, series):
#         self.series = series
#
#     def set_number(self, number):
#         self.number = number
#
# class ForeignPassport(Passport):
#     def __init__(self):
#         super().__init__()
#         self.visa_numb = ""
#         self.place_of_issue = ""
#
#     def get_info_foreign_passport(self):
#         info = (f"Номер визы = {self.visa_numb} \n"
#                 f"Фамилия = {self.place_of_issue}"
#                 f"{self.get_info_passport()}")
#         print(info)
#
#     def set_visa_numb(self, visa_numb):
#         self.visa_numb = visa_numb
#
#     def set_place_of_issue(self, place_of_issue):
#         self.place_of_issue = place_of_issue
#
# def get_foreign_passport():
#     foreign_passport = ForeignPassport()
#     foreign_passport.set_visa_numb("641234567")
#     foreign_passport.set_place_of_issue("+7 495")
#     foreign_passport.set_first_name("Egor")
#     foreign_passport.set_last_name("Logonom")
#     foreign_passport.set_date_of_birth("15.12.1998")
#     foreign_passport.set_country("Russia")
#     foreign_passport.set_series("4504")
#     foreign_passport.set_number("123456")
#     foreign_passport.get_info_foreign_passport()
#
# get_foreign_passport()
# 3
class Animal:
    def __init__(self):
        self.name = ""
        self.sound = ""
        self.diet = ""

    def get_info_animal(self):
        info = (f"Имя = {self.name} \n"
                f"Издает звук = {self.sound} \n"
                f"Питается = {self.diet}")
        return info

    def set_name(self, name):
        self.name = name

    def set_sound(self, sound):
        self.sound = sound

    def set_diet(self, diet):
        self.diet = diet

class Tiger(Animal):
    def __init__(self):
        super().__init__()
        self.color = ""
        self.canine_length = ""

    def get_info_tiger(self):
        info = (f"Цвет = {self.color} \n"
                f"Размер клыков = {self.canine_length} \n"
                f"{self.get_info_animal()}")
        print(info)

    def set_color(self, color):
        self.color = color

    def set_canine_length(self, canine_length):
        self.canine_length = canine_length

class Crocodile(Animal):
    def __init__(self):
        super().__init__()
        self.length = ""
        self.skin_type = ""

    def get_info_crocodile(self):
        info = (f"Длина = {self.length} \n"
                f"Тип кожи = {self.skin_type} \n"
                f"{self.get_info_animal()}")
        print(info)

    def set_length(self, length):
        self.length = length

    def set_skin_type(self, skin_type):
        self.skin_type = skin_type

class Kangaroo(Animal):
    def __init__(self):
        super().__init__()
        self.jump_distance = ""
        self.pouch_size = ""

    def get_info_kangaroo(self):
        info = (f"Длина прыжка = {self.jump_distance} \n"
                f"Размер сумки = {self.pouch_size} \n"
                f"{self.get_info_animal()}")
        print(info)

    def set_jump_distance(self, jump_distance):
        self.jump_distance = jump_distance

    def set_pouch_size(self, pouch_size):
        self.pouch_size = pouch_size

def get_crocodile():
    crocodile = Crocodile()
    crocodile.set_length("50")
    crocodile.set_skin_type("гребнистый")
    crocodile.set_name("Saltwater")
    crocodile.set_sound("шипение")
    crocodile.set_diet("рыбой")
    crocodile.get_info_crocodile()

get_crocodile()