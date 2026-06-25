# bank Account (valiation + read-only propety)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def showBalance(self):
        return f"Account balance is :{self._balance}"

    @property
    def is_rich(self):
        if self._balance >= 1000000:
            return True
        else:
            return False

    @showBalance.setter
    def set_balance(self, value):
        if value < 0:
            raise ValueError("Money can't come in negative number")
        else:
            self._balance = self._balance + value


acc = BankAccount(30000)

acc.set_balance = 20000000
print(acc.showBalance)
print(acc.is_rich)


# Employee Name (Computed Property)


class Employee:

    _f_name = ""
    _l_name = ""

    @property
    def get_first_name(self):
        return f"FirstName: {self._f_name}"

    @property
    def get_last_name(self):
        return f"LastName: {self._l_name}"

    @property
    def get_full_name(self):
        return f"FullName:{self._f_name} {self._l_name}"

    @get_full_name.setter
    def set_full_name(self, value):
        if value == "":
            raise ValueError("full name not be blank")
        else:
            new_value = value.split(" ")
            self._f_name = new_value[0]
            self._l_name = new_value[1]

    @get_full_name.deleter
    def get_full_name(self):
        self._f_name = ""
        self._l_name = ""


e = Employee()
e.set_full_name = "Vikash Sharma"

print(e.get_full_name)
print(e.get_first_name)
print(e.get_last_name)
del e.get_full_name
print(e.get_full_name)
