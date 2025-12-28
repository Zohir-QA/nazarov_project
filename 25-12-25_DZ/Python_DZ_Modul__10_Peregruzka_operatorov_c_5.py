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
