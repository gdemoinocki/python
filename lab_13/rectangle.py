from . import base
import math


class Rectangle(base.BaseClass):

    def __init__(self, fu, a, b):
        self.a = a
        self.b = b
        self.res = ''
        if fu == 1:
            self.area()

    def area(self):
        self.res = round(self.a * self.b, 2)
        return str(self.res)

    def c_circle(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2) / 2, 2)

    def i_circle(self):
        if self.a == self.b:
            return round(self.a / 2)
        return 'окружность не вписывается в прямоугольник'

    def __str__(self):
        return str(self.res)

if __name__ == "__main__":
    print(Rectangle(float(1), float(2), float(3)))

