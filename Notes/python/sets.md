## 📑 Python Sets and Frozensets Notes

Sets are an unordered collection data type in Python, primarily used to perform mathematical set operations and efficiently store unique items.

-----

## 1\. Defining and Properties

  * **Syntax:** Sets are defined using curly braces: `my_set = {"value 1", "value 2", "value 3"}`.
  * **Purpose:** Sets are used to store multiple items in a single variable.

### Key Set Properties

| Property | Status | Description |
| :--- | :--- | :--- |
| **Unordered** | Yes | Items do not have a defined index; order may change after every run. |
| **Unchangeable**\* | Yes | Items themselves cannot be changed, but you can add or remove items from the set. |
| **Unindexed** | Yes | Cannot access items using index numbers or keys. |
| **Duplicates** | **Not Allowed** | Sets automatically ignore duplicate values. |

### Handling Duplicates

Duplicate values are ignored. For example: `{"apple", "banana", "cherry", "apple"}` results in `{'apple', 'banana', 'cherry'}`.

> **Crucial Note:** The values **`True`** and **`1`** are considered the same value in sets, as are **`False`** and **`0`**. They are treated as duplicates, and only one will be kept.

### Inspecting Sets

  * **Length:** Use the **`len()`** function to find the number of unique items.
  * **Data Type:** Use the **`type()`** function: `print(type({}))` outputs `<class 'set'>`.
  * **Constructor:** Use the **`set()`** constructor to create a set from any iterable (list, tuple, etc.): `my_set = set(["a", "b", "c"])`.

-----

## 2\. Accessing and Adding Items

### Access Set Items

Since sets are **unordered** and **unindexed**, you cannot access items by referring to an index or key.

  * **Looping:** You can loop through the set items using a `for` loop.
  * **Checking Existence:** You can check if a specified value is present using the **`in`** keyword.

<!-- end list -->

```python
my_set = {"A", "B", "C"}
for item in my_set:
    print(item)

if "B" in my_set:
    print("B is in the set.")
```

### Add Set Items

Once a set is created, you cannot change its existing items, but you **can add new items**.

1.  **`add()`:** Adds a **single element** to the set.
      * `my_set.add("D")`
2.  **`update()`:** Adds elements from **another iterable** (set, list, tuple, etc.) to the current set. Duplicate items are ignored.
      * `my_set.update(["E", "F"])`

-----

## 3\. Removing Items

To remove an item, you can use the following methods:

1.  **`remove()`:** Removes the specified item. **Raises a `KeyError`** if the item is not found.
2.  **`discard()`:** Removes the specified item. **Does nothing** if the item is not found (safer than `remove()`).
3.  **`pop()`:** Removes a **random** item from the set (since sets are unordered). Returns the removed item.
4.  **`clear()`:** Removes all elements from the set, leaving it empty.
5.  **`del` keyword:** Deletes the entire set object from memory.

-----

## 4\. Set Operations (Joining Sets)

Set operations are powerful tools for combining, comparing, and filtering collections.

| Operation/Method | Shortcut | Description | Example |
| :--- | :--- | :--- | :--- |
| **`union()`** | `\|` | Returns a **new set** containing **all** unique items from both sets. | `set1 \| set2` |
| **`update()`** | `\|=` | **Updates the first set** with items from another set (union and assignment). | `set1 \|= set2` |
| **`intersection()`** | `&` | Returns a **new set** containing **ONLY the items present in both** sets (duplicates/common items). | `set1 & set2` |
| **`difference()`** | `-` | Returns a **new set** containing items present **only in the first set**, but not in the second. | `set1 - set2` |
| **`symmetric_difference()`** | `^` | Returns a **new set** containing all items **EXCEPT the common ones** (items unique to each set). | `set1 ^ set2` |

You can also join a set and a tuple (or any iterable) using methods like `union()`, but the result will always be a new **set**.

[Image of a Venn diagram illustrating set union, intersection, and difference]
![alt text](images/image.png)

-----

## 5\. Frozenset (`frozenset`)

A **frozenset** is an immutable version of a standard set. Once created, you **cannot add or remove elements**.

  * **Creation:** Use the **`frozenset()`** constructor to create a frozenset from any iterable.
    ```python
    my_frozenset = frozenset(["a", "b", "c"])
    ```
  * **Frozenset Methods:** Being immutable, frozensets support all **non-mutating set operations** (those that return a new set or a boolean), such as `copy()`, `difference()`, `intersection()`, `union()`, `isdisjoint()`, `issubset()`, and `issuperset()`.

-----

## 6\. Comprehensive Set Methods Summary

The following table summarizes the key methods available for sets. Note that methods ending in `_update` modify the original set in-place.

| Method | Shortcut | Description |
| :--- | :--- | :--- |
| `add()` | | Adds an element to the set. |
| `clear()` | | Removes all elements from the set. |
| `copy()` | | Returns a shallow copy of the set. |
| `discard()` | | Removes the specified item (safe). |
| `remove()` | | Removes the specified item (raises KeyError if not found). |
| `pop()` | | Removes a random element from the set. |
| `difference_update()` | `-=` | Removes items in the set that are also in another specified set. |
| `intersection_update()`| `&=` | Keeps only the items in the set that are also present in other specified set(s). |
| `isdisjoint()` | | Returns `True` if two sets have **no common items**. |
| `issubset()` | `<=` / `<` | Returns `True` if all items of this set are present in another set. |
| `issuperset()` | `>=` / `>` | Returns `True` if all items of another set are present in this set. |
| `symmetric_difference_update()` | `^=` | Inserts the symmetric differences from this set and another. |
| `union()` | `|` | Returns a new set containing the union of sets. |
| `update()` | `|=` | Updates the set with the union of itself and others. |