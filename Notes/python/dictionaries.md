## 📑 Python Dictionaries Notes

Dictionaries (`dict`) are a powerful, flexible data structure in Python used to store data in **key:value pairs**. They are the primary tool for mapping data.

-----

## 1\. Defining and Properties

  * **Syntax:** Dictionaries are created using curly braces, with entries separated by commas:
    ```python
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    ```

### Key Dictionary Properties

| Property | Status | Description |
| :--- | :--- | :--- |
| **Ordered** | Yes\* | The items have a defined order that will not change (from Python 3.7+). |
| **Changeable (Mutable)** | Yes | You can change, add, or remove items after the dictionary is created. |
| **Duplicates** | **Not Allowed (Keys)** | Keys must be unique; values can be duplicated. If a key is repeated, the latest value assigned to that key will overwrite the previous one. |

  * **Length:** Use the **`len()`** function to find the number of key:value pairs.
  * **Data Type:** Use the **`type()`** function: `print(type({}))` outputs `<class 'dict'>`.
  * **Constructor:** Use the **`dict()`** constructor to create a dictionary, often from a sequence of key-value tuples: `new_dict = dict(brand="Tesla", model="S")`.

-----

## 2\. Accessing and Checking Items

Unlike lists, you access dictionary items by referring to their **key**, not their index.

### Access Methods

1.  **Square Brackets:** Directly access the value using the key. **Raises a `KeyError`** if the key does not exist.
      * `print(thisdict["model"])`
2.  **`get()` Method:** Returns the value of the specified key. **Returns `None`** (or a specified default value) if the key does not exist (safer).
      * `print(thisdict.get("model"))`
      * `print(thisdict.get("color", "Not Found"))`

### View Objects (Keys, Values, Items)

These methods return dynamic "views" of the dictionary's content, which will update if the dictionary changes:

  * **`keys()`:** Returns a list-like view of all the keys in the dictionary.
  * **`values()`:** Returns a list-like view of all the values in the dictionary.
  * **`items()`:** Returns a list-like view containing a tuple for each key-value pair.

### Check if Key Exists

Use the **`in`** keyword to determine if a specified **key** is present in the dictionary:

```python
if "model" in thisdict:
    print("The key 'model' exists.")
```

-----

## 3\. Changing and Adding Items

### Change or Add

Since dictionaries are changeable, you can modify a value by referencing its key:

  * **Change:** If the key exists, the value is updated.
  * **Add:** If the key does not exist, a new key:value pair is inserted.
      * `thisdict["year"] = 2024` (Change)
      * `thisdict["color"] = "red"` (Add)

### `update()` Method

The **`update()`** method updates the dictionary with elements from another dictionary (or any iterable of key-value pairs). If a key exists, its value is updated; otherwise, the new key:value pair is added.

```python
thisdict.update({"year": 2024, "lights": "LED"})
```

-----

## 4\. Removing Items

1.  **`pop(key)`:** Removes the item with the **specified key** and returns the associated value.
2.  **`popitem()`:** Removes the **last inserted** key-value pair (in versions prior to 3.7, it removed a random item).
3.  **`del` keyword:**
      * Removes the item with the **specified key**: `del thisdict["model"]`.
      * Deletes the **entire dictionary**: `del thisdict`.
4.  **`clear()`:** Removes all the elements from the dictionary, leaving an empty dictionary `{}`.

-----

## 5\. Looping Dictionaries

Dictionaries can be looped in several ways using the `for` loop:

| Goal | Method | Example |
| :--- | :--- | :--- |
| **Loop Keys (Default)** | Loop the dictionary object directly. | `for k in thisdict:` |
| **Loop Keys (Explicit)** | Use the **`keys()`** method. | `for k in thisdict.keys():` |
| **Loop Values Only** | Use the **`values()`** method. | `for v in thisdict.values():` |
| **Loop Both (Key & Value)** | Use the **`items()`** method (returns tuples of key, value). | `for k, v in thisdict.items(): print(k, v)` |

-----

## 6\. Copying Dictionaries

Simple assignment (`dict2 = dict1`) only creates a **reference**. To create a true, independent copy:

1.  **`copy()` Method:** Uses the built-in dictionary method.
      * `new_dict = old_dict.copy()`
2.  **`dict()` Constructor:** Uses the built-in function, passing the original dictionary as an argument.
      * `new_dict = dict(old_dict)`

### Nested Dictionaries

A dictionary can contain another dictionary. This is common when modeling hierarchical data.

```python
family = {
  "child1": {"name": "Emil", "year": 2004},
  "child2": {"name": "Tobias", "year": 2007}
}
print(family["child2"]["name"]) # Accesses "Tobias"
```

-----

## 7\. Dictionary Methods Summary

| Method | Description |
| :--- | :--- |
| `clear()` | Removes all elements from the dictionary. |
| `copy()` | Returns a shallow copy of the dictionary. |
| `fromkeys()` | Returns a dictionary with the specified keys and a single specified value (optional). |
| `get()` | Returns the value for the specified key (safe lookup). |
| `items()` | Returns a view object containing tuples of key-value pairs. |
| `keys()` | Returns a view object containing the dictionary's keys. |
| `pop()` | Removes the element with the specified key. |
| `popitem()` | Removes the last inserted key-value pair. |
| `setdefault()` | Returns the value of the specified key. If the key doesn't exist, it inserts the key with a default value and returns that default value. |
| `update()` | Updates the dictionary with the specified key-value pairs. |
| `values()` | Returns a view object containing the dictionary's values. |