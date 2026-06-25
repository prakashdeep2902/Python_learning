# inharitance
class Company:
    numberOfEmployee = 12000
    Name = "ITC"
    Islegal = True


class User:
    name = "Prakash Deep Sharma"
    age = 27
    working = False
    Hight = "6ft"


class Employee(Company, User):

    def getInfo(self):
        return {
            "User": {
                "Name": self.name,
                "age": self.age,
                "Hight": self.Hight,
            },
            "company": {"name": self.Name, "no_of_Employees": self.numberOfEmployee},
        }


e = Employee()
print(e.getInfo())


# super() calls methods from the parent class.


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll


s = Student("Prakash", 101)

print(s.name)


# understanding decortor propely

# A decorator is a function that adds or modifies the behavior of another
# function without changing its original code.


def log(fun):
    def otherFun():
        print("what is your name")
        fun()
        print("ohh, I see")

    return otherFun


@log
def prinName():
    print("Prakash")


prinName()


# classmethod decotrateor


class Person:

    name = "prakash"

    @classmethod
    def show(self):
        print(f"This is {self.name}")


user = Person()

user.name = "vikash"

print(user.show())


class User:

    details = {"name": "prakash", "age": 27, "work": True}

    @property
    def sending_details(self):
        return self.details


user = User()
print("Details of Users: ", user.sending_details)

name = user.sending_details["age"]

print("name::::==>", type(name))
