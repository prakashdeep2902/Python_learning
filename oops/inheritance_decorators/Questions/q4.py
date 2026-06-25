class Complex:

    def __init__(self, real, imgi):
        self.real = real
        self.imgi = imgi

    def __add__(self, other):
        return Complex(self.real + other.real, self.imgi + other.imgi)

    def __str__(self):
        return f"({self.real},{self.imgi})"


c1 = Complex(1, 2)
c2 = Complex(3, 3)

print(c1 + c2)
