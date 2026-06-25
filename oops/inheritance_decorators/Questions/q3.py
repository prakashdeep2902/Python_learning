# getter and setter in class


class Employee:
    def __init__(self, salary):
        self._salary = salary

    # get salary using @property
    @property
    def get_salary(self):
        return self._salary

    # set salary
    @get_salary.setter
    def set_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        else:
            self._salary = value


employee = Employee(30000)

print(employee.get_salary)

employee.set_salary = 50000

print(employee.get_salary)
