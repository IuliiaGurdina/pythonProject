# from rectangle import Rectangle, Square, Circle
#
# rect_1 = Rectangle(3, 4)
# rect_2 = Rectangle(12, 5)
#
# print(rect_1.get_area())
# print(rect_2.get_area())
#
# square_1 = Square(5)
# square_2 = Square(10)
#
# print(square_1.get_area_square(), square_2.get_area_square())
#
# circle_1 = Circle(6)
#
# print(circle_1.get_area_circle())
# figures = [rect_1, rect_2, square_1, square_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     else:
#         print(figure.get_area())

# from rectangle import Rectangle
# rectangle_1 = Rectangle(5, 10, 50, 100)
# print(rectangle_1)

# from rectangle import Rectangle
# rect_1 = Rectangle(5, 10, 50, 100)
# print(rect_1)
# print(rect_1.get_area())

from rectangle import Customers
customer_1 = Customers("Петр", "Иванов", "Москва", 50)
customer_2 = Customers("Владимир", "Зайцев", "Нижний Новгород", 45)
customer_3 = Customers("Людмила", "Боярова", "Тула", 48)
guest_list = [customer_1, customer_2, customer_3]
for guest in guest_list:
    print(guest.get_guest())