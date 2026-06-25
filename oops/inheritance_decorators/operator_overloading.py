class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num + other.num


n = Number(1)
m = Number(2)

print(n + m)
print(n * m)


# vector
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y}) prakash"

    def __len__(self):
        return self.x


v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1)
print(v2)

print(v1 + v2)
