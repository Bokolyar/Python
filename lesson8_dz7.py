class complex():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x} + {self.y}i'
    def __add__(self, other):
        return complex(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        return complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


c1 = complex(2, 3)
c2 = complex(3, 4)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)