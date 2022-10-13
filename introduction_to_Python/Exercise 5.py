"""
Write a program that reads in the radius of a circle and prints the
circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
Do these calculations in output statements.
"""

r = float(input("r = "))
d = r * 2
print(f"d= {d}")
l = 2 * 3.14159*r
print(f"l= {l}")
s = 3.14159*r**2
print(f"s= {s}")

