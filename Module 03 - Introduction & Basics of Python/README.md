# **Context**

- [**Context**](#context)
- [**Day 03 - Introduction And Basic Of Python**](#day-03---introduction-and-basic-of-python)
  - [**Introduction to Python \& Setup**](#introduction-to-python--setup)
  - [**Write our first Program in Python**](#write-our-first-program-in-python)
    - [print() Function Parameters in Python](#print-function-parameters-in-python)
  - [**Operators in Python**](#operators-in-python)
  - [**Python Data Types \& Comments**](#python-data-types--comments)
  - [**Variables, Keywords \& Identifiers in Python**](#variables-keywords--identifiers-in-python)
    - [Variables](#variables)
    - [Keywords](#keywords)
    - [Identifiers](#identifiers)
  - [**Python Input**](#python-input)
  - [**Type Conversion in Python**](#type-conversion-in-python)
  - [**Literals in Python**](#literals-in-python)

# [**Day 03 - Introduction And Basic Of Python**](./Day%2003%20-%20Introduction%20And%20Basic%20Of%20Python/)

## **Introduction to Python & Setup**

- What is Python?
  - Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.

- Why Python?
  - Easy to learn
  - Design Philosophy
  - Batteries Included
  - General Purpose
  - Libraries & Community

- Installation & Environment Setup
  - [Python](https://www.python.org/downloads/)
  - [Anaconda](https://www.anaconda.com/download/success)
  - [Google Colab](https://colab.research.google.com/)

[⬆️ Go to Context](#context)

## **Write our first Program in Python**

```py
print("Hello World")
```

### print() Function Parameters in Python

- `objects`: Values to print (can be multiple)
  - Example: `print("Hello", "World") → Hello World`
- `sep`: Separator between multiple objects (default = `' '`)
  - Example: `print("Hello", "World", sep="-") → Hello-World`
- `end`: String added after the output (default = `'\n'`)
  - Example: `print("Hello", end="!") → Hello!`
- `file`: Output stream to write (default = `sys.stdout`)
  - Example: `print("Hello", file=sys.stderr)`
- `flush`: Whether to forcibly flush the stream (default = `False`)
  - Example: `print("Processing...", flush=True)`

[⬆️ Go to Context](#context)

## **Operators in Python**

- Arithmetic Operators
  - Addition (`+ `): `5 + 3 → 8`
  - Subtraction (`- `): `5 - 3 → 2`
  - Multiplication (`*`): `5 * 3 → 15`
  - Division (`/`): `5 / 2 → 2.5`
  - Floor Division (`//`): `5 // 2 → 2`
  - Modulus (`%`): `5 % 2 → 1`
  - Exponentiation (`**`): `2 ** 3 → 8`

- Comparison Operators
  - Equal to (`==`): `5 == 3 → False`
  - Not equal to (` !=`): `5 != 3 → True`
  - Greater than (`>`): `5 > 3 → True`
  - Less than (`<`): `5 < 3 → False`
  - Greater than or equal to (`>=`): `5 >= 3 → True`
  - Less than or equal to (`<=`): `5 <= 3 → False`

- Assignment Operators
  - Assign (`=`): `x = 5`
  - Add and assign (` +=`): `x += 3 → x = x + 3`
  - Subtract and assign (`-=`): `x -= 3 → x = x - 3`
  - Multiply and assign (`*=`): `x *= 3 → x = x * 3`
  - Divide and assign (`/=`): `x /= 3 → x = x / 3`
  - Floor divide and assign (`//=`): `x //= 3 → x = x // 3`
  - Modulus and assign (`%=`): `x %= 3 → x = x % 3`
  - Exponentiate and assign (`**=`): `x **= 3 → x = x ** 3`

- Logical Operators
  - Logical AND (`and`): `True and False → False`
  - Logical OR (`or`): `True or False → True`
  - Logical NOT (`not`): `not True → False`

- Bitwise Operators
  - Bitwise AND (`&`): `5 & 3 → 1`
  - Bitwise OR (`|`): `5 | 3 → 7`
  - Bitwise XOR (`^`): `5 ^ 3 → 6`
  - Bitwise NOT (`~`): `~5 → -6`
  - Left shift (`<<`): `5 << 1 → 10`
  - Right shift (`>>`): `5 >> 1 → 2`

- Membership Operators
  - In (`in`): `'a' in 'apple' → True`
  - Not in (`not in`): `'b' not in 'apple' → True`

- Identity Operators
  - Is (`is`): `x is y`
  - Is not (`is not`): `x is not y`

[⬆️ Go to Context](#context)

## **Python Data Types & Comments**

- Data Types in Python
  - Integer (`int`) - Whole numbers: `x = 10`
  - Float (`float`) - Decimal numbers: `y = 3.14`
  - Complex (`complex`) - Complex numbers: `z = 2 + 3j`
  - String (`str`) - Text: `s = "Hello"`
  - Boolean (`bool`) - True or False: `flag = True`
  - List (`list`) - Ordered, mutable collection: `lst = [1, 2, 3]`
  - Tuple (`tuple`) - Ordered, immutable collection: `tup = (1, 2, 3)`
  - Set (`set`) - Unordered, unique elements: `st = {1, 2, 3}`
  - Dictionary (`dict`) - Key-value pairs: `d = {"a": 1, "b": 2}`
  - NoneType (`None`) - Represents no value: `x = None`

- Comments in Python
  - Single-line comment (`#`): `# This is a comment`
  - Multi-line comment (triple quotes `''' '''` or `""" """`)

    ```py
    '''
    This is
    a multi-line comment
    '''
    ```

[⬆️ Go to Context](#context)

## **Variables, Keywords & Identifiers in Python**

### Variables

- Variable Binding in Python
  - Static Binding: Variable type is fixed at **compile time** (not typical in Python, seen in languages like C/C++)

    ```py
    int x = 10;  // x is always integer
    ```

  - Dynamic Binding: Variable type is determined at **runtime** (Python uses this)

    ```py
    x = 10      # x is int
    x = "Hello" # x now becomes str
    ```

[⬆️ Go to Context](#context)

### Keywords

- Boolean Literals
  - `True`: Boolean true value
  - `False`: Boolean false value
  - `None`: Represents absence of value

- Conditional / Decision Making
  - `if`: Conditional execution
  - `elif`: Else-if condition
  - `else`: Default condition
  - `assert`: Check condition, raise error if false
  - `not`: Logical NOT
  - `and`: Logical AND
  - `or`: Logical OR
  - `in`: Membership check
  - `is`: Identity check

- Loops
  - `for`: For loop
  - `while`: While loop
  - `break`: Exit loop
  - `continue`: Skip current iteration
  - `else`: Optional else block in loops

- Functions & Classes
  - `def`: Define a function
  - `return`: Return value from function
  - `lambda`: Anonymous function
  - `class`: Define a class
  - `nonlocal`: Modify variable in outer (but non-global) scope
  - `global`: Declare global variable

- Exception Handling
  - `try`: Start exception block
  - `except`: Handle exception
  - `finally`: Execute code regardless of exception
  - `raise`: Raise an exception

- Modules & Imports
  - `import`: Import module
  - `from`: Import specific names from module
  - `as`: Alias for module or variable

- Asynchronous Programming
  - `async`: Define asynchronous function
  - `await`: Wait for asynchronous operation

- Others / Flow Control
  - `pass`: Do nothing (placeholder)
  - `del`: Delete variable or object
  - `yield`: Produce generator value

[⬆️ Go to Context](#context)

### Identifiers

- Names given to variables, functions, classes, or objects to identify them.
  - Rules for Python Identifiers:
    - Can contain letters (`a-z`, `A-Z`), digits (`0-9`), and underscore (`_`)
    - Must **start with a letter or underscore**, not a digit
    - Case-sensitive (`myVar` ≠ `myvar`)
    - Cannot be a **keyword** (like `if`, `for`, `class`)
    - No spaces or special characters allowed

  - Examples:
    - Valid: `my_var`, `_counter`, `Data123`, `userName`
    - Invalid: `123data`, `my-var`, `for`, `user name`

  - Naming Conventions:
    - Variables / functions: `snake_case` → `my_variable`
    - Classes: `PascalCase` → `MyClass`
    - Constants: `UPPER_CASE` → `PI_VALUE`

[⬆️ Go to Context](#context)

## **Python Input**

- Input in Python

  - `input()`: Reads a line of text from the user (always returns a string)
    - Example: `name = input("Enter your name: ")`

[⬆️ Go to Context](#context)

## **Type Conversion in Python**

- `int()`: Convert to integer
  - Example: `x = int(3.14) → 3`

- `float()`: Convert to float
  - Example: `y = float(5) → 5.0`

- `str()`: Convert to string
  - Example: `s = str(100) → "100"`

- `bool()`: Convert to boolean
  - Example: `flag = bool(0) → False`

- `complex()`: Convert to complex number
  - Example: `c = complex(2, 3) → (2+3j)`

- `list()`: Convert to list
  - Example: `lst = list("abc") → ['a','b','c']`

- `tuple()`: Convert to tuple
  - Example: `tup = tuple([1,2,3]) → (1,2,3)`

- `set()`: Convert to set
  - Example: `st = set([1,2,2,3]) → {1,2,3}`

- `dict()`: Convert to dictionary (from iterable of key-value pairs)
  - Example: `d = dict([("a",1),("b",2)]) → {'a':1,'b':2}`

- `ord()`: Convert character to ASCII/Unicode integer
  - Example: `num = ord('A') → 65`

- `chr()`: Convert ASCII/Unicode integer to character
  - Example: `ch = chr(65) → 'A'`

[⬆️ Go to Context](#context)

## **Literals in Python**

- Literals in Python : Literals are **fixed values** assigned directly in the code that represent data. They are not computed or changed during execution.

  - String Literals
    - Example: `s = "Hello World"`

  - Numeric Literals
    - Integer
      - Example: `x = 10`
    - Float
      - Example: `y = 3.14`
    - Complex
      - Example: `z = 2 + 3j`

  - Boolean Literals
    - Example: `flag = True` / `flag = False`

  - None Literal
    - Example: `x = None`

  - Collection Literals
    - List
      - Example: `lst = [1, 2, 3]`
    - Tuple
      - Example: `tup = (1, 2, 3)`
    - Set
      - Example: `st = {1, 2, 3}`
    - Dictionary
      - Example: `d = {"a":1, "b":2}`

  - Bytes Literals
    - Example: `b = b"Hello"`

[⬆️ Go to Context](#context)