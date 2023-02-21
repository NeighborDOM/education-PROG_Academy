import re
"""
1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
"""
match = input()
match = re.finditer(r'Rb+r', match)
for a in match:
    print(a[0])
else:
    print("Not found")

"""
2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999)
"""
credit_card = input()
pattern = r"^(\d{4}[- ]){3}\d{4}$"
match = re.search(pattern, credit_card)
if match:
    print("Correct")
else:
    print("Incorrect")

"""
3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
Вимоги:
-Цифри (0-9).
-лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
-у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
-Символ "-" не може повторюватися.
"""

email = input()
pattern = r'^[\w\d_.]+(-?[\w\d])+@[\w\d-]+(?:\.[a-zA-Z0-9-]+)*$'

match = re.search(pattern, email)
if match:
    print(match.group())
else:
    print("The email is incorrect")

"""
4. Напишіть функцію, яка перевіряє правильність логіну.
Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.
"""
login_string = input()
pattern = '^[a-zA-Z0-9_]{2,10}$'
login_string = re.search(pattern, login_string)
if login_string:
    print(login_string.group())
else:
    print("Incorrect")




