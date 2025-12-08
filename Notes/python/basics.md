## 🐍 Python Fundamentals Notes

These notes cover the core concepts of Python required for a strong foundation: built-in data structures, flow control, and functions.

-----

## 1\. Data Structures (Collections)

Python offers several built-in structures for storing collections of data, each with unique characteristics related to **Order**, **Mutability**, and **Uniqueness**.

| Data Structure | Delimiter | Order | Mutability (Can be changed?) | Duplicates | Key Characteristics |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[ ]` | **Ordered** | **Mutable** | Allowed | Versatile, general-purpose collection. Supports indexing, slicing, and methods like `append()`, `pop()`. |
| **Tuple** | `( )` | **Ordered** | **Immutable** | Allowed | Used for fixed data (e.g., coordinates, record data). Faster than lists. Can be used as dictionary keys. |
| **Set** | `{ }` | **Unordered** | **Mutable** | **NO** (only unique) | Ideal for membership testing and mathematical set operations (union, intersection, difference). |
| **Dictionary (Dict)** | `{ }` | **Ordered** (from Python 3.7+) | **Mutable** | Keys are unique; Values can be duplicated. | Stores data in **key-value pairs**. Keys must be immutable (e.g., strings, numbers, tuples). Fast lookup by key. |

### Quick Examples:

```python
my_list = [1, "two", 3.0] # List: Mutable, Ordered
my_list.append(4)         # Valid

my_tuple = (10, 20, 30)   # Tuple: Immutable, Ordered
# my_tuple[0] = 5         # Invalid operation - will cause error

my_set = {1, 2, 2, 3}     # Set: Mutable, Unordered, Unique
# Result: {1, 2, 3}

my_dict = {"name": "Alice", "age": 30} # Dictionary: Mutable, Key-Value
print(my_dict["name"])    # Output: Alice
```

-----

## 2\. Flow Control (Decision Making & Loops)

Flow control statements dictate the order in which a program's code is executed.

### A. Conditional Statements (Selection)

Used to execute specific blocks of code based on whether a **Boolean condition** (`True` or `False`) is met.

| Statement | Purpose | Syntax Example |
| :--- | :--- | :--- |
| **`if`** | Executes a code block if the condition is **True**. | `if x > 10: \n    # code block` |
| **`elif`** | Checks an additional condition if the preceding `if`/`elif` conditions were **False**. | `elif x > 5: \n    # code block` |
| **`else`** | Executes a code block if **all** preceding `if`/`elif` conditions were **False**. | `else: \n    # code block` |

> **Key Rule:** Python uses **indentation** (typically 4 spaces) to define code blocks (Scope).

### B. Iteration Statements (Loops)

Used to repeat a block of code multiple times.

| Statement | Purpose | Syntax Example |
| :--- | :--- | :--- |
| **`for`** | Iterates over the items of any **sequence** (list, tuple, dictionary, string) or other iterable objects. | `for item in my_list: \n    print(item)` |
| **`while`** | Repeats a block of code as long as a specified Boolean **condition remains `True`**. | `count = 0 \nwhile count < 5: \n    print(count) \n    count += 1` |

### C. Jump Statements

  * **`break`**: Immediately exits the current loop entirely.
  * **`continue`**: Skips the rest of the current iteration and moves to the next one.
  * **`pass`**: A null operation; used as a placeholder where a statement is syntactically required but you don't want to execute any code.

-----

## 3\. Functions

Functions are blocks of reusable code that perform a specific task, promoting modularity and code reuse.

| Concept | Description | Syntax Example |
| :--- | :--- | :--- |
| **Definition** | Declared using the **`def`** keyword, followed by the function name, parameters in parentheses, and a colon. | `def calculate_sum(a, b):` |
| **Parameters** | Variables listed in the function definition. They receive values (arguments) when the function is called. | `def greet(name):` |
| **`return`** | The statement used to **exit** a function and **send a value** back to the caller. | `return a + b` |
| **Return Value** | A function returns the special value **`None`** by default if no `return` statement is used or if `return` is used without a value. A function can return multiple values, which Python handles as a single tuple. | `return mean, median` |

### Function Example

```python
# Function Definition
def is_even(number):
    """Checks if a number is even.""" # Docstring (documentation)
    if number % 2 == 0:
        return True # Returns a boolean value
    else:
        return False # Exits the function

# Function Call
result = is_even(4)
print(result) # Output: True

# Function returning None
def print_hello(name):
    print(f"Hello, {name}!")

test = print_hello("Bob")
print(test) # Output: Hello, Bob! (then) None
```

The video below introduces the concept of control structures, which are essential for understanding how to use `if`, `for`, and `while` statements effectively in Python.

[If and While (Control Structures) - Python Like a Pro \#7](https://www.youtube.com/watch?v=s9nR1xxfeNU)

http://googleusercontent.com/youtube_content/0
