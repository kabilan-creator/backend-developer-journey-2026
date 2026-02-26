Day 01 – Functions & Functional Programming
Topics Covered

Basic Functions

return statement

*args

**kwargs

Lambda function

map()

filter()

reduce()

Key Concepts
*args (Arbitrary Arguments):

Uses a single asterisk (*) to prefix the parameter.

It packs all passed non-keyword arguments into a tuple, allowing the function to handle any number of inputs.

While args is the conventional naming, any name can be used as long as the asterisk is present (e.g., *nums).

**kwargs (Arbitrary Keyword Arguments):

Uses a double asterisk (**) to prefix the parameter.

It packs all passed keyword arguments (e.g., city="Detroit") into a dictionary.

Combining *args and **kwargs:

You can use both in a single function to accept a mix of arbitrary positional and keyword arguments.

Important Rule: When defining the function parameters, *args must come before **kwargs, or a syntax error will occur.


🧠 1️⃣ Basic Function
def greet(name):
    return f"Hello {name}"
What I Understood

=> Function helps reuse logic.

=> return sends value back.

=> Backend APIs mainly use return, not print.

🧠 2️⃣ *args
def add(*args):
    return sum(args)
Understanding

=> *args collects multiple positional arguments.

=> Stored as tuple.

=> Useful when number of inputs is unknown.

🧠 3️⃣ **kwargs
def user_info(**kwargs):
    return kwargs
Understanding

=> **kwargs collects keyword arguments.

=> Stored as dictionary.

=> Used when passing dynamic data.

🧠 4️⃣ Lambda Function
square = lambda x: x * x
print(square(5))
Understanding

=> Anonymous function.

=> Used for short temporary logic.

=> Mostly used with map/filter.

🧠 5️⃣ map()
numbers = [1,2,3]
result = list(map(lambda x: x*x, numbers))
Understanding

=> Applies function to each element.

=> Returns iterator.

=> Need list() to see result.

🧠 6️⃣ filter()
numbers = [1,2,3,4]
even = list(filter(lambda x: x % 2 == 0, numbers))
Understanding

=> Filters elements based on condition.

=> Returns iterator.

🧠 7️⃣ reduce()
from functools import reduce

numbers = [1,2,3,4]
total = reduce(lambda x,y: x+y, numbers)
Understanding

Reduces list into single value.

Used for accumulation logic.

🔥 What I Improved Today

Better understanding of argument handling.

Learned difference between args and kwargs.

Understood functional programming basics.