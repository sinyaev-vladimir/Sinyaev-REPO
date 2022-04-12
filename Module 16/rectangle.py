class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return 3.14 * self.r ** 2

class Triangle:
    def __init__(self, x, h):
        self.x = x
        self.h = h

    def get_area_triangle(self):
        return (self.x * self.h) / 2

    # метод для возвращения параметров фигуры в строку
    def get_triangle_args(self):
        return (f"длина гипотенузы: {self.x}, высота треугольника: {self.h}")