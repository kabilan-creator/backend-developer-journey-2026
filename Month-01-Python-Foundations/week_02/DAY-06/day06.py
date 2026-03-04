#Stacking Decorators
from functools import wraps

def log(func):
    @wraps(func)    
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def timeit(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log
@timeit 
def compute_square(n):
    return n * n
# Example usage
result = compute_square(10)
print(f"Result: {result}")

#example - 2

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclaim
@uppercase
def greet(name):
    return f"Hello, {name}"

# Example usage
greeting = greet("Alice")

