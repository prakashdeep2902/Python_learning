class Employee:
    language = "python"  # these are class attributes
    age: 25
    salary = 1200000


prakash = Employee()

prakash.name = "Prakash"  # this is object attributes
print(prakash.name, prakash.language)


# self


class User:
    name = "vikash"
    age = 25
    salary = 1200000

    def getInfo(self):
        return f"name of user is {self.name} age is {self.age} and salary {self.salary}"

    @staticmethod
    def greet():
        print("Hello this is prakash")


emp = User()

print(emp.getInfo())
print(emp.greet())


# counstroctor


class animal:
    def __init__(self, name, price, bread):
        self.name = name
        self.price = price
        self.bread = bread

    def greet(self):
        return f"The Dog name is {self.name} price is {self.price} and breead is {self.bread}"


dog = animal("sheru", 20000, "american pitbut")

print(dog.greet())
