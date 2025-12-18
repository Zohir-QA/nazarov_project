# 1
class Human:
    def __init__(self,  name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def greetings(self):
        print(f"Зовут {self.name}, лет {self.age}, вес {self.weight}, рост {self.height}")

class Builder(Human):
    def __init__(self, experience, injury):
        self.experience = experience
        self.injury = injury



    def foo(self):
        self.greetings()