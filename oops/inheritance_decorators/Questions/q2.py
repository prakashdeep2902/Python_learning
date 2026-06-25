class Animal:
    def __init__(self, tail, leg):
        self.tail = tail
        self.leg = leg
        print(f"In parent legs are {self.leg}")


class Pet(Animal):
    def __init__(self, tail, leg):
        super().__init__(tail, leg)


class Dog(Pet):
    def __init__(self, tail, leg, name, sound):
        super().__init__(tail, leg)
        self.name = name
        self.sound = sound

    def bark(self):
        return f"Dog with name {self.name} having {self.tail} tail and {self.leg} legs says {self.sound}"


dog = Dog(1, 4, "rocky", "bhu---bhu")

print(dog.bark())
