## 📑 Python Lists (Data Structure Notes)

Lists are one of the most fundamental and versatile built-in data types in Python, used to store multiple items in a single variable.

-----

## 1\. List Properties and Python Collections

Lists belong to the category of sequence data types in Python.

  * **List Items** are enclosed in square brackets: `list_name = ['value 1', 'value 2', 'value 3']`.

### Key Characteristics of Lists

| Property | Description |
| :--- | :--- |
| **Ordered** | List items have a defined order, and this order will not change. New items are added to the end. (Supports indexing.) |
| **Changeable (Mutable)** | You can change, add, and remove items after the list has been created. |
| **Allows Duplicates** | Since lists are indexed, they can contain multiple items with the same value. |

### Python Collection Types (Arrays)

Python has four built-in collection data types:

| Data Type | Order | Changeable | Duplicates | Key Use |
| :--- | :--- | :--- | :--- | :--- |
| **List** | Ordered | **Changeable** | Allowed | General purpose, mutable sequence. |
| **Tuple** | Ordered | Unchangeable | Allowed | Fixed data structure, often faster. |
| **Set** | Unordered | Unchangeable\* | **Not Allowed** | Membership testing, unique collection. |
| **Dictionary** | Ordered\*\* | Changeable | **Keys Unique** | Key-value pairs for mapping data. |

> \*Set items are unchangeable, but you can add or remove items from the set.
> **Dictionaries are ordered from Python 3.7+ (officially).**

-----

## 2\. Creating and Inspecting Lists

  * **Length:** Use the **`len()`** function to find the number of items in a list.
  * **Type:** Use the **`type()`** function to verify the data type: `print(type([]))` outputs `<class 'list'>`.
  * **Constructor:** Use the **`list()`** constructor to create a new list, often from another iterable: `my_list = list(('a', 'b', 'c'))`.

-----

## 3\. Accessing and Checking Items

### Indexing and Slicing

  * **Index:** Access items using their index (position): `my_list[0]` is the first item.
  * **Negative Indexing:** Access items from the end: `my_list[-1]` is the last item.
  * **Range of Indexing (Slicing):** Returns a new list of the specified items.
      * `list[start:end]` (End index is **exclusive**).
      * `list[start:]` (From start to the end).
      * `list[:end]` (From the beginning up to the end index).
      * `list[-4:-1]` (Range using negative indexes).

### Check if Item Exists

Use the **`in`** keyword to determine if an item is present:

```python
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, apple is in the list.")
```

-----

## 4\. Modifying and Adding Items

### Changing Values

  * **Change Single Item:** Assign a new value to a specific index: `my_list[1] = "new value"`.
  * **Change Range of Items:** Assign a list of new values to a slice: `my_list[1:3] = ["new value 1", "new value 2"]`.

### Adding Items

1.  **`append()`:** Adds an element to the **end** of the list.
      * `my_list.append("orange")`
2.  **`insert()`:** Adds an element at a **specified position**.
      * `my_list.insert(1, "grape")` (Inserts "grape" at index 1).
3.  **`extend()`:** Adds the elements of another iterable (like a list, tuple, set, or dictionary) to the end of the current list.
      * `list1.extend(list2)`

-----

## 5\. Removing Items

1.  **`remove()`:** Removes the item with the **specified value** (only the first occurrence).
      * `my_list.remove("apple")`
2.  **`pop()`:** Removes the element at the **specified index**. If no index is specified, it removes and returns the **last item**.
      * `my_list.pop(1)`
3.  **`del` keyword:** Removes the item at the specified index or **deletes the entire list**.
      * `del my_list[0]` (Deletes first item)
      * `del my_list` (Deletes the list object completely)
4.  **`clear()`:** Empties the list, leaving the list object intact but with no items.
      * `my_list.clear()`

-----

## 6\. Looping and List Comprehension

### Looping Lists

1.  **`for` loop (Direct Iteration):** The easiest way to loop through items.
      * `for x in my_list: print(x)`
2.  **`for` loop (Using `range()` and `len()`):** Loops through the index numbers.
      * `for i in range(len(my_list)): print(my_list[i])`
3.  **`while` loop:** Requires manually tracking the index and incrementing it.
      * `i = 0; while i < len(my_list): print(my_list[i]); i += 1`

### Looping Using List Comprehension

List comprehension provides a concise way to create new lists based on existing lists.

$$\text{[expression for item in iterable if condition == True]}$$

| Component | Description |
| :--- | :--- |
| **Expression** | The value to put into the new list (e.g., `x.upper()`, `x * 2`). |
| **Iterable** | The existing list or sequence to loop through (e.g., `fruits`). |
| **Condition (Optional)** | A filter to include only items that meet the criteria. |

```python
# Syntax Example: Create a list of squared numbers from 0 to 4
squares = [x**2 for x in range(5)] # Output: [0, 1, 4, 9, 16]
```

-----

## 7\. Sorting and Copying

### Sorting Lists

The **`sort()`** method sorts the list **in-place** (modifies the original list).

  * **Default Sort:** Sorts alphabetically or numerically in **ascending** order.
      * `my_list.sort()`
  * **Sort Descending:** Use the `reverse=True` argument.
      * `my_list.sort(reverse=True)`
  * **Case Insensitive Sort:** Use the `key=str.lower` argument to sort based on a lowercase representation.
      * `my_list.sort(key=str.lower)`
  * **Customize Sort Function:** Use the `key` argument to specify a function to be called on each list item prior to making comparisons.

### Reverse Order

The **`reverse()`** method reverses the **current order** of the elements (it does not sort them).

  * `my_list.reverse()`

### Copying Lists

Simple assignment (`list2 = list1`) creates a reference, meaning changes to one affect the other. To make a true copy:

1.  **`copy()` Method:**
      * `new_list = old_list.copy()`
2.  **`list()` Constructor:**
      * `new_list = list(old_list)`
3.  **Slicing Operator:**
      * `new_list = old_list[:]`

### Joining Lists

1.  **Concatenation Operator:** Use the `+` operator to create a **new list** containing all elements.
      * `list3 = list1 + list2`
2.  **`extend()` Method:** Appends all elements from one list to the **end of another** (modifies the first list).
      * `list1.extend(list2)`

-----

## 8\. List Methods Summary

Python has a set of built-in methods designed specifically for lists.

| Method | Description |
| :--- | :--- |
| `append()` | Adds an element at the end of the list. |
| `clear()` | Removes all the elements from the list. |
| `copy()` | Returns a shallow copy of the list. |
| `count()` | Returns the number of elements with the specified value. |
| `extend()` | Adds the elements of an iterable (e.g., another list) to the end of the current list. |
| `index()` | Returns the index of the first element with the specified value. |
| `insert()` | Adds an element at the specified position. |
| `pop()` | Removes and returns the element at the specified position (defaults to the last item). |
| `remove()` | Removes the first item with the specified value. |
| `reverse()` | Reverses the order of the list. |
| `sort()` | Sorts the list (in-place) in ascending order by default. |