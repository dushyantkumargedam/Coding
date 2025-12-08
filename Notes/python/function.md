

## 🌟 Python Functions: The Code Superpower

### 🎯 Basic Functions (Your Starter Kit)

This section covers the absolute essentials—the minimum you need to know to start using functions. **These are CRITICALLY important.**

#### 1\. Defining and Calling a Function (The Factory Setup)

  * **Function Define:** We use the keyword **`def`** (short for define) to tell Python we are setting up a new function.
  * **Creating the Function:** This is the setup phase. It includes the `def` keyword, the function name, parentheses `()`, and a colon `:`.
  * **Calling the Function:** To make the code inside the function run, you must **call** it by using its name followed by parentheses.

<!-- end list -->

```python
def greet(): # Defining the function
    print("Hello, Python world!") # The code block
    
greet() # Calling the function
```

  * **Function Names:** Follow the same rules as variable names. Use descriptive, lowercase names, often separated by underscores (e.g., `calculate_area`).

#### 2\. Arguments and Parameters (The Ingredients)

Functions often need specific information to do their job.

  * **Parameters:** These are the names listed inside the function's parentheses during the definition. They are the **placeholders** for the information the function expects.
  * **Arguments:** These are the actual values sent to the function when you **call** it. They are the ingredients being supplied.
  * **Positional Arguments:** The simplest way to pass arguments. Python matches them to parameters based on their **position** (order).

<!-- end list -->

```python
def add(num1, num2): # num1 and num2 are parameters
    print(num1 + num2)

add(5, 3) # 5 and 3 are positional arguments
```

#### 3\. Return Values (The Finished Product)

The **`return`** keyword is how a function sends a result back to the code that called it.

  * **Why use `return`?** It allows the result to be used in other parts of your program (e.g., stored in a variable, used in a calculation). **This is one of the most important concepts.**
  * Functions can return any data type (numbers, strings, lists, etc.).

<!-- end list -->

```python
def multiply(a, b):
    return a * b # Returns the result

result = multiply(4, 5) # The function returns 20, which is stored in result
print(result + 2) # Output: 22
```

#### 4\. The `pass` Statement

If you define a function but haven't written the code inside yet, Python will give you an error. The **`pass`** statement is used as a temporary placeholder to avoid this error, letting you build the structure first.

```python
def future_feature():
    pass # I'll add the code here later!
```

-----

### 🛠️ Intermediate Functions (Building Flexibility)

This section adds tools to make your functions more adaptable and handle various inputs gracefully. **These are important for writing versatile code.**

#### 1\. Default Parameter Values

You can give a parameter a **default value**. If the caller doesn't provide an argument for that parameter, the default value is used instead.

```python
def greet(name, city="Unknown"):
    print(f"Hello {name} from {city}")

greet("Alice")          # Output: Hello Alice from Unknown (uses default)
greet("Bob", "London")  # Output: Hello Bob from London (overrides default)
```

#### 2\. Keyword Arguments

You can send arguments using the parameter names, which means their **order doesn't matter**.

  * **Keyword Arguments:** Passed using the `param=value` syntax.

<!-- end list -->

```python
def describe(age, name):
    print(f"{name} is {age} years old.")

# Order is swapped, but keywords ensure correct assignment
describe(name="Charlie", age=35) 
```

  * **Mixing Positional and Keyword:** Positional arguments **must always come first** in the call.

#### 3\. Scope (Where Variables Live)

Scope defines where a variable can be accessed.

  * **Local Scope (Inner Rooms):** A variable created *inside* a function is local and only exists while that function runs.
  * **Global Scope (Main House):** A variable created *outside* all functions is global and can be accessed anywhere.
  * **Global Keyword:** If you need to **modify** a global variable from inside a function, you must use the **`global`** keyword.

<!-- end list -->

```python
x = 10 # Global variable

def change_x():
    global x # Tells Python to use the global x
    x = 50   # Modifies the global x

change_x()
print(x) # Output: 50
```

#### 4\. Lambda Functions (Quick, Disposable Functions)

A **Lambda Function** is a small, anonymous function defined with a single expression.

  * **Why use Lambda?** Great for simple, one-time operations when you don't need a full `def` block.
  * **Syntax:** `lambda arguments: expression`

<!-- end list -->

```python
# A lambda function that adds 10 to its argument
add_ten = lambda a: a + 10
print(add_ten(5)) # Output: 15
```

-----

### 🧠 Advanced Functions (The Expert Toolkit)

These concepts are used for creating powerful, flexible, and robust code. **These are essential for advanced Python work (e.g., data science, web frameworks).**

#### 1\. Arbitrary Arguments (Taking *Any* Number of Inputs)

These allow a function to accept a variable number of arguments.

  * **Arbitrary Positional Arguments (`*args`):**

      * If you don't know how many positional arguments will be passed, use `*args` as a parameter.
      * The arguments are received as a **tuple**.

  * **Arbitrary Keyword Arguments (`**kwargs`):**

      * If you don't know how many keyword arguments will be passed, use `**kwargs`.
      * The arguments are received as a **dictionary**.

<!-- end list -->

```python
def process_data(name, *tasks, **info):
    # 'tasks' will be a tuple: ('clean', 'load', 'analyze')
    # 'info' will be a dict: {'project': 'alpha', 'version': 1}
    print(f"User: {name}, Tasks: {tasks}, Info: {info}")

process_data("Jane", "clean", "load", "analyze", project="alpha", version=1)
```

  * **Unpacking Arguments:** You can use `*` to unpack a list/tuple or `**` to unpack a dictionary when **calling** a function.

#### 2\. Positional-Only and Keyword-Only Arguments

These enforce how a function *must* be called.

  * **Positional-Only Arguments (`/`):** Parameters listed before the forward slash `/` must be passed using **position only**.
  * **Keyword-Only Arguments (`*`):** Parameters listed after the single asterisk `*` must be passed using **keywords only**.

<!-- end list -->

```python
def special_add(a, b, /, *, debug_mode=False):
    # a and b must be positional (e.g., special_add(10, 5))
    # debug_mode must be keyword (e.g., debug_mode=True)
    return a + b
```

#### 3\. Python Decorators (Wrapping Functions)

A **Decorator** is a function that takes another function and extends its behavior **without explicitly modifying it**. They are used extensively in frameworks.

  * **Syntax:** Use the `@decorator_name` syntax immediately before the function definition.

<!-- end list -->

```python
def log_start(func): # Decorator function
    def wrapper(*args, **kwargs):
        print("---Starting function---")
        result = func(*args, **kwargs)
        print("---Finished function---")
        return result
    return wrapper

@log_start # Applies the decorator
def perform_task(name):
    print(f"Task executed by {name}")

perform_task("system")
```

#### 4\. Recursion (Self-Calling Function)

**Recursion** is when a function calls **itself** to solve a problem. It's used for problems that can be broken down into smaller, similar sub-problems (like factorials or Fibonacci sequences).

  * **Base Case:** The condition that stops the recursion. **Crucial** to prevent an infinite loop.
  * **Recursive Case:** The step where the function calls itself.

<!-- end list -->

```python
def factorial(n):
    if n == 1: # Base Case
        return 1
    else: # Recursive Case
        return n * factorial(n - 1)
```

#### 5\. Generators (`yield` Keyword)

A **Generator** is a special type of function that uses the **`yield`** keyword instead of `return`.

  * **Generators Save Memory:** Instead of building an entire list in memory, a generator produces values **one at a time** only when requested (lazy evaluation).
  * **The `yield` Keyword:** Pauses the function, returns a value, and saves the function's state, ready to resume from where it left off on the next call.
  * **Generator Expressions:** A memory-efficient way to create a simple generator, similar to list comprehension but using parentheses `()`.

<!-- end list -->

```python
# Generator function
def even_numbers(max):
    n = 0
    while n <= max:
        yield n # Pauses here
        n += 2

# Using the generator (saves memory by not creating a full list)
for num in even_numbers(10):
    print(num)
```