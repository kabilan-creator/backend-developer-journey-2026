# Day 02 – Inner Functions

## 📚 What I Learned Today

Today I learned about **Inner Functions** in Python.

- An inner function is defined inside another function.
- It can only be accessed within the outer function.
- It behaves like a private helper function.

---

## 🧠 Key Understanding

- `inner()` exists only inside `outer()`.
- It cannot be called directly from outside.
- This helps in controlling access to helper logic.

---

## 🎯 Why We Use Inner Functions

### 1️⃣ Encapsulation
- Hide helper logic from outside access.
- Prevent accidental usage.
- Example: `clean_data()` cannot be called globally.

### 2️⃣ Cleaner Structure
- Related logic stays grouped together.
- Makes the code more organized.

### 3️⃣ Hide Helper Functions
- If a function is only needed inside another function,
  there is no need to define it globally.

---

## 🚀 Real Backend Usage

In backend APIs, inner functions are commonly used for:

- Validation helpers
- Formatting helpers
- Small reusable logic inside endpoints

---

## 💡 What Improved Today

- Better understanding of scope
- Cleaner code structuring techniques
- Writing more controlled and modular functions