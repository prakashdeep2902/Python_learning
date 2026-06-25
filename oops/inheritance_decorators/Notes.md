### What is a Decorator?

A **decorator** is a function that adds or modifies the behavior of another function **without changing its original code**.

**Definition:**

> A decorator is a callable that takes a function (or class) as input and returns a modified function (or class).

### Example of a Custom Decorator

```python
def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@logger
def greet():
    print("Hello")

greet()
```

**Output:**

```text
Function is being called
Hello
```

`@logger` adds extra functionality before `greet()` runs.

---

# Built-in Decorators

Python provides some decorators by default.

## 1. `@property`

Used to access a method like an attribute.

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

e = Employee(50000)

print(e.salary)   # No ()
```

Output:

```text
50000
```

---

## 2. `@staticmethod`

Method that doesn't need `self` or class data.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))
```

Output:

```text
5
```

---

## 3. `@classmethod`

Method that works with the class (`cls`) instead of an object (`self`).

```python
class Employee:
    company = "OpenAI"

    @classmethod
    def show_company(cls):
        print(cls.company)

Employee.show_company()
```

Output:

```text
OpenAI
```

### Quick Summary

| Decorator        | Purpose                                 |
| ---------------- | --------------------------------------- |
| `@property`      | Use a method like an attribute          |
| `@staticmethod`  | Method independent of object/class data |
| `@classmethod`   | Method that works with class variables  |
| Custom Decorator | Add extra behavior to functions         |

### Easy Memory Trick

- **`self` → object data → normal method**
- **`cls` → class data → `@classmethod`**
- **No `self` and no `cls` → `@staticmethod`**
- **Method behaves like variable → `@property`**

# Python Inheritance Notes

## What is Inheritance?

Inheritance is a feature in Object-Oriented Programming (OOP) that allows one class (child class) to acquire the properties and methods of another class (parent class).

### Definition

> Inheritance allows code reusability by creating a new class from an existing class.

---

# Why Use Inheritance?

- Code Reusability
- Reduces Duplication
- Easier Maintenance
- Extensible Code Structure
- Creates Parent-Child Relationships

---

# Basic Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

# Single Inheritance

One child class inherits from one parent class.

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()
```

### Output

```
Animal makes a sound
```

---

# Constructor Inheritance

The child class automatically inherits the parent's constructor if it does not define its own.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Prakash")

print(s.name)
```

### Output

```
Prakash
```

---

# Using super()

The `super()` function is used to call methods or constructors of the parent class.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
```

### Why Use super()?

- Calls parent constructor
- Avoids code duplication
- Supports Multiple Inheritance
- Follows Method Resolution Order (MRO)

---

# Method Overriding

A child class can provide its own implementation of a method that already exists in the parent class.

```python
class Animal:
    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()
```

### Output

```
Bark
```

---

# Types of Inheritance

## 1. Single Inheritance

```python
class A:
    pass

class B(A):
    pass
```

---

## 2. Multiple Inheritance

A child inherits from multiple parent classes.

```python
class Father:
    def drive(self):
        print("Driving")

class Mother:
    def cook(self):
        print("Cooking")

class Child(Father, Mother):
    pass
```

---

## 3. Multilevel Inheritance

```python
class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass
```

---

## 4. Hierarchical Inheritance

Multiple child classes inherit from one parent class.

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

---

## 5. Hybrid Inheritance

Combination of multiple inheritance types.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

---

# Method Resolution Order (MRO)

MRO determines the order in which Python searches for methods in inheritance hierarchies.

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
```

### Output

```
C
```

Check MRO:

```python
print(D.mro())
```

Output:

```python
[D, B, C, A, object]
```

---

# isinstance()

Checks whether an object belongs to a class.

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

### Output

```
True
True
```

---

# issubclass()

Checks whether a class inherits from another class.

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))
```

### Output

```
True
```

---

# Real Example

```python
class Animal:
    def __init__(self, legs):
        self.legs = legs

    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    def __init__(self, legs, name):
        super().__init__(legs)
        self.name = name

    def speak(self):
        print("Bark")

dog = Dog(4, "Tommy")

print(dog.name)
print(dog.legs)

dog.speak()
```

### Output

```
Tommy
4
Bark
```

---

# Important Interview Questions

## What is Inheritance?

Inheritance is a mechanism that allows one class to inherit properties and methods from another class.

---

## What is Method Overriding?

Redefining a parent method in the child class.

---

## What is super()?

Used to call parent class methods and constructors.

---

## What is MRO?

Method Resolution Order determines the sequence in which Python searches for methods.

---

## Difference Between Inheritance and Composition?

### Inheritance

```python
class Dog(Animal):
    pass
```

Dog **is an** Animal.

### Composition

```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
```

Car **has an** Engine.

---

# Quick Revision

- Inheritance = Reuse Parent Class Features
- Parent Class = Base/Super Class
- Child Class = Derived/Sub Class
- `super()` = Access Parent Methods
- Overriding = Replace Parent Method
- MRO = Method Search Order
- `isinstance()` = Check Object Type
- `issubclass()` = Check Class Relationship

---

# Memory Trick

```
Inheritance = IS-A Relationship

Dog IS-A Animal
Cat IS-A Animal
Student IS-A Person
```

If one object "IS-A" another object, inheritance is usually the right choice.
