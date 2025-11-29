## 📑 Python Tuples Notes

Tuples are a fundamental sequence data type in Python, used to store multiple items in a single variable. They are defined by their **immutability**.

-----

## 1\. Defining and Properties

  * **Syntax:** Tuples are defined using parentheses: `my_tuple = ("value1", "value2", "value3")`.
  * **List vs. Tuple:**
      * **List:** Uses square brackets `[]`. It is **ordered** and **changeable (mutable)**.
      * **Tuple:** Uses parentheses `()`. It is **ordered** and **unchangeable (immutable)**.

### Key Tuple Properties

| Property | Status | Description |
| :--- | :--- | :--- |
| **Ordered** | Yes | Items have a defined index/order. |
| **Changeable** | **No (Immutable)** | You cannot change, add, or remove items after creation. |
| **Duplicates** | Allowed | Can contain multiple items with the same value. |

### Creating a Single-Item Tuple

To create a tuple with only one item, you **must** include a trailing comma after the item. Without the comma, Python recognizes it only as the type of the item inside the parentheses (e.g., a string or integer).

```python
one_item_tuple = ("apple",) # Correct: type is <class 'tuple'>
not_a_tuple = ("apple")    # Incorrect: type is <class 'str'>
```

### Inspecting Tuples

  * **Data Type:** Use the **`type()`** function: `print(type(my_tuple))`
  * **Constructor:** Use the **`tuple()`** constructor to create a tuple, often from a list or other iterable: `new_tuple = tuple(["a", "b", "c"])`.

-----

## 2\. Accessing Items

Since tuples are **ordered**, access is identical to lists.

  * **Indexing:** Access items using positive index numbers (starting at 0).
  * **Negative Indexing:** Access items from the end (e.g., `-1` is the last item).
  * **Range of Indexing (Slicing):** Returns a new tuple containing the specified range: `my_tuple[1:4]` (index 4 is exclusive).

### Check if Item Exists

Use the **`in`** keyword to determine if an item is present:

```python
colors = ("red", "green", "blue")
if "red" in colors:
    print("Red is present.") # True
```

-----

## 3\. Updating, Adding, and Removing Items (The Workaround)

Because tuples are **immutable**, you cannot directly use methods like `append()`, `remove()`, or direct index assignment.

The standard workaround involves temporary type conversion:

1.  **Convert** the tuple to a **list** using `list()`.
2.  **Modify** the list (change, add, or remove items).
3.  **Convert** the list back to a **tuple** using `tuple()`.

### Example: Change Item

```python
x = ("apple", "banana", "cherry")
y = list(x)      # Step 1: Convert to list
y[1] = "kiwi"    # Step 2: Modify the list
x = tuple(y)     # Step 3: Convert back to tuple
# x is now ('apple', 'kiwi', 'cherry')
```

### Example: Add Item (Append)

Adding an item is done by converting to a list and using `append()`.

### Example: Remove Item

Removing an item is done by converting to a list and using `remove()` or `pop()`.

### The `del` Keyword

The **`del`** keyword can delete the **entire tuple object** completely from memory, but it cannot delete individual items within the tuple.

```python
t = (1, 2, 3)
del t  # The tuple 't' no longer exists
# print(t) would cause an error
```

-----

## 4\. Unpacking Tuples

**Unpacking** is a way to extract the values from a tuple (or any iterable) into multiple variables. The number of variables must match the number of elements.

```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits # Unpacks values into variables
print(yellow) # Output: banana
```

### Using Asterisk `*` (Variable Assignment)

If the number of variables is less than the number of values, you can add an asterisk `*` to a variable name. This variable will then hold the remaining values as a **list**.

```python
# The asterisk is on the middle variable
info = ("Alice", 25, "Analyst", "NYC")
(name, age, *details) = info

print(details) # Output: ['Analyst', 'NYC'] (Note: it's a list)

# The asterisk can be placed anywhere
(*first_two, last_item) = info
print(first_two) # Output: ['Alice', 25, 'Analyst']
```

-----

## 5\. Looping and Joining

### Loop Tuples

Tuples are iterable, and loops work the same as they do for lists:

  * **Direct Iteration:** `for item in my_tuple: print(item)`
  * **Index Iteration:** `for i in range(len(my_tuple)): print(my_tuple[i])`

### Join Tuples

Tuples are joined using the **`+`** operator, which creates a **new tuple**.

```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2 # t3 is now (1, 2, 3, 4)
```

-----

## 6\. Tuple Methods

Due to their immutable nature, tuples have very few methods compared to lists.

| Method | Description |
| :--- | :--- |
| **`count()`** | Returns the number of times a specified value occurs in the tuple. |
| **`index()`** | Searches the tuple for a specified value and returns the **first index** where it is found. Raises an error if the value is not present. |

```python
data = (10, 20, 10, 30)
print(data.count(10))  # Output: 2
print(data.index(20))  # Output: 1
```