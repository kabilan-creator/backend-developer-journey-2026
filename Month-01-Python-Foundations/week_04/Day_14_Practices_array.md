# 📅 Day – Array Mastery & Problem-Solving Patterns

## 📚 What I Learned Today

Today I strengthened my understanding of **array fundamentals and core DSA patterns**, and improved my problem-solving approach from brute force to optimized solutions.

---

## 🔹 1️⃣ Array Basics (Strong Foundation)

### What I Practiced

- Traversal

```python
for num in arr:
    print(num)
```

- Index access

```python
arr[i]
```

- Basic operations

```python
sum(arr)
len(arr)
max(arr)
min(arr)
```

### Status

- Comfortable with basic array operations

---

## 🔹 2️⃣ Comparison Logic (Major Improvement)

### Understanding

- “Do I want bigger?” → use `>`
- “Do I want smaller?” → use `<`

### Patterns Practiced

- Maximum element
- Minimum element
- Largest even number
- Smallest positive number

---

## 🔹 3️⃣ Tracking Variables (Core Skill)

### Concept

Maintain values while traversing:

```python
max_so_far = arr[0]
min_so_far = arr[0]
count = 0
```

### Key Learning

- Traverse → Compare → Update

This is a core DSA pattern.

---

## 🔹 4️⃣ Multi-variable Logic (Advanced Step)

### Problems Solved

- Second largest element
- Third largest element

### Key Learning

- Value shifting technique
- Avoid duplicates
- Maintain multiple variables

---

## 🔹 5️⃣ Adjacent Pattern

### Concept

Work with:

```python
arr[i] and arr[i+1]
```

### Problems

- Sorted check
- First increasing pair
- Peak element

---

## 🔹 6️⃣ Brute Force Thinking (Important Step)

### Approach

- Solve first using nested loops
- Try all possibilities

### Example

```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        # check condition
```

### Key Learning

- First solve → then optimize

---

## 🔹 7️⃣ Optimization Thinking (Real Growth)

### Improvement

- From O(n²) → O(n)

### Techniques Learned

- Use `set()` for fast lookup
- Avoid repeated calculations

### Problems

- Two Sum
- Duplicate detection
- Common elements

---

## 🔹 8️⃣ Hashing (Very Important)

### Concepts

- `set()` → fast lookup
- `dict` → frequency counting

### Example

```python
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1
```

### Problems Practiced

- Frequency count
- First non-repeating element
- Duplicates
- Intersection of arrays

---

## 🔹 9️⃣ Advanced Pattern – Boyer-Moore Voting

### Concept

- Candidate selection
- Cancellation logic
- Final verification

### Key Idea

- Efficient majority element detection in O(n) time and O(1) space

---

## 🔹 🔟 Pattern Recognition (Most Important)

### What I Improved

| Problem Type        | Pattern Used        |
|--------------------|--------------------|
| Max / Min          | Comparison         |
| Pair Problems      | Nested / Hashing   |
| Sorted Check       | Adjacent Pattern   |
| Frequency          | HashMap            |
| Majority Element   | Boyer-Moore        |

---

# 🚀 Key Takeaway

Today I improved my ability to:

- Identify patterns in problems
- Move from brute force → optimized solutions
- Use hashing for efficiency
- Think like an interviewer
- Solve array problems with structured logic