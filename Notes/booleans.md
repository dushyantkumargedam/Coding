## 🧱 Python Booleans (`bool`)

Booleans represent one of two binary states, which are fundamentally **True** or **False**. This concept is central to all programming logic and control flow.

  * In a numerical context, `True` corresponds to **1**, and \`False\*\* corresponds to **0**.
  * The actual type in Python is `bool`.

-----

### 1\. The `bool()` Function

The built-in **`bool()`** function allows you to evaluate any value or object and return its inherent truthiness: `True` or `False`.

#### Values That Evaluate to `True` (Truthiness)

Almost any value is evaluated to `True` if it contains some form of content or is a non-zero entity.

| Data Type | True Condition | Example | Output |
| :--- | :--- | :--- | :--- |
| **String** | Any string that is **not empty**. | `print(bool("Hello"))` | `True` |
| **Number** | Any number that is **not zero** (positive or negative). | `print(bool(15))` | `True` |
| **Sequence/Collection**| Any list, tuple, set, or dictionary that is **not empty**. | `print(bool([1, 2]))` | `True` |

#### Values That Evaluate to `False` (Falsiness)

The following values are considered **False** when evaluated by `bool()`:

1.  The boolean constant **`False`**.
2.  The number **`0`** (integer, float, or complex).
3.  The empty string **`""`**.
4.  Empty sequences: **`[]`** (list), **`()`** (tuple), **`{}`** (dictionary or set).
5.  The special value **`None`**.
6.  Objects that are made from a class with a special method called **`__len__`** that returns `0` or `False`. (This is an advanced concept for custom classes.)

<!-- end list -->

```python
# Examples of Falsey values
print(bool(0))      # Output: False
print(bool(""))     # Output: False (empty string)
print(bool([]))     # Output: False (empty list)
print(bool(None))   # Output: False
```

-----

### 2\. Functions Can Return a Boolean

In addition to the `bool()` function, functions that perform checks or comparisons inherently return a boolean value (`True` or `False`).

#### Using `isinstance()`

The **`isinstance()`** function is a built-in function used to determine if an object is an instance of a specified data type (class). It returns a boolean result.

```python
x = 200
y = "Python"

# Checks if x is an integer
print(isinstance(x, int))     # Output: True

# Checks if y is a list
print(isinstance(y, list))    # Output: False
```