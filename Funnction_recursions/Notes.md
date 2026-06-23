# Functions and Recursion in Python — Complete Guide

---

# 1. What is a Function?

A **function** is a block of reusable code that performs a specific task.

Instead of writing the same code again and again, you write it once inside a function and call it whenever needed.

### Syntax

```python
def function_name():
    # code
```

### Example

```python
def greet():
    print("Hello World")

greet()
```

**Output**

```python
Hello World
```

---

# 2. Why Use Functions?

### Advantages

- Code Reusability
- Better Readability
- Easier Debugging
- Less Code Duplication
- Modular Programming

### Without Function

```python
print("Hello Prakash")
print("Hello Prakash")
print("Hello Prakash")
```

### With Function

```python
def greet():
    print("Hello Prakash")

greet()
greet()
greet()
```

---

# 3. Function with Parameters

Parameters are values received by a function.

```python
def greet(name):
    print("Hello", name)

greet("Prakash")
```

**Output**

```python
Hello Prakash
```

---

# 4. Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

**Output**

```python
30
```

---

# 5. Return Statement

A function can send a value back using `return`.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

**Output**

```python
30
```

---

# 6. Difference Between print() and return

### Using print()

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```python
30
None
```

---

### Using return

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```python
30
```

---

# 7. Default Parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Prakash")
```

Output:

```python
Hello Guest
Hello Prakash
```

---

# 8. Keyword Arguments

```python
def student(name, age):
    print(name, age)

student(age=22, name="Prakash")
```

Output:

```python
Prakash 22
```

---

# 9. Positional Arguments

```python
def student(name, age):
    print(name, age)

student("Prakash", 22)
```

---

# 10. Arbitrary Arguments (\*args)

Allows multiple values.

```python
def numbers(*args):
    print(args)

numbers(1, 2, 3, 4, 5)
```

Output:

```python
(1, 2, 3, 4, 5)
```

---

# 11. Arbitrary Keyword Arguments (\*\*kwargs)

```python
def student(**kwargs):
    print(kwargs)

student(name="Prakash", age=22)
```

Output:

```python
{'name': 'Prakash', 'age': 22}
```

---

# 12. Local Variables

Created inside a function.

```python
def test():
    x = 10
    print(x)

test()
```

---

# 13. Global Variables

Created outside functions.

```python
x = 100

def test():
    print(x)

test()
```

Output:

```python
100
```

---

# 14. global Keyword

```python
x = 10

def change():
    global x
    x = 20

change()

print(x)
```

Output:

```python
20
```

---

# 15. Lambda Function

One-line anonymous function.

```python
square = lambda x: x*x

print(square(5))
```

Output:

```python
25
```

---

# 16. Nested Functions

Function inside another function.

```python
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()
```

---

# 17. Recursive Function

A function calling itself.

```python
def hello():
    hello()

hello()
```

⚠ Infinite recursion → Error

---

# Recursion

---

# 18. What is Recursion?

**Definition:**

A function calling itself repeatedly until a stopping condition (Base Case) is reached.

### Structure

```python
def function():
    if condition:
        return

    function()
```

---

# 19. Base Case

The condition that stops recursion.

Without a base case:

```python
def test():
    test()

test()
```

Output:

```python
RecursionError
```

---

# 20. Recursion Example

Print numbers from 1 to 5

```python
def show(n):

    if n > 5:
        return

    print(n)

    show(n + 1)

show(1)
```

Output:

```python
1
2
3
4
5
```

---

# 21. Recursion Tree

```python
show(1)
```

Calls:

```python
show(1)
 └─ show(2)
      └─ show(3)
           └─ show(4)
                └─ show(5)
                     └─ show(6)
```

Then returns back.

---

# 22. Factorial Using Recursion

### Formula

```text
5! = 5 × 4 × 3 × 2 × 1
```

### Code

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```python
120
```

---

# How Factorial Works

```python
factorial(5)

5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1
```

Result:

```python
120
```

---

# 23. Sum of N Numbers

```python
def total(n):

    if n == 1:
        return 1

    return n + total(n - 1)

print(total(5))
```

Output:

```python
15
```

Because:

```python
5+4+3+2+1=15
```

---

# 24. Fibonacci Series Using Recursion

```python
def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

print(fib(6))
```

Output:

```python
8
```

Series:

```python
0 1 1 2 3 5 8
```

---

# 25. Recursion vs Loop

| Loop                | Recursion                   |
| ------------------- | --------------------------- |
| Uses for/while      | Function calls itself       |
| Faster              | Slightly slower             |
| Less memory         | More memory                 |
| Easy for large data | Can hit recursion limit     |
| Preferred in Python | Used for tree-like problems |

---

# 26. When to Use Recursion?

Use recursion when solving:

- Factorial
- Fibonacci
- Tree Traversal
- Directory Traversal
- Binary Search
- Backtracking Problems
- DFS (Graphs)

---

# 27. Recursion Call Stack

Example:

```python
def test(n):

    if n == 0:
        return

    print(n)

    test(n-1)

test(3)
```

Stack:

```text
test(3)
test(2)
test(1)
test(0)
```

Then returns:

```text
test(0)
↑
test(1)
↑
test(2)
↑
test(3)
```

---

# Interview Definitions (Revision)

### Function

> A function is a reusable block of code that performs a specific task.

### Parameter

> Variables defined in function definition.

```python
def add(a, b):
```

`a` and `b` are parameters.

---

### Argument

> Values passed during function call.

```python
add(10, 20)
```

`10` and `20` are arguments.

---

### Return

> Sends a value back from a function.

---

### Recursion

> A technique where a function calls itself to solve a smaller version of the same problem.

---

### Base Case

> The condition that stops recursive calls.

---

### Call Stack

> Memory structure that stores active function calls.

---

# Quick Revision

```python
# Simple Function
def greet():
    print("Hello")

# Parameter
def greet(name):
    print(name)

# Return
def add(a,b):
    return a+b

# Lambda
square = lambda x:x*x

# Recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
```
