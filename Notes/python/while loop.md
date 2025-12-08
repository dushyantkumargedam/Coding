## 🔁 Python Loops: `while` and `for`

Loops are essential control flow structures that allow you to execute a block of code repeatedly. Python primarily uses two types of loops: the **`while` loop** and the **`for` loop**.

-----

## 1\. The `while` Loop

### Definition and Example

The `while` loop is used to execute a block of code **as long as a specific condition is true**. The loop will keep iterating, checking the condition before each cycle, until the condition evaluates to `False`.

**Crucial Note:** You must ensure that something inside the loop modifies the condition's variables, otherwise, you will create an **infinite loop**.

```python
# Initialization (start condition)
count = 1

# Loop Condition: continues as long as count is less than or equal to 5
while count <= 5: 
    print(count)
    count += 1 # Modification (ensures the loop eventually stops)

# Output: 1, 2, 3, 4, 5
```

-----

## 2\. The `for` Loop

The `for` loop is used for **iterating over a sequence** (like a list, tuple, dictionary, set, or string) or other iterable objects. This is the most common loop type for traversing data structures.

### Example: Iterating over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output: apple, banana, cherry
```

### The `range()` Function

The `range()` function is often used with the `for` loop to iterate a specific number of times. It generates a sequence of numbers.

  * `range(stop)`: Generates numbers from 0 up to (but not including) `stop`.
  * `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.
  * `range(start, stop, step)`: Generates numbers with a specified increment.

<!-- end list -->

```python
# Loop 5 times (0, 1, 2, 3, 4)
for i in range(5):
    print(f"Iteration {i}")
```

-----

## 3\. Loop Control Statements

These statements allow you to change the execution flow from its normal sequence within a loop.

### The `break` Statement

The **`break`** statement immediately **stops the entire loop** (both `while` and `for`) and execution jumps to the first line of code *after* the loop block.

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break # Stops the loop entirely when i is 3
    i += 1
# Output: 1, 2, 3
```

### The `continue` Statement

The **`continue`** statement stops the **current iteration** of the loop and jumps to the next iteration (it checks the condition again for a `while` loop, or moves to the next item for a `for` loop). The code below the `continue` is skipped for that cycle.

```python
for x in range(5): # 0, 1, 2, 3, 4
    if x % 2 == 0: # Checks if x is even
        continue # Skips the print statement for even numbers
    print(x)
# Output: 1, 3
```

-----

## 4\. The `else` Statement with Loops

Python allows an optional **`else`** block to be used with both `for` and `while` loops.

### How the `else` Statement Works

The code block in the `else` statement is executed **if the loop completes without being terminated by a `break` statement**.

| Condition | Action |
| :--- | :--- |
| **Normal Completion** | The `else` block **executes**. |
| **Terminated by `break`** | The `else` block is **skipped**. |

### Example with `for` loop

```python
data = [1, 2, 3]

for item in data:
    if item == 10:
        print("Found it!")
        break
else:
    print("Loop finished without finding the item.")
# Output: Loop finished without finding the item.
```