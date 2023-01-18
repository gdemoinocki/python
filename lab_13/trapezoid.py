from . import base
class Trapezoid(base.BaseClass):


    def __init__(self,func, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        if func == 1:
            self.area()
        elif func == 2:
            self.c_circle()
        else:
            self.i_circle()

    def area(self):
        return round((self.h * (self.a + self.b)) / 2, 2)

    def c_circle(self):
        return round((self.a + self.b + self.c) / 4 * self.area(), 2)

    def i_circle(self):
        return round(self.h/2, 2)
