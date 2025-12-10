# 1
class Car:
    def __init__(self):
        self._model = ""
        self._year = 0
        self._manufacturer = ""
        self._engine_volume = 0
        self._color = ""
        self._price = 0

    def input_data(self):
        self._model = input("Введите название модели: ")
        self._year = int(input("Введите год выпуска: "))
        self._manufacturer = input("Введите производителя: ")
        self._engine_volume = input("Введите объем двигателя (л): ")
        self._color = input("Введите цвет машины: ")
        self._price = input("Введите цену: ")

    def output_data(self):
        print(f"Модель: {self._model}")
        print(f"Год выпуска: {self._year}")
        print(f"Производитель: {self._manufacturer}")
        print(f"Объем двигателя: {self._engine_volume} л")
        print(f"Цвет: {self._color}")
        print(f"Цена: {self._price:.2f}")
# 2

# 3
