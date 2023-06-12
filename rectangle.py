# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def getWidth(self):
#         return self.width
#     def getHeight(self):
#         return self.height
#     def getArea(self):
#         return self.width * self.height

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_area(self):
#         return self.a * self.b
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#     def get_area_square(self):
#         return self.a ** 2
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def get_area_circle(self):
#         return 3.14 * self.r ** 2

# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'

# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'
#     def get_area(self):
#         return self.width * self.height

class Customers:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"'{self.first_name}, {self.last_name}'. {self.city}. Баланс: {self.balance} руб."
    def get_guest(self):
        return f"{self.first_name} {self.last_name}, г. {self.city}"
