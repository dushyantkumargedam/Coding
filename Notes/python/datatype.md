## 🐍 Python Data Types and Casting Notes

## 1\. Built-in Data Types Overview

Python has several built-in categories of data types. These types define the kind of value an object holds, and what operations can be performed on it.

| Category | Type (Class) | Example | Description |
| :--- | :--- | :--- | :--- |
| **Text** | `str` (String) | `"Hello World"` | Sequence of Unicode characters. |
| **Numeric** | `int`, `float`, `complex` | `5`, `5.0`, `5 + 2j` | Whole numbers, decimals, and imaginary numbers. |
| **Sequence** | `list`, `tuple`, `range` | `[1, 2]`, `(1, 2)`, `range(6)` | Ordered collections of objects. |
| **Mapping** | `dict` (Dictionary) | `{"name": "Alice"}` | Unordered collections of key-value pairs. |
| **Set** | `set`, `frozenset` | `{1, 2, 3}` | Unordered collections of unique items. |
| **Boolean** | `bool` | `True`, `False` | Logical values used in conditional statements. |

-----

## 2\. Checking the Data Type

You can determine the data type of any object (variable) by using the built-in **`type()`** function.

```python
x = "Data Science"
y = 100
z = 5.5

print(type(x)) # Output: <class 'str'>
print(type(y)) # Output: <class 'int'>
print(type(z)) # Output: <class 'float'>
```

-----

## 3\. Numeric Types

Python's core numeric types are used to store numerical values.

### 3.1. `int` (Integer)

  * Represents **whole numbers**, positive or negative, without a decimal point.
  * The size of an integer is **limited only by the available memory** of the machine (it has arbitrary precision).
    ```python
    a = 100
    b = -50
    ```

### 3.2. `float` (Floating Point Number)

  * Represents numbers with a **decimal point**.
  * Can also be used for scientific notation, using 'e' to indicate the power of 10.
    ```python
    c = 3.14159
    d = 1.2e5 # same as 120000.0
    ```

### 3.3. `complex` (Complex Number)

  * Represents complex numbers in the form **$a + bj$**, where $a$ is the real part and $b$ is the imaginary part, denoted by $j$.
    ```python
    e = 5 + 3j
    ```

-----

## 4\. Random Numbers

Python does not have a built-in function to generate random numbers directly, but it relies on the **`random` module**. You must first **import** this module.

The `random` module offers several functions:

  * **`random.random()`**: Returns a **random float** $x$ such that $0.0 \le x < 1.0$.
  * **`random.randint(a, b)`**: Returns a **random integer** $N$ such that $a \le N \le b$ (inclusive).
  * **`random.choice(sequence)`**: Returns a randomly chosen element from a non-empty sequence.

<!-- end list -->

```python
import random # Must be imported before use

# Generate a random float between 0.0 and 1.0
print(random.random())

# Generate a random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))
```

-----

## 5\. Python Casting (Type Conversion)

**Casting** is the process of converting a variable from one data type to another. This is often necessary when working with external data or ensuring the correct type for a mathematical operation.

Python uses constructor functions for casting:

| Function | Purpose | Example | Result |
| :--- | :--- | :--- | :--- |
| **`int()`** | Constructs an integer number. | `int(3.14)` | `3` (truncates decimal) |
| **`float()`** | Constructs a float number. | `float(5)` | `5.0` |
| **`str()`** | Constructs a string from the input. | `str(100)` | `"100"` |

### Key Casting Notes:

  * **Float to Int:** Casting a float to an integer will **truncate** the decimal part (it does not round).
  * **String to Number:** The string must contain a **valid** representation of the number (e.g., you cannot cast the string `"hello"` to an `int`).

<!-- end list -->

```python
x = 1.9    # float
y = "10"   # string

# Casting to Integer
a = int(x) # a is now 1 (int)
b = int(y) # b is now 10 (int)

# Casting to Float
c = float(b) # c is now 10.0 (float)

print(a, c) # Output: 1 10.0
```