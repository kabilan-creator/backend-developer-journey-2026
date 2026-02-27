# Day – Scope, nonlocal & Closures Deep Dive

## 🧠 Topics Covered Today

---

## 1️⃣ LEGB Rule (Scope Resolution)

### What I Learned

Python resolves variables in this strict order:

- **L** – Local  
- **E** – Enclosing  
- **G** – Global  
- **B** – Built-in  

### Key Understanding

- Python searches variables following the LEGB order.
- Scope is determined at compile time.
- If a variable is assigned inside a function, Python treats it as **local by default**.

---

## 2️⃣ UnboundLocalError

### What I Understood

This error happens when:

- Python marks a variable as local (because of assignment).
- But the variable is accessed before it is assigned.

### Important Insight

- Reading outer variable → ✅ Works
- Modifying outer variable without `nonlocal` → ❌ Error

---

## 3️⃣ nonlocal Keyword

### Purpose

- Used inside nested functions.
- Allows modification of variables from the enclosing scope.
- Prevents Python from creating a new local variable.

### Rule I Learned

- Reading outer variable → No need for `nonlocal`
- Modifying outer variable → Must use `nonlocal`

### Difference Clarified

- `global` → Modifies global variable
- `nonlocal` → Modifies enclosing function variable

---

## 4️⃣ Closures (Core Concept)

### What I Understood

A closure is:

> A function that remembers variables from its enclosing scope even after the outer function finishes execution.

### Key Insight

- Inner function retains access to outer variables.
- Outer function memory is preserved if the inner function uses it.

---

## 5️⃣ Closure Memory Internals

### Deep Understanding Gained

- Closure variables are stored inside **cell objects**.
- They are accessible via `function.__closure__`.
- These variables are attached to the returned function object.

### Important Realization

Closure memory:
- Is not global.
- Is attached specifically to the returned inner function.

---

## 6️⃣ Independent Closure Instances

### What I Clearly Understood

Each time the outer function runs:

- A new closure memory environment is created.
- Each returned function has its own independent state.

Example understanding:

Two counters created from the same outer function  
→ Do NOT share memory.

---

# 🚀 Why This Knowledge Matters

This is important for:

- Writing decorators
- Understanding FastAPI dependencies
- Middleware logic
- Function factories
- State management without classes

---

# 💡 Personal Understanding Level Today

✔ Strong understanding of LEGB  
✔ Clear about when to use `nonlocal`  
✔ Understood closure memory behavior  
✔ Understood closure internals (`__closure__`, cell objects)  