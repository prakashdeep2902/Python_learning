# Variables and Data Types in Python

---

# 1️⃣ Variables

## Definition

A **variable** is a container used to store data values in memory.

Think of a variable as a labeled box where you can store information.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Prakash"
age = 22

print(name)
print(age)
```

### Output

```text
Prakash
22
```

### Variable Naming Rules

✅ Valid

```python
name = "Prakash"
_age = 22
user1 = "John"
```

❌ Invalid

```python
1name = "Prakash"    # Cannot start with a number
class = "Python"     # Reserved keyword
```

---

# 2️⃣ Data Types

## Definition

A **data type** specifies the type of data a variable can store.

Python automatically detects the data type.

---

## Common Data Types

| Data Type | Example            |
| --------- | ------------------ |
| int       | 10, 100            |
| float     | 10.5, 99.99        |
| str       | "Hello"            |
| bool      | True, False        |
| list      | [1, 2, 3]          |
| tuple     | (1, 2, 3)          |
| dict      | {"name":"Prakash"} |
| set       | {1, 2, 3}          |

---

## 1. Integer (int)

Whole numbers.

```python
age = 22

print(age)
print(type(age))
```

**Output**

```text
22
<class 'int'>
```

---

## 2. Float

Decimal numbers.

```python
price = 99.99

print(type(price))
```

**Output**

```text
<class 'float'>
```

---

## 3. String (str)

Text data.

```python
name = "Prakash"

print(type(name))
```

**Output**

```text
<class 'str'>
```

---

## 4. Boolean (bool)

Represents True or False.

```python
is_python_easy = True

print(type(is_python_easy))
```

**Output**

```text
<class 'bool'>
```

---

## Check Data Type

Use `type()`.

```python
x = 100

print(type(x))
```

Output:

```text
<class 'int'>
```

---

# Real Example

```python
name = "Prakash"
age = 22
salary = 50000.50
is_working = True

print(name)
print(age)
print(salary)
print(is_working)
```

---

# Interview Questions

### Q1. What is a variable?

**Answer:**
A variable is a named memory location used to store data.

---

### Q2. How do you create a variable in Python?

```python
name = "Prakash"
```

---

### Q3. Does Python require declaring a data type?

**Answer:**
No. Python is dynamically typed, so it automatically detects the data type.

Example:

```python
x = 10
y = "Hello"
```

---

### Q4. How do you check the data type of a variable?

```python
print(type(x))
```

---

### Q5. What are the basic data types in Python?

**Answer:**

- int
- float
- str
- bool
- list
- tuple
- dict
- set

---

### Q6. Difference between int and float?

| int          | float          |
| ------------ | -------------- |
| Whole number | Decimal number |
| 10           | 10.5           |

---

### Q7. Difference between `=` and `==`?

```python
x = 10      # Assignment
x == 10     # Comparison
```

**Answer:**

- `=` assigns a value.
- `==` compares values.

---

# Quick Revision

```python
name = "Prakash"    # str
age = 22            # int
salary = 50000.50   # float
is_active = True    # bool
```

### Remember

- Variable = Stores data
- Data Type = Type of data stored
- Use `type()` to check the data type
- Python automatically determines data types (Dynamic Typing) 🚀

# Operators in Python

## Definition

**Operators** are special symbols used to perform operations on variables and values.

---

# 1️⃣ Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning             | Example   |
| -------- | ------------------- | --------- |
| `+`      | Addition            | `5 + 3`   |
| `-`      | Subtraction         | `5 - 3`   |
| `*`      | Multiplication      | `5 * 3`   |
| `/`      | Division            | `10 / 2`  |
| `//`     | Floor Division      | `10 // 3` |
| `%`      | Modulus (Remainder) | `10 % 3`  |
| `**`     | Power               | `2 ** 3`  |

### Example

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

# 2️⃣ Comparison Operators

Used to compare values.

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not Equal             |
| `>`      | Greater Than          |
| `<`      | Less Than             |
| `>=`     | Greater Than or Equal |
| `<=`     | Less Than or Equal    |

### Example

```python
x = 10
y = 20

print(x == y)  # False
print(x < y)   # True
```

---

# 3️⃣ Logical Operators

Used to combine conditions.

| Operator | Meaning              |
| -------- | -------------------- |
| `and`    | Both conditions True |
| `or`     | At least one True    |
| `not`    | Opposite result      |

### Example

```python
age = 20

print(age > 18 and age < 60)  # True
print(not True)               # False
```

---

# 4️⃣ Assignment Operators

Used to assign values.

| Operator | Example  |
| -------- | -------- |
| `=`      | `x = 10` |
| `+=`     | `x += 5` |
| `-=`     | `x -= 5` |
| `*=`     | `x *= 5` |
| `/=`     | `x /= 5` |

### Example

```python
x = 10
x += 5

print(x)
```

**Output**

```text
15
```

---

# 5️⃣ Membership Operators

Used to check whether a value exists in a sequence.

| Operator | Meaning     |
| -------- | ----------- |
| `in`     | Present     |
| `not in` | Not Present |

### Example

```python
name = "Prakash"

print("P" in name)      # True
print("Z" in name)      # False
```

---

# Interview Questions

### Q1. What are operators?

Operators are symbols used to perform operations on values and variables.

### Q2. Difference between `=` and `==`?

```python
x = 10    # Assignment
x == 10   # Comparison
```

### Q3. What does `%` do?

Returns the remainder.

```python
10 % 3
```

Output:

```text
1
```

### Q4. What does `**` do?

Used for power.

```python
2 ** 3
```

Output:

```text
8
```

---

# Quick Revision

| Category   | Operators         |
| ---------- | ----------------- |
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical    | `and or not`      |
| Assignment | `= += -= *= /=`   |
| Membership | `in not in`       |

📌 **Remember:** Operators help us perform calculations, comparisons, and logical decisions in Python. 🚀

# Types and Type Casting in Python (Short Notes)

## Data Types

A **data type** defines the kind of value a variable stores.

### Common Data Types

```python
age = 22          # int
price = 99.99     # float
name = "Prakash"  # str
is_active = True  # bool
```

| Type  | Example |
| ----- | ------- |
| int   | 10      |
| float | 10.5    |
| str   | "Hello" |
| bool  | True    |

---

# Type Casting

**Type Casting** means converting one data type into another.

### Examples

#### int → float

```python
x = 10
print(float(x))
```

Output:

```python
10.0
```

#### float → int

```python
x = 10.5
print(int(x))
```

Output:

```python
10
```

#### str → int

```python
x = "100"
print(int(x))
```

Output:

```python
100
```

#### int → str

```python
x = 100
print(str(x))
```

Output:

```python
'100'
```

---

# Check Type

```python
x = 10
print(type(x))
```

Output:

```python
<class 'int'>
```

---

# Interview Questions

### Q1. What is a data type?

A data type defines the type of value stored in a variable.

### Q2. What is type casting?

Converting one data type into another.

### Q3. How do you check a variable's type?

```python
type(variable)
```

### Q4. Name some common Python data types.

- int
- float
- str
- bool

---

## Quick Revision

```python
int()      # Convert to Integer
float()    # Convert to Float
str()      # Convert to String
bool()     # Convert to Boolean
```

📌 **Formula:**
**Type Casting = Converting one data type → another data type** 🚀
