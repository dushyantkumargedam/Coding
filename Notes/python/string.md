## 🐍 Python Strings

Strings (`str`) are one of the most fundamental data types in Python. They are sequences of characters and are **immutable** (cannot be changed after creation).

-----

### 1\. String Creation and Multi-line Strings

Strings can be created using either single quotes (`'...'`) or double quotes (`"..."`).

#### Multiline Strings

To define a string that spans multiple lines, you can use **three quotes** (triple quotes) – either three single quotes (`'''...'''`) or three double quotes (`"""..."""`). The line breaks are included in the string value.

```python
multiline_str = """
This is a string 
that spans
three lines.
"""
```

-----

### 2\. Strings as Arrays and Indexing

Python does not have a separate character data type; a single character is simply a string of length 1.

Strings are treated as **arrays (sequences)** of characters. You can access elements (characters) using square brackets `[]`.

  * **Indexing:** Starts at `0` for the first character.
    ```python
    my_string = "PYTHON"
    print(my_string[0]) # Output: P
    print(my_string[4]) # Output: O
    ```

#### Negative Indexing

Negative indexing allows you to start the count from the **end** of the string:

  * `-1` refers to the **last character**.
  * `-2` refers to the second-to-last character, and so on.
    ```python
    my_string = "PYTHON"
    print(my_string[-1]) # Output: N
    print(my_string[-6]) # Output: P
    ```

-----

### 3\. String Length and Slicing

#### String Length

The built-in **`len()`** function returns the number of characters in a string.

```python
text = "Prescriptive"
print(len(text)) # Output: 12
```

#### Slicing Strings

Slicing allows you to return a range of characters using the syntax: `[start:end:step]`.

  * **`start`:** The index where the slice begins (inclusive).
  * **`end`:** The index where the slice ends (**exclusive**).
  * If omitted, `start` defaults to `0`, and `end` defaults to the string length.

<!-- end list -->

```python
s = "Optimization"
print(s[0:4])   # Output: Opti (From index 0 up to, but not including, index 4)
print(s[4:])    # Output: mization (From index 4 to the end)
print(s[:4])    # Output: Opti (From the start up to index 4)
print(s[2:10:2])# Output: piat (Every 2nd character from index 2 to 9)
```

-----

### 4\. Check String (`in` and `not in`)

You can check for the presence or absence of a specific substring or character within a string using the keywords **`in`** and **`not in`**. These checks return a Boolean result (`True` or `False`).

| Keyword | Purpose | Example | Result |
| :--- | :--- | :--- | :--- |
| **`in`** | To check if a phrase or character is **present**. | `"data" in "data science"` | `True` |
| **`not in`** | To check if a phrase or character is **not present**. | `"ML" not in "data science"` | `True` |

-----

### 5\. Python - Modify Strings (Methods)

Since strings are immutable, these "modification" methods actually return a **new string** with the changes applied.

| Method | Purpose | Example | Result |
| :--- | :--- | :--- | :--- |
| **`.upper()`** | Converts all characters to **upper case**. | `"hello".upper()` | `"HELLO"` |
| **`.lower()`** | Converts all characters to **lower case**. | `"WORLD".lower()` | `"world"` |
| **`.strip()`** | Removes any leading (start) and trailing (end) **whitespace**. | `"  Python  ".strip()` | `"Python"` |
| **`.replace(old, new)`** | Replaces all occurrences of a specified substring with another. | `"P ython".replace(" ", "")` | `"Python"` |
| **`.split(separator)`** | Splits the string into a **list** of substrings based on a specified separator (default is whitespace). | `"A,B,C".split(",")` | `['A', 'B', 'C']` |

-----

### 6\. Concatenation

To **concatenate**, or combine, two or more strings, you use the standard addition operator **`+`**.

```python
first = "Hello"
last = "World"
full = first + " " + last # Notice the space added explicitly
print(full) # Output: Hello World
```

-----

### 7\. F-Strings (Formatted String Literals)

**F-strings** (introduced in Python 3.6) are the **most modern, readable, and preferred way** to format and embed expressions inside string literals.

You prefix the string with the letter **`f`** or **`F`**. Variables and expressions are then placed inside **curly braces `{}`** within the string.

```python
name = "Gemini"
age = 1
result = 10 * 5

# Using F-string for embedding variables and expressions
greeting = f"My name is {name}, I am {age} year old, and 10 * 5 equals {result}."
print(greeting) 
# Output: My name is Gemini, I am 1 year old, and 10 * 5 equals 50.

# F-strings support method calls and formatting:
pi_value = 3.14159265
formatted = f"Pi rounded to two decimal places is: {pi_value:.2f}"
print(formatted)
# Output: Pi rounded to two decimal places is: 3.14
```

-----

### 8\. Escape Character

To insert characters that are illegal in a string (e.g., a double quote inside a double-quoted string), you use an **escape character**, which is the **backslash (`\`)**.

The backslash is followed by the character you want to insert. Common escape sequences include:

| Sequence | Result | Description |
| :--- | :--- | :--- |
| `\'` | `'` | Single Quote |
| `\"` | `"` | Double Quote |
| `\\` | `\` | Backslash |
| `\n` | New Line | Inserts a line break |
| `\t` | Tab | Inserts a tab stop |

```python
escaped_str = "The file path is C:\\Users\\Name and the quote is \"Hello\"."
print(escaped_str)
# Output: The file path is C:\Users\Name and the quote is "Hello".
```