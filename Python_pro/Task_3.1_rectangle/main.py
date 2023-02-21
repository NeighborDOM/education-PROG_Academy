# Создайте класс «Прямоугольник», у которого присутствуют два поля
# (ширина и высота). Реализуйте метод сравнения прямоугольников по
# площади. Также реализуйте методы сложения прямоугольников (площадь
# суммарного прямоугольника должна быть равна сумме площадей
# прямоугольников, которые вы складываете). Реализуйте методы
# умножения прямоугольника на число n (это должно увеличить площадь
# базового прямоугольника в n раз).

class Rectangle:

    def __init__(self, w: int | float, h: int | float):
        if not isinstance(w, (int | float)) and (h, (int | float)):
            raise TypeError
        if w == 0 or h == 0:
            raise ValueError

        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __add__(self, other):
        return Rectangle(self.w + other.w, self.h + other.h)

    def __mul__(self, other: int | float):
        return f'Width = {self.w * other}, height {self.h * other}'

    def __str__(self):
        return f'Width = {self.w}, height = {self.h}'


x_1 = Rectangle(2, 3)
x_2 = Rectangle(3, 4)

print (x_1 > x_2)

rectangles = [x_1, x_2]
print(min(rectangles))
print(max(rectangles))

x_3 = x_1 + x_2
print(x_3)

x_1 = x_1 * 2
print(x_1)
