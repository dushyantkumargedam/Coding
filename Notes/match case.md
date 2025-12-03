## 📝 Python `match` Statement (Structural Pattern Matching)

The Python `match` statement, introduced in Python 3.10, implements **structural pattern matching**. It allows you to compare a subject (variable/value) against several distinct patterns and execute a corresponding block of code based on the first pattern that matches. It is Python's version of the `switch` statement found in other languages, but far more powerful.

-----

## 1\. Syntax and Basic Usage

The `match` statement takes a **subject** and compares it against one or more **`case`** blocks.

### Basic Syntax

```python
match subject:
    case pattern_1:
        # Code to execute if subject matches pattern_1
    case pattern_2:
        # Code to execute if subject matches pattern_2
    case _:
        # Code to execute if no other case matches (the wildcard)
```

### Example: Simple Value Matching

```python
status_code = 404

match status_code:
    case 200:
        print("Success: OK")
    case 404:
        print("Client Error: Not Found")
    case 500:
        print("Server Error: Internal Server Error")
    case _: # The wildcard pattern, matches everything else
        print("Unknown Status Code")
# Output: Client Error: Not Found
```

-----

## 2\. Key Features of Structural Pattern Matching

### A. The Wildcard (`_`)

The underscore (`_`) acts as the **wildcard pattern**. It always matches and is typically used as the final `case` to provide a default or fallback action when all other specific patterns fail.

### B. Capturing Variables

A simple variable name (that is not `_` and not a reserved keyword) used in a `case` acts as a **capturing variable**. It matches any value and, upon matching, **assigns that value** to the variable name.

```python
x = 10
match x:
    case 0:
        print("Zero")
    case other_number: # Captures the value 10
        print(f"Got a number: {other_number}")
# Output: Got a number: 10
```

### C. Matching Literals, Sequences, and Classes

`match` can identify the **structure** and **contents** of complex data types:

| Pattern Type | Description | Example |
| :--- | :--- | :--- |
| **Literal** | Matches a specific constant value (e.g., numbers, strings, Booleans, `None`). | `case 10` or `case "stop"` |
| **Sequence** | Matches lists or tuples. It can specify lengths and contents. | `case [x, y]` (matches a list/tuple of length 2) |
| **Mapping** | Matches dictionaries and checks for specific keys and their values. | `case {'id': user_id, 'status': 'active'}` |
| **Class** | Matches against objects of a specific class. | `case Point(x=0, y=0)` (matches an object of class `Point` with specific attributes) |

### Example: Matching Sequences (Lists/Tuples)

```python
command = ["move", 10, 5]

match command:
    case ["move", x, y]:
        print(f"Moving to ({x}, {y})")
    case ["undo"]:
        print("Undoing last action.")
    case _:
        print("Invalid command format.")
# Output: Moving to (10, 5)
```

-----

## 3\. Advanced Features

### A. The `if` Clause (Guards)

You can add an **`if` clause** (called a **guard**) to a `case` to add an extra condition that must be met **after** the structural pattern has matched.

```python
point = (50, 10)

match point:
    case (x, y) if x == y:
        print(f"On the diagonal at {x}")
    case (x, y) if x > 0 and y > 0:
        print("In the first quadrant")
    case _:
        print("Other location")
# Output: In the first quadrant
```

### B. The `as` Keyword

The `as` keyword allows you to match a complex sub-pattern and still capture the entire matching part as a variable.

```python
data = ["header", 1, 2, 3]

match data:
    case ["header", *rest_of_data] as full_list:
        print(f"Header found. List: {full_list}, Data: {rest_of_data}")
# Output: Header found. List: ['header', 1, 2, 3], Data: [1, 2, 3]
```

-----

## 4\. `match` vs. `if/elif/else`

| Feature | `match` Statement | `if/elif/else` Chain |
| :--- | :--- | :--- |
| **Primary Focus** | **Structural Pattern** and **Content** matching. | Evaluating **Boolean conditions**. |
| **Code Structure** | Flat structure of `case` blocks. | Sequential evaluation of `elif` expressions. |
| **Variable Assignment**| Supports automatic **capturing** and **unpacking** of values within the pattern. | Requires explicit assignment inside the code blocks. |
| **Suitability** | Ideal for **parsing structured data** (tuples, lists, dictionaries, objects) and complex state checks. | Ideal for basic numerical and logical checks. |
