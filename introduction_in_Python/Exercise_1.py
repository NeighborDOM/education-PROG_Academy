# 1
# Write a Python-script that displays the message “Hello world”.

print('Hello, World!')

# 2
# Rewrite the first script to display three any messages.

x = 'some long text \nand new string \nand new line'
print(x)

# 3
# Write a Python-script to reads values for the length and width of a
# rectangle and returns the area of the rectangle.

a = float(input("Width\n"))
b = float(input("Length?\n"))
x = a * b
print(x)

# 4
# Write a program that requests the user to enter two numbers and
# prints the sum, product, difference and quotient of the two numbers.

a = float(input("Number 1\n"))
b = float(input("Number 2\n"))
x = a + b
print(x)
x = a * b
print(x)
x = a - b
print(x)
x = a / b
print(x)

# 5
# Write a program that reads in the radius of a circle and prints the
# circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.

r = float(input("r = "))
d = r * 2
print(f"d= {d}")
l = 2 * 3.14159 * r
print(f"l= {l}")
s = 3.14159 * r ** 2
print(f"s= {s}")
