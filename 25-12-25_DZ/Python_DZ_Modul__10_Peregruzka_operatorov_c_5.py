# 1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __add__(self, other):
#         return Circle(self.radius + other.radius)
#
#     def __sub__(self, other):
#         return Circle(self.radius - other.radius)
#
#     def __isub__(self, other):
#         self.radius -= other.radius
#         return self
#
#     def __iadd__(self, other):
#         self.radius += other.radius
#         return self
#
#     def get_circle_radius(self):
#         return f"Радиус окружности = {self.radius}"
#
# c1 = Circle(5)
# c2 = Circle(7)
# c3 = Circle(5)
# print(c1 == c3) # True (радиусы равны)
# print(c1 == c2) # False (радиусы разные)
# print(c1 < c2)  # True
# print(c1 > c2)  # False
# print(c1 <= c3) # True
# print(c2 >= c3) # True
# c4 = c1 + c2
# print(c4.radius)

# 2
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
#
#     def __mul__(self, other):
#         real = self.real * other.real - self.imag * other.imag
#         imag = self.real * other.imag + self.imag * other.real
#         return Complex(real, imag)
#
#     def __truediv__(self, other):
#         denom = other.real ** 2 + other.imag ** 2
#         return Complex(
#             (self.real * other.real + self.imag * other.imag) / denom,
#             (self.imag * other.real - self.real * other.imag) / denom
#         )
#
# comp_1 = Complex(real=5,imag=10)
# comp_2 = Complex(real=2,imag=3)
#
# print(comp_1.__add__(comp_2).__dict__)
# print(comp_1.__sub__(comp_2).__dict__)
# print(comp_1.__mul__(comp_2).__dict__)
# print(comp_1.__truediv__(comp_2).__dict__)

# 3
# class Airplane:
#     def __init__(self, plane_type, current_passengers):
#        self.plane_type = plane_type
#        self.current_passengers = current_passengers
#
#     def __eq__(self, other):
#        return self.plane_type == other.plane_type
#
#     def __add__(self, other):
#         return self.current_passengers + other.current_passengers
#
#     def __sub__(self, other):
#         return self.current_passengers - other.current_passengers
#
#     def __isub__(self, other):
#         self.current_passengers -= other.current_passengers
#         return self
#
#     def __iadd__(self, other):
#         self.current_passengers += other.current_passengers
#         return self
#
#     def __lt__(self, other):
#         return self.current_passengers < other.current_passengers
#
#     def __gt__(self, other):
#         return self.current_passengers > other.current_passengers
#
#     def __ge__(self, other):
#         return self.current_passengers >= other.current_passengers
#
#     def __le__(self, other):
#         return self.current_passengers <= other.current_passengers
#
# c1 = Airplane("Boeing 737", current_passengers=120)
# c2 = Airplane("Boeing 737", current_passengers=50)
#
# print(c1.__eq__(c2))
# print(c1.__sub__(c2))
# print(c1.__ge__(c2))

# 4
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area * self.price > other.area * other.price

    def __lt__(self, other):
        return self.area * self.price < other.area * other.price

    def __ge__(self, other):
        return self.area * self.price >= other.area * other.price

    def __le__(self, other):
        return self.area * self.price <= other.area * other.price

flat_1 = Flat(area=10, price=30)
flat_2 = Flat(area=20, price=50)

print(flat_1.__eq__(flat_2))
print(flat_1.__ne__(flat_2))
print(flat_1.__ge__(flat_2))
print(flat_1.__le__(flat_2))