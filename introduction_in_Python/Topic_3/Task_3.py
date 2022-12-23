"""
1. Write a Python program to print the number entered by user only if the number entered is negative.
"""

c = []
a = int(input("Enter size of list:"))
for x in range(0, a):
    b = float(input("Enter element of list:"))
    c.append(b)
print("Negative numbers in", c, "are: ")
negative_numbers = list(filter(lambda i: (i < 0), c))
print(negative_numbers)

"""
2. Write a Python program to check if the value a is less than 20 or not.
"""

a = 20
b = float(input('Enter number:'))
print(b, 'is less than 20', b < 20)

"""
3. Write a Python program to check if a given number is Zero or Not.
"""

num = float(input("Enter a number: "))
print(num, "- zero", (num == 0))

"""
4. Write a Python program to check if a given number is Even or Odd.
"""

num = int(input("Enter a number: "))
print("{0} is Even number".format(num), num % 2 == 0) or print("{0} is Odd number".format(num), num % 2 != 0)

"""
5. Write a Python program to find largest number among three numbers entered by user.
"""

a = float(input("First number - "))
b = float(input("Second number - "))
c = float(input("Third number - "))
print(max(a, b, c))
