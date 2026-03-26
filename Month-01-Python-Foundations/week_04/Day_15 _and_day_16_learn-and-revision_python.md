# 📅 Python Revision – Core Concepts (Functions, Loops, OOP, Decorators)

## 📚 What I Revised Today

Today I revised core Python concepts required for backend development and problem solving.

---

## 🔹 1️⃣ Functions

### Concept

- Functions are reusable blocks of code
- Improve modularity and readability

### Example

```python
def greet(name):
    return f"Hello {name}"
```

### Key Points

- Functions can return values
- Functions are first-class objects
- Can pass functions as arguments

---

## 🔹 2️⃣ Loops

### For Loop

```python
arr = [1, 2, 3]

for num in arr:
    print(num)
```

### While Loop

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

### Key Points

- Used for iteration
- Avoid infinite loops
- Use `break` and `continue` when needed

---

## 🔹 3️⃣ Classes & Objects

### Class Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"
```

### Object Creation

```python
p1 = Person("Kabilan")
print(p1.greet())
```

### Key Points

- Class → blueprint
- Object → instance
- `self` → refers to current object

---

## 🔹 4️⃣ OOP Concepts

### Encapsulation

- Bundle data and methods inside class

### Inheritance

```python
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    pass
```

### Polymorphism

- Same method behaves differently

### Abstraction

- Hide internal logic

---

## 🔹 5️⃣ Decorators

### Basic Structure

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

### Usage

```python
@decorator
def greet():
    print("Hello")
```

### Key Points

- Wrap functions
- Add extra behavior
- Used in backend frameworks

---

## 🔹 6️⃣ functools.wraps

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Why Use

- Preserves function name
- Keeps metadata intact
- Important for FastAPI and debugging

---

## 🔹 7️⃣ Combined Understanding

- Functions → building blocks
- Loops → iteration
- Classes → structure
- OOP → design system
- Decorators → enhance behavior

---

# 🚀 Key Takeaway

Today I revised:

- Python core fundamentals
- OOP concepts
- Decorator internals
- Loop and function usage

This strengthens my foundation for:

- Backend development
- API design
- Problem solving