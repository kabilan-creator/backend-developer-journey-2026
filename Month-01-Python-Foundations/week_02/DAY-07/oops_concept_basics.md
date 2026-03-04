# 📅 Day – Python OOP Fundamentals

## 📚 What I Learned Today

Today I learned the fundamentals of **Object-Oriented Programming (OOP)** in Python and why it is important for building scalable and maintainable applications.

---

## 🔹 1️⃣ What is Object-Oriented Programming (OOP)

OOP is a programming paradigm that organizes code using **classes and objects**.

It helps represent **real-world entities in software** and improves:

- Code structure
- Reusability
- Maintainability
- Scalability

---

## 🔹 2️⃣ Class

A **class** is a blueprint used to create objects.

It defines:
- **Attributes** → data
- **Methods** → functions/behavior

Example:

```python
class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Key Understanding

- Classes act as templates.
- Attributes store data.
- Methods define behavior.

---

## 🔹 3️⃣ Object

An **object** is an instance of a class.

Each object:
- Has its own data
- Follows the structure defined by the class

Example:

```python
dog1 = Dog("Buddy", 3)
```

Here, `dog1` is an object created from the `Dog` class.

---

## 🔹 4️⃣ Constructor (`__init__`)

The `__init__` method is a **special method** that runs automatically when an object is created.

It is used to **initialize object attributes**.

Example:

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

---

## 🔹 5️⃣ `self` Keyword

The `self` keyword refers to the **current instance of the class**.

It allows objects to:
- Store their own data
- Access their own attributes and methods

---

## 🔹 6️⃣ Class Attributes vs Instance Attributes

### Class Attribute
Shared by **all objects** of the class.

Example:

```python
class Dog:
    species = "Canine"
```

### Instance Attribute
Unique to **each object**.

Example:

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

---

## 🔹 7️⃣ Four Pillars of OOP

I learned the **core principles of OOP**.

### 1️⃣ Encapsulation
Bundling data and methods together inside a class.

### 2️⃣ Inheritance
Allowing a child class to inherit properties and methods from a parent class.

### 3️⃣ Polymorphism
The same method name can perform different behaviors depending on the object.

### 4️⃣ Abstraction
Hiding internal implementation details and exposing only necessary functionality.

---

# 🎯 Key Takeaway

Classes help:

- Organize code
- Model real-world entities
- Improve reusability
- Make large applications easier to manage

OOP is widely used in **backend systems, frameworks, and large-scale software development**.

---

# 🚀 Next Learning Plan

Next I will learn:

- Instance vs Class variables
- `@classmethod` and `@staticmethod`
- Magic methods in Python
- Method overriding
- Inheritance concepts