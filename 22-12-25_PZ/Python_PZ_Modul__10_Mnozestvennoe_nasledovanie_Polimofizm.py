# 2
# class Wheels:
#     def __init__(self):
#         self.wheel_count = ""
#         self.diameter = ""
#
#     def get_info_wheels(self):
#         info = (f"Количество колес = {self.wheel_count} \n"
#                 f"Диаметр колес = {self.diameter}")
#         return info
#
#     def set_wheel_count(self, wheel_count):
#         self.wheel_count = wheel_count
#
#     def set_diameter(self, diameter):
#         self.diameter = diameter
#
# class Engine:
#     def __init__(self):
#         self.power = ""
#         self.fuel = ""
#
#     def get_info_engine(self):
#         info = (f"Мощность двигателя = {self.power} \n"
#                 f"Вместимость топлива = {self.fuel}")
#         return info
#
#     def set_power(self, power):
#         self.power = power
#
#     def set_fuel(self, fuel):
#         self.fuel = fuel
#
#
# class Doors:
#     def __init__(self):
#         self.door_count = ""
#         self.color = ""
#
#     def get_info_doors(self):
#         info = (f"Количество дверей = {self.door_count} \n"
#                 f"Цвет дверей = {self.color}")
#         return info
#
#     def set_door_count(self, door_count):
#         self.door_count = door_count
#
#     def set_color(self, color):
#         self.color = color
#
# class Car(Wheels, Engine, Doors):
#     def __init__(self):
#         super().__init__()
#         self.model = ""
#
#     def get_info_car(self):
#         info = (f"Модель = {self.model} \n"
#                 f"{self.get_info_doors()} \n"
#                 f"{self.get_info_engine()} \n"
#                 f"{self.get_info_wheels()}")
#         print(info)
#
#     def set_model(self,model):
#         self.model = model
#
# def get_car():
#     car = Car()
#     car.set_wheel_count("4")
#     car.set_diameter("30")
#     car.set_power("100")
#     car.set_fuel("50")
#     car.set_door_count("4")
#     car.set_color("red")
#     car.set_model("Cybertruck")
#     car.get_info_car()
#
# get_car()
# 3
class Animal:
    def __init__(self):
        self.show = ""
        self.sound = ""
        self.type = ""

    def set_show(self, show):
        self.show = show

    def set_sound(self, sound):
        self.sound = sound

    def set_type(self, type):
        self.type = type

    def get_info_animal(self):
        print(f"{self.show} издает звук: {self.sound}. Подвид {self.type}")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.show = "Рекс"
        self.sound = "гаф-гаф"
        self.type = "охотничья"

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.show = "Мурка"
        self.sound = "мяу"
        self.type = "сиамская"

class Parrot(Animal):
    def __init__(self):
        super().__init__()
        self.show = "Кеша"
        self.sound = "за Императора!"
        self.type = "королевский"

class Hamster(Animal):
    def __init__(self):
        super().__init__()
        self.show = "Пушистик"
        self.sound = "пи-пи-пи"
        self.type = "джунгарский"


def get_home_animal():
    animal = Parrot()
    animal.get_info_animal()
get_home_animal()


