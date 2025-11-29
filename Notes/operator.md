## 🤖 Python Operators: Full Details

Python operators are special symbols or keywords that perform operations on values and variables. Python organizes its operators into seven main groups.

---

### 1. Arithmetic Operators

These operators perform basic mathematical calculations.

| Operator | Name | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (Float) | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` (rounds down to the nearest whole number) |
| `%` | Modulus | `5 % 2` | `1` (remainder) |
| `**` | Exponentiation | `5 ** 2` | `25` ($5^2$) |

---

### 2. Assignment Operators

These operators are used to assign values to variables. They combine an arithmetic operation with the assignment itself.

| Operator | Example | Equivalent to |
| :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

---

### 3. Comparison Operators

These operators are used to compare two values and return a **Boolean** result (`True` or `False`).

| Operator | Name | Example |
| :--- | :--- | :--- |
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

---

### 4. Logical Operators

These operators combine conditional statements and also return a **Boolean** result.

| Operator | Description | Example |
| :--- | :--- | :--- |
| **`and`** | Returns `True` if **both** statements are true. | `x > 5 and x < 10` |
| **`or`** | Returns `True` if **at least one** statement is true. | `x > 5 or x < 4` |
| **`not`** | Reverses the result; returns `False` if the result is true. | `not(x > 5 and x < 10)` |

---

### 5. Identity Operators

These operators compare the **memory location** (identity) of two objects, not just their values.

| Operator | Description | Example |
| :--- | :--- | :--- |
| **`is`** | Returns `True` if both variables point to the **same object** in memory. | `x is y` |
| **`is not`**| Returns `True` if both variables point to **different objects** in memory. | `x is not y` |

> **Note:** For simple immutable values (like small integers and strings), Python often reuses the same memory object, making `==` and `is` sometimes behave identically, but they are fundamentally different checks.

---

### 6. Membership Operators

These operators are used to test if a sequence (string, list, tuple, set, or dictionary) contains a specified value.

| Operator | Description | Example |
| :--- | :--- | :--- |
| **`in`** | Returns `True` if the specified value is **present** in the sequence. | `"apple" in my_list` |
| **`not in`**| Returns `True` if the specified value is **not present** in the sequence. | `"banana" not in my_list` |

---

### 7. Bitwise Operators

These operators work on the operands as if they were strings of **binary digits (bits)**. They perform bit-by-bit operations and are typically used in low-level programming, encryption, or optimization.

| Operator | Name | Description | Example (A=10, B=4) | Result (A=1010, B=0100) |
| :--- | :--- | :--- | :--- | :--- |
| **`&`** | AND | Sets each bit to 1 if **both** bits are 1. | `A & B` | `0` (0000) |
| **`|`** | OR | Sets each bit to 1 if **either** of the two bits is 1. | `A | B` | `14` (1110) |
| **`^`** | XOR | Sets each bit to 1 if **only one** of the two bits is 1. | `A ^ B` | `14` (1110) |
| **`~`** | NOT | Inverts all the bits (bitwise negation). | `~A` | `-11` |
| **`<<`** | Zero fill left shift | Shifts the bits to the left, filling with zeros from the right. | `A << 2` | `40` (101000) |
| **`>>`** | Signed right shift | Shifts the bits to the right, filling with sign bits from the left. | `A >> 2` | `2` (0010) |



Would you like some practice exercises focusing on a specific group of these operators, such as **Logical** or **Membership** operators?