# 📅 Day 04 – Python Decorators

## 📚 What I Learned Today

Today I learned about Decorators in Python.

A decorator:
- Is a function that modifies another function
- Adds extra behavior without changing the original function’s code
- Wraps a function inside another function

---

## 🧠 Key Understanding

When we write:

```python
@decorator
def greet():
    print("Hello")
```

Python internally does:

```python
greet = decorator(greet)
```

Meaning:
- The original function is passed into the decorator
- The decorator returns a new function (wrapper)
- The function name now points to wrapper
- Wrapper controls what happens before and after execution

Functions in Python are first-class objects:
- Can be assigned
- Can be passed as arguments
- Can be returned from other functions

---

## 🎯 Why We Use Decorators

### 1️⃣ Avoid Repeating Code (DRY Principle)

Used to:
- Add logging
- Add authentication
- Add validation
- Add execution timing

Instead of repeating logic in every function, we wrap them once.

---

### 2️⃣ Separation of Concerns

- Business logic stays clean
- Extra logic (logging, auth, validation) stays separate
- Makes backend systems scalable

---

### 3️⃣ Modify Behavior Without Editing Original Code

- Add behavior dynamically
- Improve maintainability
- Keep functions simple

---

## 🧩 Function Replacement Concept

When using:

```python
@decorator
def greet():
    print("Hello")
```

Python does:

```python
greet = decorator(greet)
```

So:
- greet now points to wrapper
- Original function still exists inside wrapper

---

## 🛠 functools.wraps

```python
from functools import wraps
```

Why use it?

Without @wraps:
- Function name becomes "wrapper"
- __name__, __doc__, annotations are lost

With @wraps:
- Metadata is preserved
- Important for backend frameworks

Rule:
Always use:

```python
@wraps(original_function)
```

in production decorators.

---

## 🚀 Real Backend Usage

### FastAPI

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

@app.get("/") is a decorator.
It registers the function as an API route.

### Flask

```python
@app.route("/")
def home():
    return "Hello"
```

Registers route using a decorator.

---

## 💡 What Improved Today

- Strong understanding of decorator internals
- Clear mental model of function replacement
- Understood why @wraps is important
- Connected decorators to backend architecture
- Improved clean architecture thinking