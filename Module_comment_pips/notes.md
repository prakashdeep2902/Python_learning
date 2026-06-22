# Python Basics - Beginner Notes

## 1. First Code in Python

### Hello World Program

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

### Explanation

- `print()` is a built-in Python function.
- It displays data on the screen.
- Anything inside quotes (`" "`) is considered a string (text).

### More Examples

```python
print("My name is Prakash")
print(25)
print(True)
```

### Output

```text
My name is Prakash
25
True
```

---

# 2. Modules

## What is a Module?

A **module** is a Python file containing functions, variables, and classes that can be reused in other programs.

Think of it like a toolbox.

### Example

```python
import math

print(math.sqrt(25))
```

### Output

```text
5.0
```

### Why Use Modules?

- Reusability
- Organized code
- Saves time
- Easier maintenance

---

# 3. PIP

## What is PIP?

**PIP = Pip Installs Packages**

It is Python's package manager.

It helps us install external libraries/modules.

### Check PIP Version

```bash
pip --version
```

### Install a Package

```bash
pip install pyjokes
```

### Use Installed Package

```python
import pyjokes

print(pyjokes.get_joke())
```

### Example Output

```text
Why do programmers prefer dark mode? Because light attracts bugs!
```

## Useful PIP Commands

### Install Package

```bash
pip install requests
```

### Uninstall Package

```bash
pip uninstall requests
```

### See Installed Packages

```bash
pip list
```

### Upgrade Package

```bash
pip install --upgrade requests
```

---

# 4. Types of Modules

Python modules are mainly of **3 types**.

## Type 1: Built-in Modules

Already available with Python.

No installation required.

### Examples

- math
- random
- datetime
- os

### Example

```python
import random

print(random.randint(1, 10))
```

### Output

```text
7
```

---

## Type 2: User-Defined Modules

Modules created by the programmer.

### Create File: my_module.py

```python
def greet(name):
    return f"Hello {name}"
```

### Use Module in main.py

```python
import my_module

print(my_module.greet("Prakash"))
```

### Output

```text
Hello Prakash
```

---

## Type 3: Third-Party Modules

Created by other developers.

Installed using PIP.

### Examples

- numpy
- pandas
- requests
- pyjokes
- flask
- django

### Example

```python
import pyjokes

print(pyjokes.get_joke())
```

---

# Python as a Calculator

Python can work like a calculator directly in the terminal.

## Start Python

```bash
py
```

or

```bash
python
```

You will see:

```text
>>>
```

## Perform Calculations

```python
>>> 10 + 5
15

>>> 20 - 8
12

>>> 6 * 7
42

>>> 25 / 5
5.0

>>> 2 ** 4
16

>>> 10 % 3
1
```

---

## Using Math Module

```python
>>> import math

>>> math.sqrt(64)
8.0

>>> math.factorial(5)
120

>>> math.pi
3.141592653589793
```

---

## One-Line Calculator Command

```bash
py -c "print(10 + 20)"
```

### Output

```text
30
```

### Another Example

```bash
py -c "print(2**10)"
```

### Output

```text
1024
```

---

## Useful Operators

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| +        | Addition       | 5 + 3    |
| -        | Subtraction    | 5 - 3    |
| \*       | Multiplication | 5 \* 3   |
| /        | Division       | 10 / 2   |
| //       | Floor Division | 10 // 3  |
| %        | Modulus        | 10 % 3   |
| \*\*     | Power          | 2 \*\* 3 |

---

# Quick Revision

| Topic               | Definition                 |
| ------------------- | -------------------------- |
| First Program       | `print("Hello World")`     |
| Module              | Reusable Python file       |
| PIP                 | Package manager for Python |
| Built-in Module     | Comes with Python          |
| User-Defined Module | Created by programmer      |
| Third-Party Module  | Installed using PIP        |

---

# Practice Questions

## Q1

Print your name and age.

```python
print("Prakash")
print(22)
```

## Q2

Use the math module to find the square root of 64.

```python
import math

print(math.sqrt(64))
```

## Q3

Install pyjokes and print a joke.

```bash
pip install pyjokes
```

```python
import pyjokes

print(pyjokes.get_joke())
```

## Q4

Name the three types of modules.

### Answer

1. Built-in Modules
2. User-Defined Modules
3. Third-Party Modules

```

```

# Comments in Python (Short Notes)

### What are Comments?

Comments are used to explain code. Python ignores them during execution.

---

### 1. Single-Line Comment

```python
# This is a comment
print("Hello")
```

---

### 2. Inline Comment

```python
age = 22  # User age
```

---

### 3. Multi-Line Comment

```python
# Line 1
# Line 2
# Line 3
```

or

```python
"""
Multi-line comment
"""
```

---

### Output Example

```python
# Print a message
print("Hello World")
```

**Output:**

```text
Hello World
```

---

### Quick Revision

| Type        | Syntax             |
| ----------- | ------------------ |
| Single-Line | `# Comment`        |
| Inline      | `x = 10 # Comment` |
| Multi-Line  | `""" Comment """`  |

📌 **Remember:** Comments are for humans, not for Python.
