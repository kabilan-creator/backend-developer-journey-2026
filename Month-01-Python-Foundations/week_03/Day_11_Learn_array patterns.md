# 📅 Day – Array Patterns & Problem Solving

## 📚 What I Learned Today

Today I practiced important **array patterns** and improved my problem-solving approach.

---

## 🔹 1️⃣ Array Traversal Basics

### Concept
- Loop through array safely
- Avoid index out-of-bound errors

### Mistake I Fixed

```python
for i in range(len(arr)):
    arr[i+1]  # ❌ Index error
```

### Correct Approach

```python
for i in range(len(arr) - 1):
    arr[i+1]
```

### Lesson

- Always check bounds when using `i+1` or `i-1`

---

## 🔹 2️⃣ Min / Max Pattern

### Concept
Track minimum or maximum while iterating

### Example

```python
min_val = arr[0]

for x in arr:
    if x < min_val:
        min_val = x
```

### Lesson

- Always initialize with `arr[0]`, not `0`

---

## 🔹 3️⃣ Min + Max in One Traversal

### Concept
Find both min and max in a single loop

```python
min_val = arr[0]
max_val = arr[0]

for x in arr:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
```

### Lesson

- One loop → multiple results (important optimization)

---

## 🔹 4️⃣ Rotated Array Logic

### Concept
Find the breaking point (pivot)

```python
for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        print("Pivot found at index", i)
```

### Example

```
[4, 5, 6, 7, 1, 2]
              ↑ break point
```

### Lesson

- Rotation = where sorted order breaks

---

## 🔹 5️⃣ Minimum So Far Pattern (Important)

### Concept
Used in:
- Max difference
- Stock profit problems

```python
min_val = arr[0]
max_profit = 0

for x in arr:
    max_profit = max(max_profit, x - min_val)
    min_val = min(min_val, x)
```

### Lesson

- Track minimum value
- Calculate profit forward only
- Never go backward

---

## 🔹 6️⃣ Sliding Window Concept

### Concept
Window = subarray of size `k`

Example:

```
[1, 8, 1, 3], k = 3

[1, 8, 1]
   [8, 1, 3]
```

### Lesson

- Different problems → different approaches

| Problem Type | Technique        |
|-------------|-----------------|
| Sum         | Sliding Window  |
| Max Element | Deque           |

---

## 🔹 7️⃣ Thinking Like an Interviewer

### What Improved Today

- ✔ Understanding constraints
- ✔ Handling edge cases
- ✔ Debugging mistakes
- ✔ Recognizing patterns

---

# 🚀 Key Takeaway

Today I improved my ability to:

- Identify patterns in array problems
- Optimize solutions using single traversal
- Avoid common index mistakes
- Think in a structured, interview-ready way