## 🔁 Python `for` Loop

The `for` loop is used for **iteration**—that is, repeating a block of code for every item in a sequence or other iterable object. It's the standard way to traverse data structures in Python.

-----

### 1\. Definition and Example

A `for` loop executes a code block for each element in an iterable object (like a list, tuple, string, or range).

**Syntax:**

```python
for item in iterable:
    # code block to execute for each item
```

**Example:** Looping through a list.

```python
data_list = ["apple", "banana", "cherry"]

for fruit in data_list:
    print(fruit)
# Output: apple, banana, cherry
```

-----

### 2\. Looping Through a String

A string is a sequence of characters, making it an iterable. A `for` loop will iterate through each character in the string.

```python
name = "Python"

for char in name:
    print(char)
# Output: P, y, t, h, o, n (each on a new line)
```

-----

### 3\. The `range()` Function

The `range()` function is often used to iterate a specific number of times. It generates an immutable sequence of numbers and is iterable.

  * `range(stop)`: Generates numbers starting from **0** up to (but not including) `stop`.
  * `range(start, stop)`: Generates numbers from `start` up to (but not not including) `stop`.
  * `range(start, stop, step)`: Generates numbers with the specified `step` (increment/decrement).

<!-- end list -->

```python
# Looping by index using range() and len()
my_list = ['A', 'B', 'C']

for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")
# Output: Index 0: A, Index 1: B, Index 2: C
```

-----

### 4\. Loop Control Statements

#### The `break` Statement

The **`break`** statement immediately **stops the entire loop** and execution jumps to the first line of code *after* the loop block. It's typically used when a specific condition is met and no further iteration is needed.

```python
for x in [10, 20, 30, 40]:
    if x == 30:
        break # Stops the loop entirely
    print(x)
# Output: 10, 20
```

#### The `continue` Statement

The **`continue`** statement stops the **current iteration** of the loop and jumps immediately to the next item in the sequence. The code below `continue` within the loop body is skipped for that cycle.

```python
for number in [1, 2, 3, 4, 5]:
    if number % 2 == 0:
        continue # Skips the print statement for even numbers
    print(number)
# Output: 1, 3, 5
```

-----

### 5\. Nested Loops

A **nested loop** is a loop placed inside the body of another loop. The inner loop executes completely for every single iteration of the outer loop.

```python
adj = ["red", "big"]
fruits = ["apple", "banana"]

for a in adj:       # Outer loop iterates 2 times
    for f in fruits:  # Inner loop iterates 2 times for each outer iteration (2*2 = 4 total prints)
        print(a, f)
# Output: red apple, red banana, big apple, big banana
```

-----

### 6\. The `else` in `for` Loop

The `else` block associated with a `for` loop is executed **if and only if the loop completes normally**, meaning it did **not** encounter a **`break`** statement.

```python
items = [1, 5, 8]

for item in items:
    if item == 10:
        print("Found the target!")
        break
else:
    # This executes because 'break' was NOT called
    print("Target item not found in the list.")

# Output: Target item not found in the list.
```

-----

### 7\. The `pass` Statement

The **`pass`** statement is a null operation. When a statement is syntactically required (like within a loop body), but you have no code to execute yet, you can use `pass` to avoid a syntax error.

```python
for letter in "analysis":
    if letter == 'a':
        pass # Placeholder: will add special logic later
    else:
        print(letter)
```