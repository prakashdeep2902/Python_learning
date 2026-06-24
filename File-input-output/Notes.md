# Python File I/O (Input/Output) — Complete Notes for Interviews & Revision

File handling is used to **store data permanently** in files instead of keeping it only in memory while the program runs.

---

# 1. What is File I/O?

### File Input

Reading data from a file.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

### File Output

Writing data to a file.

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

---

# 2. Why Use Files?

Without files:

```python
name = "Prakash"
```

Data disappears when the program ends.

With files:

```python
with open("user.txt", "w") as file:
    file.write("Prakash")
```

Data remains even after closing the program.

---

# 3. Types of Files

## Text Files

Store readable text.

Examples:

```text
notes.txt
data.csv
students.json
```

---

## Binary Files

Store non-readable data.

Examples:

```text
image.jpg
video.mp4
music.mp3
```

---

# 4. Opening a File

Syntax:

```python
file = open(filename, mode)
```

Example:

```python
file = open("data.txt", "r")
```

---

# 5. File Modes

## r (Read)

Reads existing file.

```python
file = open("data.txt", "r")
```

Error if file doesn't exist.

---

## w (Write)

Creates new file or overwrites existing file.

```python
file = open("data.txt", "w")
```

---

## a (Append)

Adds data at end.

```python
file = open("data.txt", "a")
```

---

## x (Create)

Creates file only if it doesn't exist.

```python
file = open("data.txt", "x")
```

---

## r+

Read and Write.

```python
file = open("data.txt", "r+")
```

---

## w+

Write and Read.

```python
file = open("data.txt", "w+")
```

---

## a+

Append and Read.

```python
file = open("data.txt", "a+")
```

---

## Binary Modes

```python
rb
wb
ab
rb+
wb+
ab+
```

Example:

```python
file = open("image.jpg", "rb")
```

---

# 6. Closing Files

```python
file = open("data.txt", "r")
file.close()
```

Always close manually if not using `with`.

---

# 7. with Statement (Recommended)

Automatically closes file.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

Interview favorite question.

---

# 8. Reading Methods

---

## read()

Reads entire file.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Output:

```text
Hello
World
```

---

## read(size)

Read limited characters.

```python
file.read(5)
```

Output:

```text
Hello
```

---

## readline()

Reads one line.

```python
file.readline()
```

Output:

```text
Hello
```

---

## readlines()

Returns list.

```python
lines = file.readlines()
```

Output:

```python
['Hello\n', 'World\n']
```

---

# 9. Writing Methods

---

## write()

```python
with open("data.txt", "w") as file:
    file.write("Python")
```

---

## writelines()

```python
data = ["A\n", "B\n", "C\n"]

with open("data.txt", "w") as file:
    file.writelines(data)
```

---

# 10. Iterating Through a File

```python
with open("data.txt") as file:
    for line in file:
        print(line)
```

Memory efficient.

---

# 11. File Cursor

Cursor = current position inside file.

Example:

```python
with open("data.txt", "r") as file:
    print(file.read(5))
```

Cursor moves after reading.

---

# 12. tell()

Returns current cursor position.

```python
with open("data.txt", "r") as file:
    print(file.tell())
```

Output:

```text
0
```

After:

```python
file.read(5)
print(file.tell())
```

Output:

```text
5
```

---

# 13. seek()

Move cursor.

```python
file.seek(0)
```

Move to beginning.

Example:

```python
with open("data.txt", "r") as file:
    file.read(5)
    file.seek(0)
    print(file.read())
```

---

# 14. Checking File Exists

```python
import os

print(os.path.exists("data.txt"))
```

---

# 15. Renaming Files

```python
import os

os.rename("old.txt", "new.txt")
```

---

# 16. Deleting Files

```python
import os

os.remove("data.txt")
```

---

# 17. Working with Directories

Create Folder

```python
import os

os.mkdir("files")
```

---

Remove Folder

```python
os.rmdir("files")
```

---

Current Directory

```python
os.getcwd()
```

---

Change Directory

```python
os.chdir("folder")
```

---

# 18. Exception Handling

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
```

---

# 19. CSV Files

```python
import csv

with open("data.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

Writing CSV

```python
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
```

---

# 20. JSON Files

Python Dictionary → JSON

```python
import json

data = {
    "name": "Prakash",
    "age": 25
}

with open("data.json", "w") as file:
    json.dump(data, file)
```

---

JSON → Python Dictionary

```python
import json

with open("data.json") as file:
    data = json.load(file)

print(data)
```

---

# 21. Binary Files

Write Binary

```python
with open("file.bin", "wb") as file:
    file.write(b"Hello")
```

Read Binary

```python
with open("file.bin", "rb") as file:
    print(file.read())
```

---

# 22. Important Built-in File Methods

| Method       | Purpose                 |
| ------------ | ----------------------- |
| open()       | Open file               |
| close()      | Close file              |
| read()       | Read entire file        |
| readline()   | Read one line           |
| readlines()  | Read all lines          |
| write()      | Write string            |
| writelines() | Write multiple lines    |
| seek()       | Move cursor             |
| tell()       | Current cursor position |
| flush()      | Force write buffer      |
| readable()   | Check readable          |
| writable()   | Check writable          |
| seekable()   | Check seek support      |
| truncate()   | Resize file             |

---

# 23. Useful File Attributes

```python
file.name
file.mode
file.closed
```

Example:

```python
with open("data.txt") as file:
    print(file.name)
    print(file.mode)
```

---

# 24. Common Interview Programs

### Count Characters

```python
with open("data.txt") as file:
    print(len(file.read()))
```

---

### Count Words

```python
with open("data.txt") as file:
    print(len(file.read().split()))
```

---

### Count Lines

```python
with open("data.txt") as file:
    print(len(file.readlines()))
```

---

### Copy File

```python
with open("source.txt") as src:
    content = src.read()

with open("dest.txt", "w") as dest:
    dest.write(content)
```

---

### Replace Word

```python
with open("file.txt") as file:
    data = file.read()

data = data.replace("donkey", "######")

with open("file.txt", "w") as file:
    file.write(data)
```

---

# 25. Interview Questions (Without Answers)

### Basic

1. What is File I/O in Python?
2. Why do we use files?
3. Difference between text and binary files?
4. What is a file object?
5. What happens when a file is not closed?

### Modes

6. Difference between `r` and `r+`?
7. Difference between `w` and `a`?
8. Difference between `w+` and `r+`?
9. What does `x` mode do?
10. What happens if file doesn't exist in `r` mode?

### Reading

11. Difference between `read()`, `readline()`, and `readlines()`?
12. When should you avoid `read()`?
13. How do you read large files efficiently?
14. What does `read(10)` do?
15. How do you read a file line by line?

### Writing

16. Difference between `write()` and `writelines()`?
17. What happens when using `w` mode on existing file?
18. What is append mode?
19. How do you write multiple lines?
20. What is buffering?

### Cursor

21. What is file cursor?
22. What does `tell()` return?
23. What does `seek()` do?
24. Why is cursor position important?
25. Can cursor move backward?

### with Statement

26. Why is `with open()` preferred?
27. How does context manager work?
28. What problem does `with` solve?
29. Is `close()` needed after `with`?
30. What happens if exception occurs inside `with` block?

### Advanced

31. What is a binary file?
32. Difference between `rb` and `r`?
33. How does JSON differ from CSV?
34. What is serialization?
35. What are `json.dump()` and `json.load()`?

### Practical

36. How would you copy a file?
37. How would you count words in a file?
38. How would you find duplicate lines?
39. How would you merge two files?
40. How would you replace a word in a file?

### Expert

41. What is file buffering?
42. What is random file access?
43. What is file descriptor?
44. What is memory-efficient file processing?
45. What is the difference between absolute and relative file paths?

---

## Must-Know Topics for Python Interviews

1. `open()`
2. File modes (`r`, `w`, `a`, `r+`, `w+`, `a+`)
3. `with open()`
4. `read()`, `readline()`, `readlines()`
5. `write()`, `writelines()`
6. `seek()`, `tell()`
7. Exception handling with files
8. CSV handling
9. JSON handling
10. Binary files
11. `os` module file operations
12. File copying and word counting programs

Master these 12 topics and you'll be able to answer most Python File I/O interview questions and solve common file-handling coding problems.
