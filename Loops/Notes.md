# Python Loops — Complete Revision Guide

Loops are used to execute a block of code repeatedly.

---

# 1. What is a Loop?

A loop allows you to run the same code multiple times without writing it repeatedly.

### Example

```python
for i in range(5):
    print("Hello")
```

Output:

```
Hello
Hello
Hello
Hello
Hello
```

---

# 2. Types of Loops in Python

Python has two main loops:

1. `for` loop
2. `while` loop

---

# 3. for Loop

Used when you know how many times you want to repeat something.

### Syntax

```python
for variable in sequence:
    statement
```

### Example

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

# 4. range() Function

Used to generate a sequence of numbers.

### range(stop)

```python
for i in range(5):
    print(i)
```

Output:

```
0 1 2 3 4
```

---

### range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output:

```
2 3 4 5
```

---

### range(start, stop, step)

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```
1 3 5 7 9
```

---

### Reverse Loop

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```
10
9
8
...
1
```

---

# 5. Looping Through Strings

```python
name = "Prakash"

for ch in name:
    print(ch)
```

Output:

```
P
r
a
k
a
s
h
```

---

# 6. Looping Through Lists

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

Output:

```
10
20
30
```

---

# 7. Looping Through Tuples

```python
data = (1, 2, 3)

for i in data:
    print(i)
```

---

# 8. Looping Through Sets

```python
nums = {10, 20, 30}

for i in nums:
    print(i)
```

Note:

- Sets are unordered.

---

# 9. Looping Through Dictionaries

### Keys

```python
student = {
    "name": "Prakash",
    "age": 22
}

for key in student:
    print(key)
```

Output:

```
name
age
```

---

### Values

```python
for value in student.values():
    print(value)
```

Output:

```
Prakash
22
```

---

### Key-Value Pair

```python
for key, value in student.items():
    print(key, value)
```

Output:

```
name Prakash
age 22
```

---

# 10. while Loop

Used when the number of repetitions is not known beforehand.

### Syntax

```python
while condition:
    statement
```

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```
1
2
3
4
5
```

---

# 11. Infinite Loop

```python
while True:
    print("Running")
```

This never stops unless you use `break`.

---

# 12. break Statement

Used to exit a loop immediately.

### Example

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

Output:

```
1
2
3
4
```

---

# 13. continue Statement

Skips the current iteration.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```
1
2
4
5
```

---

# 14. pass Statement

Placeholder for future code.

```python
for i in range(5):
    pass
```

No output.

---

# 15. else with Loops

The `else` block executes only if the loop finishes normally.

### Example

```python
for i in range(5):
    print(i)
else:
    print("Loop Finished")
```

Output:

```
0
1
2
3
4
Loop Finished
```

---

### With break

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Finished")
```

Output:

```
No output from else
```

---

# 16. Nested Loops

A loop inside another loop.

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output:

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# 17. enumerate()

Provides index and value together.

```python
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```
0 Apple
1 Banana
2 Mango
```

---

# 18. zip()

Loops through multiple sequences simultaneously.

```python
names = ["Prakash", "Rahul"]
ages = [22, 24]

for name, age in zip(names, ages):
    print(name, age)
```

Output:

```
Prakash 22
Rahul 24
```

---

# 19. List Comprehension

Short way to create lists using loops.

### Normal Loop

```python
squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)
```

---

### List Comprehension

```python
squares = [i ** 2 for i in range(1, 6)]

print(squares)
```

Output:

```
[1, 4, 9, 16, 25]
```

---

# 20. Common Loop Programs

## Print 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## Sum of Numbers

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output:

```
15
```

---

## Factorial

```python
num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)
```

Output:

```
120
```

---

## Multiplication Table

```python
num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
```

---

## Prime Number

```python
num = 13

is_prime = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print("Prime")
else:
    print("Not Prime")
```

---

# 21. Important Keywords Related to Loops

| Keyword       | Meaning                         |
| ------------- | ------------------------------- |
| `for`         | Iterate over sequence           |
| `while`       | Repeat while condition is True  |
| `break`       | Exit loop                       |
| `continue`    | Skip current iteration          |
| `pass`        | Placeholder                     |
| `range()`     | Generate numbers                |
| `enumerate()` | Get index and value             |
| `zip()`       | Iterate over multiple sequences |
| `else`        | Runs if loop ends normally      |

---

# Interview Questions

### Q1. Difference between for and while?

| for                  | while                 |
| -------------------- | --------------------- |
| Known iterations     | Unknown iterations    |
| Works with sequences | Works with conditions |
| Easier to read       | More flexible         |

---

### Q2. What is an infinite loop?

A loop that never ends.

```python
while True:
    print("Hello")
```

---

### Q3. Difference between break and continue?

```python
break      # Stops loop completely
continue   # Skips current iteration
```

---

# Quick Revision (1 Minute)

```python
for i in range(5):
    pass

while condition:
    pass

break      # Exit loop
continue   # Skip iteration
pass       # Do nothing

range()
enumerate()
zip()

Nested Loops
Loop Else
List Comprehension
```
