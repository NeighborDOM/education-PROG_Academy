"""
1. Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.
"""

class_list = []


def add_str(cls):
    def dec_list(*args, **kwargs):
        res = cls(*args, **kwargs)
        class_list.append(cls)
        return res

    return dec_list


@add_str
class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


@add_str
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


x_1 = Student('Ivan', 'Ivanov1')
print(x_1)

box_1 = Box(1, 2, 3)
print(box_1)

print(class_list)

"""
2. Создайте декоратор класса с параметром. Параметром должна быть строка, 
которая должна дописываться (слева) к результату работы метода __str__.
"""


def decor_class(text):
    def decorator(cls):
        def inner(*args, **kwargs):
            return text + " " + str(cls(*args, **kwargs))

        return inner

    return decorator


@decor_class("Hello, world and ")
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


x_1 = Student('Ivan', 'Ivanov1')
print(x_1)

"""
3. Для класса Box напишите статический метод, 
который будет подсчитывать суммарный объём двух ящиков, которые будут его параметрами.
"""


class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        volume = self.a * self.b * self.c
        return volume

    @staticmethod
    def sum_volume(sum_v1, sum_v2):
        sum_v1 = Box.volume(sum_v1)
        sum_v2 = Box.volume(sum_v2)
        return sum_v1 + sum_v2

    def __str__(self):
        return f'a = {self.a}, b = {self.b}, c = {self.c}'


box_1 = Box(1, 2, 3)
box_2 = Box(2, 4, 6)
print(Box.sum_volume(box_1, box_2))
