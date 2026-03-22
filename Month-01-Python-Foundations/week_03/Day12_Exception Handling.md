# 📅 Day 12 – Error Handling, File Handling & System Operations

## 📚 What I Learned Today

Today I learned how to write **safe, robust, and backend-ready Python code** using exception handling, file operations, and system modules.

---

## 🔥 1️⃣ Error Types (Core Understanding)

I understood three types of errors:

- **Syntax Error** → Code will not run
- **Logical Error** → Wrong output
- **Exception** → Runtime crash

### Key Learning

- Only **exceptions can be handled**
- Syntax and logical errors must be fixed manually

---

## 🔥 2️⃣ Exception Handling (Very Important)

I learned how to prevent program crashes using `try-except`.

### Example

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input")
```

### General Handling

```python
try:
    # risky code
except Exception as e:
    print(e)
```

### Key Learning

- Handle specific errors when possible
- Prevent application crashes
- Write production-safe code

---

## 🔥 3️⃣ Exception Hierarchy

I understood:

- All exceptions come under `Exception`
- Many specific errors inherit from it

### Example

- ValueError
- ZeroDivisionError
- FileNotFoundError

### Key Insight

- `except Exception` catches most runtime errors

---

## 🔥 4️⃣ finally Block

### Concept

- `finally` always executes

### Example

```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup done")
```

### Key Learning

- Used for cleanup (files, database, connections)

---

## 📂 5️⃣ File Handling (Backend Core Skill)

### Read File

```python
with open("file.txt", "r") as f:
    data = f.read()
```

### Write File

```python
with open("file.txt", "w") as f:
    f.write("data")
```

### Append File

```python
with open("file.txt", "a") as f:
    f.write("new data")
```

### Key Learning

- `with` ensures file is automatically closed
- Safe and recommended way

---

## 🧠 6️⃣ OS Module (System Operations)

I learned how to interact with the system:

```python
import os

os.path.exists("file.txt")
os.remove("file.txt")
os.rename("old.txt", "new.txt")
os.listdir()
```

### Use Case

- File management in backend systems

---

## ⚡ 7️⃣ pathlib (Modern Approach)

```python
from pathlib import Path

p = Path("file.txt")

p.exists()
p.read_text()
p.write_text("hello")
```

### Key Learning

- Cleaner and more readable than `os`
- Preferred in modern Python development

---

## 📁 8️⃣ Directory Management

### Create Directory

```python
os.mkdir("folder")
```

### Create Nested Directory

```python
os.makedirs("parent/child")
```

### Remove Directory

```python
os.rmdir("folder")
```

### Use Case

- File uploads
- Project structure
- Storage systems

---

## 🔥 9️⃣ Real-World Backend Thinking

I combined everything into practical code:

```python
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File missing")
```

### Key Understanding

- Handle errors safely
- Use files properly
- Write production-level backend logic

---

# 🚀 What Improved Today

- Strong understanding of exception handling
- Ability to write crash-free code
- Learned file handling for backend systems
- Understood OS and file system operations
- Improved real-world coding thinking