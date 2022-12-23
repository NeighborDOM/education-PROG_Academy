"""
1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.
"""

print("hg1jbbkrk2brkbr3iierb4".count("b"))

"""
2. Користувач вводить з клавіатури ім'я людини.
Написати програму для перевірки введеного ім'я на валідність
(мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери,
за якою повинні йти маленькі).
"""

name = (input("Enter a name: "))
match name:
    case name if name.isalpha() and name.istitle():
        print(name)
    case _:
        print("ERROR")

"""
3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.
"""

text = input("Enter a word or phrase: ")
summa = 0
k = 0
for i in range(len(text)):
    k = ord(text[i])
    summa += k
print(summa)

""" 
4. Виведіть на екран 10 рядків із значенням числа Pi.
У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
"""

import math

for i in range(3, 12):
    print(f' pi = {math.pi:.{i}}')

'''
5. Вводиться з клавіатури користувачем текст.
Знайти в ньому найдовше слово та вивести його на екран.
'''

text = input("Enter text: ")

long_text = text.split()
x = " "

for word in long_text:
    if len(word) > len(x):
        x = word
print(f'Longest word:{x}')
