"""
1. Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.
"""

func_count = 0


def function_decorator(func):
    def inner(*args, **kwargs):
        global func_count
        func_count += 1

        return func(*args, **kwargs)

    inner.count = 0
    return inner


@function_decorator
def counter(*args, **kwargs):
    return f"{args} and {kwargs}"


print(counter(1, 2))
print(counter(3, 4))
counter(1, 2)
print("Function called {} times".format(func_count))
"""
2. Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки последовательности.
"""
func_list = []


def function_decorator(func):
    def inner(*args, **kwargs):
        func_list.append(func)
        return func(*args, **kwargs)

    return inner


@function_decorator
def add_list(*args, **kwargs):
    return f"{args} and {kwargs}"


print(add_list(1, 2))
print(add_list(3, 4))
add_list(1, 2)
print(func_list)
"""
3. Предположим, в классе определён метод __str__, который возвращает строку на основании класса.
Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл,
имя которого совпадает с именем класса, метод которого вы декорировали.
"""


def save_file(s):
    def file(f):
        file_name = f.__class__.__name__
        file = open(f'{file_name}.txt', 'w')
        file.write(s(f))
        file.close()
        return (s(f))

    return file


class Student:
    def __init__(self, name, surname, sex, date_of_birth, passport):
        """
        :param name:
        :param surname:
        :param sex:
        :param date_of_birth:
        :param passport:
        """
        self.name = name
        self.surname = surname
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.passport = passport

    @save_file
    def __str__(self):
        return f'name = {self.name}, surname = {self.surname}, ' \
               f'sex = {self.sex}, date_of_birth = {self.date_of_birth}, ' \
               f'passport = {self.passport}'


x_1 = Student('Ivan', 'Ivanov1', 'male', '10.10.1991', 'KM156789')
print(x_1)

