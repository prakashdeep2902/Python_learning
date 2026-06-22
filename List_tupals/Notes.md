# Lists and Tuples in Python

---

# 1️⃣ List

## Definition

A **List** is an ordered, mutable (changeable) collection of items.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

**Output**

```text
['Apple', 'Banana', 'Mango']
```

### Access Elements

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
```

**Output**

```text
Apple
```

### Modify List

```python
fruits = ["Apple", "Banana"]

fruits[1] = "Orange"

print(fruits)
```

**Output**

```text
['Apple', 'Orange']
```

### Common Methods

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")   # Add item
fruits.remove("Banana")  # Remove item

print(fruits)
```

---

# 2️⃣ Tuple

## Definition

A **Tuple** is an ordered, immutable (unchangeable) collection of items.

### Example

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits)
```

**Output**

```text
('Apple', 'Banana', 'Mango')
```

### Access Elements

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
```

**Output**

```text
Apple
```

### Cannot Modify

```python
fruits = ("Apple", "Banana")

fruits[1] = "Orange"   # Error
```

---

# Difference Between List and Tuple

| List        | Tuple         |
| ----------- | ------------- |
| `[]`        | `()`          |
| Mutable     | Immutable     |
| Can modify  | Cannot modify |
| More memory | Less memory   |
| Slower      | Faster        |

---

# Interview Questions

### Q1. What is a List?

A mutable collection of items stored in square brackets `[]`.

### Q2. What is a Tuple?

An immutable collection of items stored in parentheses `()`.

### Q3. Difference between List and Tuple?

- List → Changeable
- Tuple → Not Changeable

### Q4. Which is faster?

**Tuple** is faster than List.

---

# Quick Revision

```python
# List
numbers = [1, 2, 3]

# Tuple
numbers = (1, 2, 3)
```

📌 **Remember:**

- **List = Mutable = `[]`**
- **Tuple = Immutable = `()`** 🚀

# Useful List Methods in Python

## 1. append()

Adds an item at the end.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")
print(fruits)
```

Output:

```python
['Apple', 'Banana', 'Mango']
```

---

## 2. insert()

Adds an item at a specific position.

```python
fruits.insert(1, "Orange")
```

---

## 3. remove()

Removes a specific item.

```python
fruits.remove("Banana")
```

---

## 4. pop()

Removes item by index.

```python
fruits.pop()
```

---

## 5. sort()

Sorts the list.

```python
numbers = [5, 2, 8, 1]

numbers.sort()
print(numbers)
```

Output:

```python
[1, 2, 5, 8]
```

---

## 6. reverse()

Reverses the list.

```python
numbers.reverse()
```

---

## 7. count()

Counts occurrences.

```python
nums = [1, 2, 2, 3]

print(nums.count(2))
```

Output:

```python
2
```

---

## 8. index()

Returns the index of an item.

```python
nums.index(3)
```

---

# Useful Tuple Methods in Python

Since tuples are **immutable**, they have only **2 built-in methods**.

---

## 1. count()

Counts occurrences.

```python
numbers = (1, 2, 2, 3)

print(numbers.count(2))
```

Output:

```python
2
```

---

## 2. index()

Returns the position of an item.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output:

```python
1
```

---

# Useful Functions for Both List and Tuple

## len()

Returns total items.

```python
nums = [1, 2, 3]

print(len(nums))
```

---

## max()

Returns largest value.

```python
print(max([10, 20, 30]))
```

Output:

```python
30
```

---

## min()

Returns smallest value.

```python
print(min([10, 20, 30]))
```

Output:

```python
10
```

---

## sum()

Returns total sum.

```python
print(sum([10, 20, 30]))
```

Output:

```python
60
```

---

# Interview Questions

### Q1. Which methods are available in Tuple?

- `count()`
- `index()`

### Q2. Why does Tuple have fewer methods than List?

Because tuples are **immutable** (cannot be changed).

### Q3. Most commonly used List methods?

- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`

---

# Quick Revision

### List Methods

```python
append()
insert()
remove()
pop()
sort()
reverse()
count()
index()
```

### Tuple Methods

```python
count()
index()
```

📌 **Interview Shortcut:**

**List = Mutable → Many Methods**
**Tuple = Immutable → Only count() and index()** 🚀
