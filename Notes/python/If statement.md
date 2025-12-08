## 🔀 Python Flow Control: If Statements

Python's flow control allows your programs to make decisions and execute code conditionally using **comparison operators** and **`if` statements**.

-----

## 1\. The `if` Statement and Indentation

The `if` statement evaluates a **condition** (an expression using comparison operators like $a == b$, $a < b$, etc.) that results in either `True` or `False`.

  * If the condition is **`True`**, the code block immediately following the `if` statement is executed.
  * If the condition is **`False`**, the code block is skipped.

### Comparison Operators (Conditions)

| Operator | Description |
| :--- | :--- |
| `==` | Equals |
| `!=` | Not Equals |
| `<` | Less than |
| `<=` | Less than or equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |

### Indentation (Meaning)

In Python, **indentation** (typically 4 spaces) is mandatory and critical. It defines the **scope** or **code block** belonging to the `if` statement (or any control structure like loops or functions).

  * Code within the same indented block is executed together if the condition is met.
  * The block ends when the indentation returns to the previous level.

<!-- end list -->

```python
x = 10
y = 5

if x > y: # Condition is True
    # Start of the code block (Indented)
    print("x is greater than y")
    print("This is a multiple statement in the if block")
    # End of the code block
print("This runs regardless of the condition.")
```

-----

## 2\. The `elif` Keyword

The `elif` (short for "else if") keyword allows you to check **multiple conditions** sequentially after the initial `if` statement has failed.

### How `elif` Works

  * The Python interpreter checks the `if` condition first.
  * If the `if` condition is `False`, it moves to the first `elif`.
  * If that `elif` condition is `True`, its code block is executed, and the entire `if`-`elif`-`else` chain **terminates** (no further `elif` or `else` checks are performed).
  * If the `elif` is `False`, it moves to the next `elif`, and so on.

### When to Use `elif`

Use `elif` when you have **more than two mutually exclusive possibilities** and you need to test them in a specific order.

```python
grade = 75

if grade >= 90:
    print("A")
elif grade >= 80: # Checked only if grade < 90
    print("B")
elif grade >= 70: # Checked only if grade < 80
    print("C")
# Output: C
```

-----

## 3\. The `else` Keyword

The `else` keyword catches any condition that was **not caught** by the preceding `if` and `elif` statements.

### How `else` Works

  * The `else` block executes **only if all preceding conditions** (`if` and any `elif` statements) in the chain evaluate to `False`.
  * It acts as a **fallback** or a default action.

### Complete If-Elif-Else Chain

The `else` block is optional, but creates a complete decision chain:

```python
hour = 17

if hour < 12:
    print("Morning")
elif hour < 18:
    print("Afternoon")
else: # Executed if neither hour < 12 NOR hour < 18 is True
    print("Evening")
# Output: Afternoon
```

### `else` Without `elif`

You can use `else` directly after an `if` statement if you only have two outcomes:

```python
age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")
# Output: Minor
```

-----

## 4\. Short Hand If (Ternary Operator)

Python offers concise syntax for simple `if` and `if-else` statements, often referred to as the **Ternary Operator**.

### Short Hand If

If you have only one statement to execute when the condition is `True`:

$$\text{statement if condition else\_statement (optional)}$$

```python
a = 20
b = 10
if a > b: print("A is greater")
```

### Short Hand If ... Else

The entire `if-else` logic is placed on one line, and it can be used to **assign a value** based on the condition.

$$\text{value\_if\_true if condition else value\_if\_false}$$

```python
score = 90
status = "Pass" if score >= 70 else "Fail"
print(status) # Output: Pass
```

### When to Use Shorthand If

Use it when the logic is very simple and readable; avoid it for complex logic as it reduces clarity.

-----

## 5\. Python Logical Operators

Logical operators combine multiple conditional statements to form complex checks.

[Image of a Truth table for logical operators AND OR NOT]

| Operator | Description | Example |
| :--- | :--- | :--- |
| **`and`** | Returns `True` if **both** conditions are true. | `age > 18 and city == "NYC"` |
| **`or`** | Returns `True` if **at least one** condition is true. | `day == "Sat" or day == "Sun"` |
| **`not`** | Reverses the result. | `not(age > 18)` (True if age is NOT greater than 18) |

### Combining Multiple Operators

You can use multiple conditions and operators on a single line. Use **parentheses** `()` for clarity and to control the order of evaluation.

```python
temp = 25
raining = False

if temp > 20 and not raining:
    print("Go outside!")
```

-----

## 6\. Nested If Statements

**Nested `if` statements** involve placing an `if` statement *inside* the code block of another `if` or `elif` statement.

### How Nested If Works

The inner `if` statement is only evaluated and executed **if the outer condition is already `True`**.

```python
num = 15

if num > 10:
    print("Number is greater than 10")
    if num > 20: # This inner check only runs if num > 10
        print("Number is also greater than 20")
    else:
        print("Number is between 10 and 20")
# Output:
# Number is greater than 10
# Number is between 10 and 20
```

### Nested If vs. Logical Operators

  * **Logical Operators (`and`):** Generally preferred for simple, clear logic because they are more concise and often more efficient.
      * *Example:* `if num > 10 and num < 20:`
  * **Nested `if`:** Useful when the action taken in the inner block depends on the outer condition, or when the conditions are complex and sequencing is necessary.

-----

## 7\. The `pass` Statement

An `if` statement (like loops, functions, and classes) **cannot be empty** in Python; it must contain at least one statement.

### The `pass` Statement

If you need a placeholder for an `if` statement (or any other block) where you haven't written the code yet, use the **`pass` statement** to avoid a syntax error.

  * `pass` is a null operation; nothing happens when it executes.

### Why Use `pass`?

  * **Prototyping:** Allows you to sketch out the structure of your code without writing the implementation details immediately.
  * **Placeholder:** Use it when you deliberately want to skip an action for a specific condition.

<!-- end list -->

```python
if day == "Saturday":
    pass # To be implemented later: add weekend logic
elif day == "Sunday":
    print("Relax!")
else:
    print("Work day.")
```

### `pass` in Other Contexts

The `pass` statement can be used anywhere a statement is syntactically required but you need to do nothing, such as inside function definitions, class definitions, or loops.