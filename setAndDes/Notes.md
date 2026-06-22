# Dictionary and Set in Python

## Dictionary

### Definition

A **Dictionary** is a mutable collection that stores data in the form of **key-value pairs**.

### Example

```python
student = {
    "name": "Prakash",
    "age": 22,
    "city": "Delhi"
}

print(student)
```

### Features

- Stores data as key-value pairs
- Mutable (can be modified)
- Keys must be unique
- Ordered (Python 3.7+)
- Fast data lookup using keys

### Accessing Values

```python
student = {
    "name": "Prakash",
    "age": 22
}

print(student["name"])
print(student.get("age"))
```

### Adding and Updating Values

```python
student = {
    "name": "Prakash"
}

student["age"] = 22
student["name"] = "Rahul"

print(student)
```

### Removing Values

```python
student = {
    "name": "Prakash",
    "age": 22
}

student.pop("age")

print(student)
```

### Important Dictionary Methods

| Method    | Description             |
| --------- | ----------------------- |
| get()     | Returns value of key    |
| keys()    | Returns all keys        |
| values()  | Returns all values      |
| items()   | Returns key-value pairs |
| update()  | Updates dictionary      |
| pop()     | Removes a key           |
| popitem() | Removes last item       |
| clear()   | Removes all items       |
| copy()    | Creates copy            |

### Example

```python
student = {
    "name": "Prakash",
    "age": 22
}

print(student.keys())
print(student.values())
print(student.items())
```

### Dictionary Comprehension

#### Definition

Dictionary comprehension is a short way to create dictionaries.

#### Example

```python
squares = {x: x*x for x in range(5)}

print(squares)
```

---

# Set

## Definition

A **Set** is an unordered collection of unique elements.

### Example

```python
numbers = {1, 2, 3, 4, 5}

print(numbers)
```

### Features

- Stores unique values only
- Mutable
- Unordered
- Fast searching
- Removes duplicates automatically

### Creating an Empty Set

```python
s = set()
```

### Adding Elements

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

### Adding Multiple Elements

```python
numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)
```

### Removing Elements

```python
numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)
```

### Important Set Methods

| Method    | Description            |
| --------- | ---------------------- |
| add()     | Adds element           |
| update()  | Adds multiple elements |
| remove()  | Removes element        |
| discard() | Removes element safely |
| pop()     | Removes random element |
| clear()   | Removes all elements   |
| copy()    | Creates copy           |

### Example

```python
numbers = {1, 2, 3}

numbers.discard(2)

print(numbers)
```

---

# Set Operations

## Union

### Definition

Combines all unique elements from both sets.

### Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
```

Output:

```python
{1, 2, 3, 4, 5}
```

---

## Intersection

### Definition

Returns common elements from both sets.

### Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)
```

Output:

```python
{3}
```

---

## Difference

### Definition

Returns elements present in first set but not in second set.

### Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A - B)
```

Output:

```python
{1, 2}
```

---

## Symmetric Difference

### Definition

Returns elements present in either set but not in both.

### Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A ^ B)
```

Output:

```python
{1, 2, 4, 5}
```

---

# Frozen Set

## Definition

A **Frozen Set** is an immutable version of a set.

### Example

```python
fs = frozenset([1, 2, 3])

print(fs)
```

---

# Dictionary vs Set

| Feature          | Dictionary      | Set                |
| ---------------- | --------------- | ------------------ |
| Stores           | Key-Value Pairs | Unique Values      |
| Mutable          | Yes             | Yes                |
| Ordered          | Yes             | No                 |
| Duplicate Values | Allowed         | Not Allowed        |
| Access Method    | By Key          | Membership Testing |

### Dictionary Example

```python
student = {
    "name": "Prakash",
    "age": 22
}
```

### Set Example

```python
numbers = {1, 2, 3, 4}
```

---

# Practice Questions

## Dictionary Questions

### 1. Student Marks Dictionary

Create a dictionary containing student names and marks. Print the student with the highest marks.

### 2. Character Frequency Counter

Count frequency of each character in a string using a dictionary.

### 3. Word Count Program

Count occurrence of each word in a sentence.

### 4. Merge Two Dictionaries

Merge two dictionaries into one.

### 5. Invert a Dictionary

Convert keys into values and values into keys.

---

## Set Questions

### 6. Remove Duplicates

Remove duplicate values from a list using a set.

### 7. Common Elements

Find common elements between two sets.

### 8. Unique Words Finder

Print all unique words from a sentence.

### 9. Check Subset

Check whether one set is a subset of another.

### 10. Missing Numbers

Find missing numbers using set operations.

---

# Interview Questions

## Dictionary

1. What is a dictionary?
2. Why must dictionary keys be unique?
3. Difference between get() and []?
4. What is dictionary comprehension?
5. How do you merge dictionaries?

## Set

1. What is a set?
2. Why are sets faster for searching?
3. Difference between remove() and discard()?
4. What is a frozenset?
5. Explain union and intersection.

---

# Quick Revision

## Dictionary

```python
student = {
    "name": "Prakash",
    "age": 22
}
```

- Key-Value pairs
- Mutable
- Ordered
- Unique keys

## Set

```python
numbers = {1, 2, 3, 4}
```

- Unique values
- Mutable
- Unordered
- Fast searching
