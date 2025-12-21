# 1
class Human:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_info_human(self):
        info = (f"Имя = {self.name} \n"
                f"Лет = {self.age} \n"
                f"Вес = {self.weight} \n"
                f"Рост = {self.height}")
        print(info)

class Builder(Human):
    def __init__(self, experience, injury):
        self.experience = experience
        self.injury = injury

    def get_info_builder(self):
        info = (f"Опыт = {self.experience} \n"
                f"Травмы = {self.injury} \n"
                f"{self.get_info_human()}")
        print(info)

class Sailor(Human):
    def __init__(self, rank, ship_type):
        super().__init__(name="", age=22, weight=70, height=100)
        self.rank = rank
        self.ship_type = ship_type

    def get_info_sailor(self):
        info = (f"Ранг = {self.rank} \n"
                f"Тип судно = {self.ship_type} \n"
                f"{self.get_info_human()}")
        print(info)

class Pilot(Human):
    def __init__(self, aircraft_type, flight_hours):
        self.aircraft_type = aircraft_type
        self.flight_hours = flight_hours

    def get_info_pilot(self):
        info = (f"Тип самолета = {self.aircraft_type} \n"
                f"Время в полете = {self.flight_hours} \n"
                f"{self.get_info_human()}")
        print(info)

def get_sailor():
    # sailor = Sailor(rank=1, ship_type="Pilot")
    # sailor.get_info_sailor()
    Human(name="", age=22, weight=70, height=100)
    # sailor.get_info_human()
    sailor = Sailor(rank=1, ship_type="Pilot")
    sailor.get_info_sailor()

get_sailor()

