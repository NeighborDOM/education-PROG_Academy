"""
1. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
які є одночасно і в першому, і в другому рядку.
Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».
"""

text_1 = input()
text_2 = input()
set_1 = set(text_1)
set_2 = set(text_2)

print(set_1 & set_2)

"""
2. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.
"""

list_one = []
list_two = []

for x in range(1, 100):
    if x % 3 == 0:
        list_one.append(x)
print(list_one)

for y in range(1, 100):
    if y % 5 == 0:
        list_two.append(y)
print(list_two)

"""
3. Створіть список із числами, які є в обох списках.
Напишіть функцію, яка поверне максимальне число зі списку чисел.
"""

list_one = input()
list_two = input()

set_one = set(list_one)
set_two = set(list_two)
set_three = (set_one & set_two)
list_three = list(set_three)
print(list_three)


def list_max(list_three):
    return max(list_three)


print("Max number in the list: ", max(list_three))

"""
4. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.
"""


def summa(a, b, c):
    x = a + b
    y = c + str(x)
    return y


print(summa(1, 2, "DOM"))

"""
5. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.
"""


def rectangle(a, b):
    print("*" * a)
    for i in range(b):
        print("*" * b)


rectangle(5, 5)

"""
6. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
"""


def number(list, element):
    if element in list:
        y = list.index(element)
        return y
    else:
        y = -1
        return y


list = [1, 2, 3, 4, 5, 3]
element = 3
print(number(list, element))

"""
7. Напишіть функцію, яка поверне кількість слів у текстовому рядку.
"""


def words(a):
    b = a.split()
    return len(b)


a = input(" ")
print(words(a))
