# 2
class Wheels:
    def __init__(self):
        self.wheel_count = ""
        self.diameter = ""

    def get_info_wheels(self):
        info = (f"Количество колес = {self.wheel_count} \n"
                f"Диаметр колес = {self.diameter}")
        return info

    def set_wheel_count(self, wheel_count):
        self.wheel_count = wheel_count

    def set_diameter(self, diameter):
        self.diameter = diameter

class Engine:
    def __init__(self):
        self.power = ""
        self.fuel = ""

    def get_info_engine(self):
        info = (f"Мощность двигателя = {self.power} \n"
                f"Топлива двигателя = {self.fuel}")
        return info

    def set_power(self, power):
        self.power = power

    def set_fuel(self, fuel):
        self.fuel = fuel


class Doors:
    def __init__(self):
        self.door_count = ""
        self.color = ""

    def get_info_doors(self):
        info = (f"Количество дверей = {self.door_count} \n"
                f"Цвет дверей = {self.color}")
        return info

    def set_door_count(self, door_count):
        self.door_count = door_count

    def set_color(self, color):
        self.color = color

class Car(Wheels, Engine, Doors):
    def get_info_doors(self):
        info = (f"{self.get_info_wheels()} \n"
                f"{self.get_info_engine()} \n"
                f"{self.get_info_doors()}")
        print(info)

def get_car():
    car = Car()
    car.set_wheel_count("4")
    car.set_diameter("30")
    car.set_power("100")
    car.set_fuel("50")
    car.set_door_count("4")
    car.set_color("red")
    car.get_info_doors()

get_car()


