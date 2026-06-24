# write a class calculator for finding squre,cube,square root


class calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def square(a):
        return a * a

    @staticmethod
    def cube(a):
        return a * a * a

    @staticmethod
    def squreRoot(a):
        return a**0.5


cal = calculator()

print(int(cal.add(12, 29)))
print(int(cal.square(5)))
print(int(cal.cube(5)))
print(int(cal.squreRoot(5)))
