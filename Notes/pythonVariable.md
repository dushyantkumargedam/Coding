### 1\. Print Without a New Line

By default, the built-in `print()` function automatically adds a newline character (`\n`) after displaying its output.

To print multiple outputs on the **same line**, you can use the **`end`** parameter and set it to a different character, or an empty string, instead of the default newline character.

```python
# Example of using the 'end' parameter
print("This is the first part.", end=" ") # Notice the space inside the quotes
print("This is the second part.", end="***") 
print("This is the final part.") 

# Output: This is the first part. This is the second part.***This is the final part.
```

-----

### 2\. Getting the Data Type

The built-in **`type()`** function is used to determine the data type (class) of a variable, value, or object. This is crucial for understanding how data is stored and manipulated.

```python
x = 5             # Integer
y = "Hello"       # String
z = 3.14          # Float
my_list = [1, 2]  # List

print(type(x))        # Output: <class 'int'>
print(type(y))        # Output: <class 'str'>
print(type(z))        # Output: <class 'float'>
print(type(my_list))  # Output: <class 'list'>
```

-----

### 3\. Python Variable Naming Rules

Variables can have short names (like `i` or `n`) or descriptive names (like `user_age` or `file_path`). Adhering to conventions (e.g., lowercase with underscores for multi-word names, known as **snake\_case**) improves readability.

#### Rules for Valid Variable Names:

1.  A variable name **must start with a letter** (`A-z`) or the **underscore character** (`_`).
2.  A variable name **cannot start with a number** (`0-9`).
3.  A variable name can only contain **alpha-numeric characters** and **underscores** (`A-z`, `0-9`, and `_`).
4.  Variable names are **case-sensitive** (`age`, `Age`, and `AGE` are considered three different variables).
5.  A variable name **cannot be any of the Python keywords** (e.g., `for`, `if`, `while`, `def`, `class`).

| Valid Examples | Invalid Examples |
| :--- | :--- |
| `myVar` | `1_var` (Starts with a number) |
| `__private_name` | `my-var` (Contains a hyphen) |
| `TotalVolume` | `for` (Is a keyword) |

-----

### 4\. Unpack a Collection

**Unpacking** is a convenient feature that allows you to extract all the values from an iterable collection (like a list or a tuple) directly into separate variables in a single line.

*The number of variables on the left side **must exactly match** the number of elements in the collection on the right side.*

```python
# Unpacking a Tuple
colors = ("red", "green", "blue")
(c1, c2, c3) = colors # Assigns "red" to c1, "green" to c2, etc.

print(c1)  # Output: red

# Unpacking a List
coordinates = [10.5, 20.2]
x, y = coordinates

print(y)   # Output: 20.2
```

-----

### 5\. Python Global Variables (Scope)

A variable's **scope** determines where it is accessible in your code.

  * **Local Variables:** Created inside a function and are only accessible from within that function.
  * **Global Variables:** Created in the main body of the code and are accessible both inside and outside any function.

#### Using `global` Keyword

By default, when you try to assign a value to a variable inside a function, Python creates a new **local** variable with that name.

To modify an **existing global variable** from within a function, you must use the **`global` keyword**.

```python
# Global variable
counter = 10 

def increment_counter():
    # We explicitly tell Python we want to modify the global 'counter'
    global counter 
    counter = counter + 1 # Modifies the global variable

def check_counter():
    # Accesses the global variable without modification
    print(f"Counter inside check_counter: {counter}")

increment_counter()
print(f"Counter after increment: {counter}") # Output: 11
check_counter()                             # Output: Counter inside check_counter: 11
```