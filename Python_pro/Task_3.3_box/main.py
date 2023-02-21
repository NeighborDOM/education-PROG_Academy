class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __ne__(self, other):
        return self.volume() != other.volume()

    def __add__(self, other):
        if isinstance(other, Box):
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, tuple) and len(other) == 3:
            x, y, z = other
            if isinstance(x, int | float) and isinstance(y, int | float) and isinstance(z, int | float):
                return Box(self.x + x, self.y + y, self.z + z)

        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Box):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        return NotImplemented

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


x_1 = Box(12, 2, 0.3)
x_2 = Box(10, 1, 6)
x_3 = Box(1.0, 20, 3)
x_4 = Box(12, 2, 1.5)
x_5 = Box(0.5, 20, 30)
x_6 = Box(10, 20, 30)

boxes = [x_1, x_2, x_3, x_4, x_5, x_6]
print(min(boxes))
print(max(boxes))
print(list(map(str, sorted(boxes))))

x_7 = x_1 + x_2
print(x_7)

x_8 = x_1 + (5, 3, 2)
print(x_8)

x_1 += x_2
print(x_1)
