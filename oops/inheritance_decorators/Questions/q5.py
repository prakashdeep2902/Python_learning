class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._y)

    def __str__(self):
        return f"({self._x} , {self._y})"


v1 = Vector(1, 2)
v2 = Vector(2, 3)

print(v1 + v2)
print(v1, v2)
