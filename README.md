<div align="center">
<h1>Full Stack DS with GenAI Bootcamp</h1>

> *Notes, Assignments of Full Stack DS with GenAI Bootcamp*
</div>

# **Context**
- [**Context**](#context)
- [**Day 01 - Induction Session**](#day-01---induction-session)
  - [**Session and Overview**](#session-and-overview)
    - [Introduction](#introduction)
- [**Day 02 - Introduction to AI \& System Setup**](#day-02---introduction-to-ai--system-setup)
  - [**Introduction to AI**](#introduction-to-ai)
    - [What is AI?](#what-is-ai)
    - [What is Data Science?](#what-is-data-science)
    - [Career Opportunities](#career-opportunities)
    - [Importance of DS](#importance-of-ds)
    - [Application of AI](#application-of-ai)
    - [Venn Diagram](#venn-diagram)
    - [AI Project Development Life Cycle](#ai-project-development-life-cycle)
    - [Different Roles in AI](#different-roles-in-ai)
  - [**System Setup Tools**](#system-setup-tools)
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
- [**Day 04 - Conditional Statements, Pip, Modules \& Loops**](#day-04---conditional-statements-pip-modules--loops)
  - [**Conditional Statements**](#conditional-statements)
  - [**PIP (Pip Installs Packages)**](#pip-pip-installs-packages)
  - [**Modules in Python**](#modules-in-python)
  - [**Loops in Python**](#loops-in-python)

# **Day 01 - Induction Session**

## **Session and Overview**

### Introduction

- Overview on
  - Github
  - Linkedin
  - Email
  - Assignment Submission

[⬆️ Go to Context](#context)

# **Day 02 - Introduction to AI & System Setup**

## **Introduction to AI**

### What is AI?

- Artificial Intelligence (AI) is the creation of computer systems that can simulate human intelligence to perform tasks.
- In short, AI allows machines to:
  - Learn from data.
  - Reason and solve problems.
  - Make decisions or take actions (like recognizing speech or driving a car)

[⬆️ Go to Context](#context)

### What is Data Science?

- Data Science is an interdisciplinary field that uses scientific methods, processes,algorithms, and systems to extract knowledge and insights from vast amounts of structured and unstructured data, in order to inform human decision-making and strategy.
- In simpler terms: It's the entire process of getting useful, actionable knowledge out of raw data.

[⬆️ Go to Context](#context)

### Career Opportunities

- "The rise of AI/Data Science needs will create roughly 11.5 million job openings
- by 2026" US Bureau of Labour Statistics "By 2026, AI/Data Scientists and Analysts will become the number one emerging role in the world." World Economic Forum
- Data Science and Artificial Intelligence are amongst the hottest fields of the 21st century that will impact all segments of daily life by 2025, from transport and logistics to healthcare and customer service.

[⬆️ Go to Context](#context)

### Importance of DS

- Data science helps brands to understand their customers in a much enhanced and empowered manner.
- It allows brands to communicate their story in such a engaging and powerful manner.
- Data is a new field that is constantly growing and evolving.
- Its findings and results can be applied to almost any sector like travel, healthcare and education among others.
- Data science is accessible to almost all sectors.

[⬆️ Go to Context](#context)

### Application of AI

- **Healthcare** – AI helps in disease detection, medical imaging, drug discovery, and robotic surgery.
- **Finance** – Used for fraud detection, stock prediction, automated trading, and credit risk analysis.
- **Education** – Powers personalized learning, grading automation, and virtual tutoring systems.
- **Transportation** – Enables self-driving cars, route optimization, and predictive vehicle maintenance.
- **Manufacturing** – Improves production efficiency, defect detection, and supply chain optimization.
- **Retail** – Provides product recommendations, demand forecasting, and customer behavior analysis.
- **Agriculture** – Supports crop monitoring, soil analysis, pest control, and smart irrigation.
- **Cybersecurity** – Detects anomalies, prevents intrusions, and strengthens network defenses.
- **Entertainment** – Generates AI-driven music, movies, games, and content personalization.
- **Customer Service** – Automates responses through chatbot and voice assistants for 24/7 support.

[⬆️ Go to Context](#context)

### Venn Diagram

![venn diagram](https://i.imgur.com/6e3FSxF.png)

[⬆️ Go to Context](#context)

### AI Project Development Life Cycle

![ai project development life cycle](https://i.imgur.com/r3L7rpk.png)

[⬆️ Go to Context](#context)

### Different Roles in AI

- **Data Analyst** - Data analysis + AI insights
- **Machine Learning Engineer** - Predictive models, pipelines
- **Deep Learning Engineer** - Neural networks, CV, NLP
- **NLP Engineer / LLM Engineer** - Text, chatbot, RAG, fine-tuning
- **Computer Vision Engineer** - Images, video, 3D data
- **Generative AI Engineer** - Image/audio/text generation/RAG/Agents/MCP
- **MLOps Engineer** - Model optimization/deployment & monitoring
- **AI Engineer/Data Scientist** - Full AI stack (ML, DL, LLMs, MLOps)
- **AI Research Engineer** - Develop new algorithms & architectures

[⬆️ Go to Context](#context)

## **System Setup Tools**

- [Anaconda](https://www.anaconda.com/download/success)
- [VS Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/install/windows)
- [GitHub](https://github.com/)
- [Salary Range](https://www.glassdoor.com/)

> VS Code Extension - Python, Code Runner, Jupyter, Git, Graph, Git Lens.

[⬆️ Go to Context](#context)

# **Day 03 - Introduction And Basic Of Python**

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

# **Day 04 - Conditional Statements, Pip, Modules & Loops**

## **Conditional Statements**

- Conditional Statements in Python : Conditional statements are used to make decisions in code based on whether a condition is **True** or **False**.

  - `if` Statement

    ```py
    x = 10
    if x > 5:
        print("x is greater than 5")
    ```

  - `if-else` Statement

    ```py
    x = 3
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
    ```

  - `if-elif-else` Statement

    ```py
    x = 0
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")
    ```

  - Nested `if` Statement

    ```py
    x = 15
    if x > 0:
        if x % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    ```

  - Conditional Expression (Ternary Operator)

    ```py
    x = 10
    result = "Even" if x % 2 == 0 else "Odd"
    print(result)
    ```

[⬆️ Go to Context](#context)

## **PIP (Pip Installs Packages)**

- PIP (Pip Installs Packages) : `pip` is the **package manager for Python** used to install, upgrade, and manage external Python libraries and dependencies.

- Check pip version
  - `pip --version`

- Install a package
  - `pip install package_name`

- Install specific version
  - `pip install package_name==1.2.3`

- Upgrade a package
  - `pip install --upgrade package_name`

- Uninstall a package
  - `pip uninstall package_name`

- Show installed packages
  - `pip list`

- Show details of a package
  - `pip show package_name`

- Save installed packages to a requirements file
  - `pip freeze > requirements.txt`

- Install packages from a requirements file
  - `pip install -r requirements.txt`

[⬆️ Go to Context](#context)

## **Modules in Python**

- Modules in Python : A **module** in Python is a file containing Python code (functions, variables, or classes) that can be imported and reused in other programs.

  - Types of Modules
    - Built-in Modules: Pre-installed with Python (e.g., `math`, `os`, `sys`)
    - User-defined Modules: Created by the user as `.py` files
    - External Modules: Installed using `pip` (e.g., `requests`, `numpy`)

  - Importing a Module

    ```py
    import math
    print(math.sqrt(16))
    ```

  - Importing Specific Function

    ```pt
    from math import sqrt
    print(sqrt(25))
    ```

  - Importing with Alias

    ```py
    import math as m
    print(m.pi)
    ```

  - Importing All Contents (not recommended)

    ```py
    from math import *
    print(factorial(5))
    ```

  - Creating a User-defined Module

    - File: `my_module.py`

      ```py
      def greet(name):
          return f"Hello, {name}!"
      ```

    - Usage:

      ```py
      import my_module
      print(my_module.greet("Tansen"))
      ```

  - Checking Module Search Path

    ```py
    import sys
    print(sys.path)
    ```

  - Re-importing a Modified Module

    ```py
    import importlib
    importlib.reload(my_module)
    ```

[⬆️ Go to Context](#context)

## **Loops in Python**

- Loops in Python : Loops are used to **execute a block of code repeatedly** until a certain condition is met.

  - Types of Loops
    - `for` loop
    - `while` loop

  - `for` Loop
    - Used to iterate over a sequence (list, tuple, string, range, etc.)

      ```py
      for i in range(5):
          print(i)
      ```

  - `while` Loop
    - Executes as long as the condition is `True`

      ```py
      x = 0
      while x < 5:
          print(x)
          x += 1
      ```

  - `break` Statement
    - Used to **exit** the loop immediately

      ```py
      for i in range(10):
          if i == 5:
              break
          print(i)
      ```

  - `continue` Statement
    - Skips the current iteration and continues with the next

      ```py
      for i in range(5):
          if i == 2:
              continue
          print(i)
      ```

  - `else` with Loop
    - The `else` block executes **only if the loop completes normally** (without `break`)

      ```py
      for i in range(3):
          print(i)
      else:
          print("Loop finished")
      ```

  - Nested Loops
    - A loop inside another loop

      ```py
      for i in range(2):
          for j in range(3):
              print(i, j)
      ```

  - Infinite Loop
    - A loop that runs forever until a `break` condition occurs

      ```py
      while True:
          print("Running...")
          break
      ```

[⬆️ Go to Context](#context)
