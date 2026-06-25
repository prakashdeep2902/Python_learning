class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j + {self.k}k")


Two_D = TwoDVector(1, 2)
Two_D.show()
Three_D = ThreeDVector(1, 2, 3)
Three_D.show()
