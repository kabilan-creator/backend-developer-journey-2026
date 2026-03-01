# 📅 Day 05 – Advanced Python Decorators & Exception Handling

## 📚 What I Learned Today

Today I moved beyond basic decorators and understood how they work in real backend systems.

---

## 🔹 1️⃣ Decorator with Arguments

When a decorator needs parameters, it must use a 3-layer structure:

- Outer function → accepts decorator arguments  
- Middle function → accepts original function  
- Inner wrapper → executes modified behavior  

Example:

```python
def decorator(arg):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

Usage:

```python
@decorator("test")
def greet():
    print("Hello")
```

Internally becomes:

```python
greet = decorator("test")(greet)
```

This helped me clearly understand how Python rewrites decorated functions.

---

## 🔹 2️⃣ Stacking Decorators

```python
@decorator_one
@decorator_two
def my_function():
    pass
```

Internally:

```python
my_function = decorator_one(decorator_two(my_function))
```

### Important Understanding

- Wrapping happens bottom → top  
- Execution happens top → bottom  

This clarified execution order confusion.

---

## 🔹 3️⃣ Custom Authentication Decorator

I built a simple role-based access decorator:

```python
from functools import wraps

def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                raise PermissionError("Unauthorized access")
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator
```

This simulates real backend permission systems.

---

## 🔹 4️⃣ Understanding Python Exceptions Properly

I encountered this error:

```
TypeError: exceptions must derive from BaseException
```

From this, I learned:

- Only classes derived from `BaseException` can be raised
- Python is case-sensitive (`Exception` ≠ `exception`)
- How to create custom exception classes
- Why raising generic exceptions is not ideal in production

Example custom exception:

```python
class UnauthorizedError(Exception):
    pass
```

Using try/except:

```python
try:
    risky_function()
except UnauthorizedError as e:
    print("Access denied:", e)
```

---

## 🔹 5️⃣ Rate Limiter Concept

I implemented a basic rate limiter decorator:

```python
import time
from functools import wraps

def rate_limiter(limit, window_seconds):
    calls = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()

            # Remove expired calls
            while calls and current_time - calls[0] > window_seconds:
                calls.pop(0)

            if len(calls) >= limit:
                raise Exception("Rate limit exceeded")

            calls.append(current_time)
            return func(*args, **kwargs)

        return wrapper
    return decorator
```

This is how APIs prevent abuse and brute-force attacks.

---

## 🔹 6️⃣ Async Decorator Basics

If original function is async, wrapper must also be async.

```python
from functools import wraps

def async_logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print("Before async function")
        result = await func(*args, **kwargs)
        print("After async function")
        return result
    return wrapper
```

Async decorators are essential in FastAPI-style systems.

---

# 🧠 Core Concepts Strengthened Today

✔ Function wrapping mechanism  
✔ Closure behavior in decorators  
✔ Execution order clarity  
✔ Role-based access control logic  
✔ Proper exception handling  
✔ Backend-style control flow  
✔ Sync vs Async decorator differences  