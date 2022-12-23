"""
1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
Наприклад, 1 - "Monday".
"""

dict_days = {"1": "Monday",
             "2": "Tuesday",
             "3": "Wednesday",
             "4": "Thursday",
             "5": "Friday",
             "6": "Saturday",
             "7": "Sunday"}
# Method 1
for num, day in dict_days.items():
    print(f'{num.title()} - {day.title()}')

# Method 2
for day in dict_days:
    print(day, "-", dict_days.get(day))

"""
2. Опишіть кота (домашня тварина) на основі словника.
"""

dict_cat = {"Name": "",
            "Date of birth": "",
            "Breed": "",
            "Colour": "",
            "Age": "",
            "Cost type": "",
            "Distinctive marks": ""}
print("Description of cat:")
for key in dict_cat:
    print(key)
    dict_cat[key] = input(f'{""}')
    print(dict_cat)
for description in dict_cat:
    print(description, ":", dict_cat[description])

'''
3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
скільки разів яка літера зустрічається в цьому рядку.
Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.
'''

text = input('')
dict_text = {}

for char in text:
    if not dict_text.get(char):
        dict_text[char] = text.count(char)

print(dict_text)


