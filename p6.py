import math


class Shape:
    def area(self):
        pass


class Square(Shape):                             # area of square -> area=side_length^2
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Triangle(Shape):                           # area = 1/2 * base * height
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Shape):                              # area = pi * radius^2
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


square = Square(5)
triangle = Triangle(4, 6)
circle = Circle(6.5)

square.area()
triangle.area()
circle.area()
