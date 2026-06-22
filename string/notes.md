You're right. My mistake — I gave **JavaScript Strings** instead of **Python Strings**.

# Strings in Python (Short Notes)

## Definition

A **String** is a sequence of characters enclosed in quotes.

### Example

```python
name = "Prakash"
city = 'Delhi'
```

---

# Access Characters

```python
name = "Prakash"

print(name[0])
```

**Output**

```text
P
```

---

# String Methods

### 1. upper()

```python
name = "prakash"

print(name.upper())
```

**Output**

```text
PRAKASH
```

---

### 2. lower()

```python
name = "PRAKASH"

print(name.lower())
```

**Output**

```text
prakash
```

---

### 3. strip()

Removes extra spaces.

```python
name = "  Prakash  "

print(name.strip())
```

**Output**

```text
Prakash
```

---

### 4. replace()

```python
msg = "Hello World"

print(msg.replace("World", "Python"))
```

**Output**

```text
Hello Python
```

---

### 5. len()

Returns string length.

```python
name = "Prakash"

print(len(name))
```

**Output**

```text
7
```

---

### 6. split()

```python
text = "Python is easy"

print(text.split())
```

**Output**

```python
['Python', 'is', 'easy']
```

---

# String Concatenation

```python
first = "Prakash"
last = "Sharma"

print(first + " " + last)
```

**Output**

```text
Prakash Sharma
```

---

# f-String (Most Important)

```python
name = "Prakash"
age = 22

print(f"My name is {name} and I am {age} years old")
```

**Output**

```text
My name is Prakash and I am 22 years old
```

---

# Interview Questions

### Q1. What is a string?

A string is a collection of characters enclosed in quotes.

### Q2. Are strings mutable in Python?

**No**, strings are **immutable**.

### Q3. How do you find string length?

```python
len(string)
```

### Q4. Difference between `+` and f-string?

- `+` → Concatenation
- `f-string` → Modern and preferred way

---

# Quick Revision

| Method      | Purpose                |
| ----------- | ---------------------- |
| `len()`     | Length                 |
| `upper()`   | Uppercase              |
| `lower()`   | Lowercase              |
| `strip()`   | Remove spaces          |
| `replace()` | Replace text           |
| `split()`   | Convert string to list |

📌 **Remember:** String = Text data enclosed in `' '` or `" "` and strings are **immutable** in Python. 🚀
