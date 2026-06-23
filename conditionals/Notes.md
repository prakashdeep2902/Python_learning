# Python Conditions & Membership Operators - Quick Revision Notes

## 1. Condition

**Definition:**
A condition is an expression that evaluates to either `True` or `False`.

**Example:**

```python
age = 20
print(age >= 18)   # True
```

---

## 2. `if` Statement

**Definition:**
Used to execute a block of code only when a condition is `True`.

**Syntax:**

```python
if condition:
    statement
```

**Example:**

```python
age = 20

if age >= 18:
    print("Adult")
```

---

## 3. `if-else` Statement

**Definition:**
Used when you want one action if the condition is true and another action if it is false.

**Syntax:**

```python
if condition:
    statement1
else:
    statement2
```

**Example:**

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 4. `if-elif-else` Statement

**Definition:**
Used to check multiple conditions one by one.

**Syntax:**

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

**Example:**

```python
marks = 85

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
else:
    print("C Grade")
```

---

# Comparison Operators

## 5. `==` (Equal To)

**Definition:** Checks whether two values are equal.

```python
print(10 == 10)  # True
```

## 6. `!=` (Not Equal To)

**Definition:** Checks whether two values are different.

```python
print(10 != 20)  # True
```

## 7. `>` (Greater Than)

```python
print(20 > 10)  # True
```

## 8. `<` (Less Than)

```python
print(10 < 20)  # True
```

## 9. `>=` (Greater Than or Equal To)

```python
print(20 >= 20)  # True
```

## 10. `<=` (Less Than or Equal To)

```python
print(10 <= 20)  # True
```

---

# Logical Operators

## 11. `and`

**Definition:** Returns `True` only if both conditions are true.

```python
age = 25
salary = 50000

if age > 18 and salary > 30000:
    print("Eligible")
```

---

## 12. `or`

**Definition:** Returns `True` if at least one condition is true.

```python
marks = 35
sports = True

if marks >= 40 or sports:
    print("Admission Granted")
```

---

## 13. `not`

**Definition:** Reverses the result.

```python
is_blocked = False

if not is_blocked:
    print("Access Allowed")
```

---

# Nested Condition

## 14. Nested `if`

**Definition:** An `if` statement inside another `if` statement.

```python
age = 20
license = True

if age >= 18:
    if license:
        print("Can Drive")
```

---

# Membership Operators

## 15. `in`

**Definition:** Checks whether a value exists in a sequence (list, tuple, string, set, dictionary).

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
```

**Output:**

```python
True
```

---

## 16. `not in`

**Definition:** Checks whether a value does not exist in a sequence.

```python
fruits = ["apple", "banana"]

print("orange" not in fruits)
```

**Output:**

```python
True
```

---

# Collection Types Used with `in`

## 17. List

**Definition:** Ordered, mutable collection.

```python
fruits = ["apple", "banana", "mango"]
```

---

## 18. Tuple

**Definition:** Ordered, immutable collection.

```python
numbers = (10, 20, 30)
```

---

## 19. Set

**Definition:** Unordered collection of unique values.

```python
colors = {"red", "green", "blue"}
```

---

## 20. String

**Definition:** Collection of characters.

```python
name = "Prakash"
```

---

## 21. Dictionary

**Definition:** Stores data in key-value pairs.

```python
student = {
    "name": "Prakash",
    "age": 25
}
```

Access key:

```python
print("name" in student)
```

Access value:

```python
print("Prakash" in student.values())
```

---

# Ternary Operator

## 22. One-Line `if-else`

**Definition:** Short form of `if-else`.

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

# Interview Revision (1-Minute Summary)

```text
if        -> Executes code when condition is True
else      -> Executes code when condition is False
elif      -> Checks multiple conditions
==        -> Equal
!=        -> Not Equal
>         -> Greater Than
<         -> Less Than
>=        -> Greater Than or Equal
<=        -> Less Than or Equal
and       -> Both conditions must be True
or        -> Any one condition must be True
not       -> Reverse the result
in        -> Checks existence of value
not in    -> Checks absence of value
List      -> Ordered, mutable collection
Tuple     -> Ordered, immutable collection
Set       -> Unique values only
Dictionary-> Key-value pairs
Nested if -> if inside another if
Ternary   -> One-line if-else
```

These are the core condition concepts that every Python beginner and interview candidate should know.
