class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = ((value / self.salary) - 1) * 100


emp = Employee(233, 10)
emp.salaryAfterIncrement = 280
print(emp.increment)
print(emp.salaryAfterIncrement)
