If you're learning Python OOPs (Object-Oriented Programming), you should understand the concepts in this order:

# 1. What is OOP?

**Definition:**
Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **objects** and **classes**.

It helps in:

- Code reusability
- Modularity
- Maintainability
- Real-world modeling

Example:

```python
car1 = {
    "brand": "BMW",
    "color": "Black"
}
```

Instead of creating many dictionaries, we use classes.

---

# 2. Class

**Definition:**
A class is a blueprint/template used to create objects.

Syntax:

```python
class Student:
    pass
```

Example:

```python
class Student:
    name = "Prakash"

print(Student.name)
```

Output:

```python
Prakash
```

---

# 3. Object

**Definition:**
An object is an instance of a class.

Example:

```python
class Student:
    name = "Prakash"

s1 = Student()
s2 = Student()

print(s1.name)
print(s2.name)
```

Output:

```python
Prakash
Prakash
```

---

# 4. Attributes

Attributes are variables inside a class.

### Class Attribute

Shared among all objects.

```python
class Employee:
    company = "Google"

e1 = Employee()
e2 = Employee()

print(e1.company)
print(e2.company)
```

---

### Instance Attribute

Unique for every object.

```python
class Employee:
    company = "Google"

e1 = Employee()
e1.name = "Prakash"

e2 = Employee()
e2.name = "Rahul"

print(e1.name)
print(e2.name)
```

---

# 5. Methods

**Definition:**
Functions defined inside a class are called methods.

```python
class Employee:

    def greet(self):
        print("Good Morning")

e1 = Employee()
e1.greet()
```

Output:

```python
Good Morning
```

---

# 6. self Keyword

**Definition:**
`self` refers to the current object.

Python automatically passes the object as the first argument.

Example:

```python
class Employee:

    def greet(self):
        print("Hello")

e1 = Employee()
e1.greet()
```

Actually Python executes:

```python
Employee.greet(e1)
```

---

## Why self is needed?

Without self:

```python
class Employee:

    def greet():
        print("Hello")

e1 = Employee()
e1.greet()
```

Error:

```python
TypeError
```

---

# 7. Accessing Object Variables Using self

```python
class Employee:

    def show(self):
        print(self.name)

e1 = Employee()
e1.name = "Prakash"

e1.show()
```

Output:

```python
Prakash
```

---

# 8. Constructor (**init**)

## Definition

A constructor is a special method that runs automatically whenever an object is created.

Python Constructor:

```python
__init__()
```

---

## Syntax

```python
class Employee:

    def __init__(self):
        print("Constructor called")
```

```python
e1 = Employee()
```

Output:

```python
Constructor called
```

---

# 9. Parameterized Constructor

Constructor that accepts arguments.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Prakash", 50000)

print(e1.name)
print(e1.salary)
```

Output:

```python
Prakash
50000
```

---

# 10. Constructor with Default Values

```python
class Employee:

    def __init__(self, name, salary=10000):
        self.name = name
        self.salary = salary

e1 = Employee("Prakash")

print(e1.salary)
```

Output:

```python
10000
```

---

# 11. Multiple Objects Using Constructor

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Prakash", 50000)
e2 = Employee("Rahul", 70000)

print(e1.name)
print(e2.name)
```

Output:

```python
Prakash
Rahul
```

---

# 12. Constructor vs Method

| Constructor                   | Method               |
| ----------------------------- | -------------------- |
| Automatically called          | Manually called      |
| Name fixed (`__init__`)       | Any name             |
| Used for initialization       | Used for actions     |
| Runs once per object creation | Runs whenever called |

Example:

```python
class Employee:

    def __init__(self):
        print("Constructor")

    def show(self):
        print("Method")

e1 = Employee()
e1.show()
```

Output:

```python
Constructor
Method
```

---

# 13. Real-World Example

```python
class Train:

    def __init__(self, seats, fare):
        self.seats = seats
        self.fare = fare

    def get_status(self):
        print(f"Seats Available: {self.seats}")

    def get_fare(self):
        print(f"Fare: {self.fare}")

railway = Train(400, 2500)

railway.get_status()
railway.get_fare()
```

Output:

```python
Seats Available: 400
Fare: 2500
```

---

# Common Interview Questions (Theory)

### Q1. What is OOP?

Programming paradigm based on classes and objects.

### Q2. Difference between Class and Object?

| Class          | Object          |
| -------------- | --------------- |
| Blueprint      | Instance        |
| Logical entity | Physical entity |

---

### Q3. What is self?

Reference to the current object.

---

### Q4. What is a constructor?

Special method automatically executed during object creation.

---

### Q5. Can a class have multiple constructors in Python?

No. Python doesn't support constructor overloading directly.

```python
class Test:
    def __init__(self, x=None):
        self.x = x
```

---

# 5 Important Interview Coding Questions

## Question 1: Student Class

Create a class `Student` with:

- name
- marks

Constructor initializes both.

Method:

```python
display()
```

Output:

```python
Name: Prakash
Marks: 90
```

---

## Question 2: Rectangle Class

Create a class `Rectangle`.

Constructor:

```python
length
width
```

Methods:

```python
area()
perimeter()
```

---

## Question 3: BankAccount Class

Constructor:

```python
account_holder
balance
```

Methods:

```python
deposit(amount)
withdraw(amount)
show_balance()
```

---

## Question 4: Employee Class

Constructor:

```python
name
salary
```

Method:

```python
annual_salary()
```

Return:

```python
salary * 12
```

---

## Question 5: Train Reservation Class

Constructor:

```python
total_seats
fare
```

Methods:

```python
book_ticket()
cancel_ticket()
get_status()
```

Update seats accordingly.

---

# Quick Revision Notes

```text
OOP      -> Programming using classes and objects

Class    -> Blueprint

Object   -> Instance of class

Attribute-> Variables inside class

Method   -> Functions inside class

self     -> Current object reference

__init__ -> Constructor

Class Attribute
    Shared by all objects

Instance Attribute
    Unique for each object

Constructor
    Runs automatically when object is created

Parameterized Constructor
    Accepts values during object creation
```

Master these topics first. After this, the next OOP topics are:

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction
5. Class Methods
6. Static Methods
7. Magic/Dunder Methods
8. Property Decorators
9. Method Resolution Order (MRO)
10. Multiple Inheritance

These are the topics most frequently asked in Python interviews after constructors.
