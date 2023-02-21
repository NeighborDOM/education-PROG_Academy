"""
1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
закон якої задається за допомогою функції користувача.
 Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів,
 що видаються послідовностю.
 Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
"""
import timeit


def user_progression(item):
    if item % 2:
        return item + 1
    return item + 2


def generator_func(start, stop, func):
    """
    :param start:
    :param stop:
    :param func:
    :return:
    """
    while start < stop:
        yield start
        start = func(start)


for item in generator_func(2, 100, user_progression):
    print(item)


# Варіант 2

class A:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        while self.start < self.stop:
            yield self.start
            self.start += self.start


x = A(1, 100)
for item in x:
    print(item)

"""
2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація.
Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
 Порівняйте швидкість виконання із просто рекурсивним підходом.
"""
import timeit

s_1 = """
def fibonachi():
    first_number = 0
    second_number = 1

    def get_next():
        nonlocal first_number
        nonlocal second_number
        next_number = second_number + first_number
        first_number = second_number
        second_number = next_number
        return next_number

    return get_next


f = fibonachi()
for i in range(100):
    (f())
"""

s_2 = """
def recur_fibo(n):
    if n <= 1:
        return 1
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


for i in range(100):
    recur_fibo(1)
"""

print(timeit.timeit(s_1, number=20))
print(timeit.timeit(s_2, number=20))

"""
3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача 
і поверне суми елементів отриманого списку.
"""
a = [1, 2, 4, 5, 7, 8]


def custom_function(n):
    return item ** 2


def new_function(custom_list, custom_function):
    result = []
    for element in custom_list:
        result.append(custom_function(element))
    return sum(result)


x = new_function(a, custom_function)
print(x)

# Вариант 2

import random


def user_func(item):
    return item ** 3


def func(x, func):
    return sum(func(item) for item in x)


x = [random.randint(1, 100) for _ in range(10)]
print(x)
print(func(x, user_func))
print(x)
