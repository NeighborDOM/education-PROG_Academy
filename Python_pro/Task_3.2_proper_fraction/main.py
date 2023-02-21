# Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.

class Fraction:

    def __init__(self, num: int, denom: int):
        self.num = num
        self.denom = denom

    def __gt__(self, other):
        return self.num / self.denom > other.num / other.denom

    def __lt__(self, other):
        return self.num / self.denom < other.num / other.denom

    def __ge__(self, other):
        return self.num / self.denom >= other.num / other.denom

    def __le__(self, other):
        return self.num / self.denom <= other.num / other.denom

    def __eq__(self, other):
        return self.num / self.denom == other.num / other.denom

    def __ne__(self, other):
        return self.num / self.denom != other.num / other.denom

    def __add__(self, other):
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __str__(self):
        if self.num < self.denom:
            return f'Proper fraction {self.num} / {self.denom}'
        elif self.num > self.denom:
            return f'Improper fraction {self.num} / {self.denom}'
        else:
            return ZeroDivisionError


fr_1 = 1, 5
fr_2 = 1, 4

print(fr_1 > fr_2)
