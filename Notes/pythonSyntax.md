Python for Kids — Quick and Easy Notes

Basics
- Python is a language to tell the computer what to do.
- Comments (notes the computer ignores):
    # This is a note
    """This is a
    bigger note"""
- Run code with python.

Words that mean numbers and things
- Numbers:
    x = 5
    y = 3.14
- Words (strings):
    name = "Alice"
    greeting = 'hi'
    long = """many
    lines"""
    hello = f"Hi, {name}!"
- True or False:
    alive = True
- Nothing:
    nothing = None

Lists, boxes, and maps (containers)
- List (ordered things):
    fruits = ["apple", "banana", "cherry"]
- Tuple (like a list you don't change):
    pos = (10, 20)
- Set (unique things):
    colors = {"red", "blue"}
- Dict (names to things):
    kid = {"name": "Sam", "age": 8}

Putting things in boxes (variables)
- Make a variable:
    a = 1
    a = "now a word"
- Two at once:
    a, b = 1, 2
- Change a little:
    x += 1  # add 1 to x

Math and checks
- Math: + - * / // % **
- Compare: == != < <= > >=
- Words: and, or, not
- In a box?: item in list
- Same object?: is, is not

Decisions and loops
- If (choose):
    if hungry:
        eat()
    elif thirsty:
        drink()
    else:
        play()
- Short choose:
    snack = "apple" if want_apple else "cookie"
- Repeat with for:
    for toy in toys:
        print(toy)
- Repeat until:
    while not done:
        try_one_more()

Functions — little machines
- Make one:
    def add(a, b=2):
        """Adds numbers"""
        return a + b
- Short function:
    add = lambda x, y: x + y

Classes — make your own types (like blueprints)
- A simple class:
    class Dog:
        def __init__(self, name):
            self.name = name
        def bark(self):
            return "Woof!"
- Use it:
    d = Dog("Bingo")
    d.bark()

Reading and writing files
- Read:
    with open("file.txt", "r", encoding="utf-8") as f:
        text = f.read()
- Write:
    with open("file.txt", "w") as f:
        f.write("Hello!")

Errors (when things go wrong)
- Try and handle:
    try:
        value = mydict["key"]
    except KeyError:
        value = None
- Make your own:
    raise ValueError("Oops!")

Helpful tips
- Indent with 4 spaces.
- Use print(...) to see things.
- Keep code small and simple.
- Experiment and have fun!

Where to learn more
- Python docs: https://docs.python.org/3/

End of kid-friendly notes
