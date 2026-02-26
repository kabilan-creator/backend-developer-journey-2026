An inner function is a function defined inside another function.
It can only be used within the outer function and is not directly accessible from outside.

In simple words:

It is a “private helper function” inside another function.

Here:

inner() exists only inside outer()

You cannot call inner() directly from outside

Why Do We Use Inner Functions?
1️⃣ Encapsulation

We hide helper logic so it cannot be accessed accidentally from outside.

Why this is good design?

=> clean_data() cannot be called from outside
=> Keeps namespace clean
=> Improves readability
=> in backend APIs, this is used for:
=> validation helpers
=> formatting helpers
=> small reusable logic inside endpoints

2️⃣ Cleaner Structure

Related logic stays grouped together.

3️⃣ Hide Helper Functions

If a function is only needed inside another function, there’s no reason to define it globally.

