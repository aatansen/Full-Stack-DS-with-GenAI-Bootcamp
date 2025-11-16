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
  - [**Assignment 01**](#assignment-01)
- [**Day 05 - Loops in Python**](#day-05---loops-in-python)
  - [**Loops Recap**](#loops-recap)
  - [**Loop Control Statements**](#loop-control-statements)
  - [**Code Visualization Tool**](#code-visualization-tool)
- [**Day 06 - Strings in Python**](#day-06---strings-in-python)
  - [**Strings in Python**](#strings-in-python)
    - [Creating Strings](#creating-strings)
    - [Accessing Strings](#accessing-strings)
    - [Adding Chars to Strings](#adding-chars-to-strings)
    - [Editing Strings](#editing-strings)
    - [Deleting Strings](#deleting-strings)
    - [Operations on Strings](#operations-on-strings)
    - [String Functions](#string-functions)
    - [String Methods](#string-methods)
  - [**Strings Exercise**](#strings-exercise)
    - [Find the length of a given string without using the len() function](#find-the-length-of-a-given-string-without-using-the-len-function)
    - [Extract username from a given email](#extract-username-from-a-given-email)
- [**Day 07 - List in Python**](#day-07---list-in-python)
  - [**List in Python**](#list-in-python)
    - [What are Lists?](#what-are-lists)
    - [Lists Vs Arrays](#lists-vs-arrays)
    - [Characteristics of a List](#characteristics-of-a-list)
    - [How to create a list](#how-to-create-a-list)
    - [Access items from a List](#access-items-from-a-list)
    - [List Methods](#list-methods)
    - [List Functions](#list-functions)
    - [Editing items in a List](#editing-items-in-a-list)
    - [Deleting items from a List](#deleting-items-from-a-list)
    - [Operations on Lists](#operations-on-lists)
    - [List comprehension](#list-comprehension)
    - [`zip()` Function in Python](#zip-function-in-python)
- [**Day 08 - Tuples, Sets \& Dictionary**](#day-08---tuples-sets--dictionary)
  - [**Tuples**](#tuples)
    - [Creating a Tuple](#creating-a-tuple)
    - [Accessing Items in Tuple](#accessing-items-in-tuple)
    - [Editing Items in Tuple](#editing-items-in-tuple)
    - [Adding Items in Tuple](#adding-items-in-tuple)
    - [Deleting Items in Tuple](#deleting-items-in-tuple)
    - [Operations on Tuples](#operations-on-tuples)
    - [Tuple Methods](#tuple-methods)
    - [Tuple Functions](#tuple-functions)
    - [Tuple Unpacking](#tuple-unpacking)
    - [Using `zip()` with Tuples](#using-zip-with-tuples)
    - [Tuple Comprehension](#tuple-comprehension)
    - [List vs Tuple](#list-vs-tuple)
  - [**Sets**](#sets)
    - [Creating a Set](#creating-a-set)
    - [Accessing Items in Set](#accessing-items-in-set)
    - [Editing Items in Set](#editing-items-in-set)
    - [Adding Items in Set](#adding-items-in-set)
    - [Deleting Items in Set](#deleting-items-in-set)
    - [Operations on Set](#operations-on-set)
    - [Set Methods](#set-methods)
    - [Set Functions](#set-functions)
    - [Frozenset in Python](#frozenset-in-python)
    - [Set Comprehension](#set-comprehension)
    - [Using `zip()` with Sets](#using-zip-with-sets)
  - [**Dictionary**](#dictionary)
    - [Creating a Dictionary](#creating-a-dictionary)
    - [Accessing Items in Dictionary](#accessing-items-in-dictionary)
    - [Editing Items in Dictionary](#editing-items-in-dictionary)
    - [Adding Items in Dictionary](#adding-items-in-dictionary)
    - [Deleting Items in Dictionary](#deleting-items-in-dictionary)
    - [Operations on Dictionary](#operations-on-dictionary)
    - [Dictionary Methods](#dictionary-methods)
    - [Dictionary Functions](#dictionary-functions)
    - [Dictionary Unpacking](#dictionary-unpacking)
    - [Using `zip()` with Dictionary](#using-zip-with-dictionary)
    - [Dictionary Comprehension](#dictionary-comprehension)
    - [Simple Project Using Dictionary](#simple-project-using-dictionary)

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

# [**Day 04 - Conditional Statements, Pip, Modules & Loops**](./Day%2004%20-%20Conditional%20Statements,%20Pip,%20Modules%20&%20Loops/)

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

## [**Assignment 01**](./Assignments/Assignment%2001/)

[⬆️ Go to Context](#context)

# [**Day 05 - Loops in Python**](./Day%2005%20-%20Loops%20in%20Python/)

## **Loops Recap**

- `while` Loop: Repeats code **while a condition is True**

  ```py
  x = 0
  while x < 3:
      print("Count:", x)
      x += 1
  ```

- `for` Loop: Iterates over a sequence (list, string, range, etc.)

  ```py
  for i in range(3):
      print("Index:", i)
  ```

- Program to print multiplication table

  ```py
  number = int(input("Enter a number: "))
  i=1
  while i<=10:
      print(f"{number} * {i} = {number*i}")
      i+=1
  ```

- Guess the number game

  ```py
  """
  - Genera a random number (1-100)
  - Take an input from user -> guess the number
  - Compare / match the num
  - if user guess>generate number -> guess a lower num
  - if guess < generate num-> guess a higher num
  - if num correct show result
  """
  import random
  random_num=random.randint(1, 100)
  num = int(input("Guess the number: "))
  counter =1

  while num!=random_num:
      if num>random_num:
          print("Guess a lower num")
      elif num<random_num:
          print("Guess a higher num")
      num = int(input("Guess the number: "))
      counter+=1
  else:
      print(f"Total attempt: {counter}")
      print("You guess the correct number")
  ```

- Range print using list

  ```py
  list(range(1,11))
  ```

- For loop range with skip steps

  ```py
  for i in range(1,11,2):
      print(i)
  ```

- Reverse loop

  ```py
  for i in range(11,-1,-1):
      print(i)
  ```

- Triangle pattern using nested loop

  ```py
  # triangle pattern using nested for loop
  for i in range(1,6):
      for j in range(1,i+1):
          print("*", end="")
      print("")
  ```

[⬆️ Go to Context](#context)

## **Loop Control Statements**

- `break`

  ```py
  # break
  for i in range(1,11):
      if i==5:
          break
      print(i)
  ```

- `continue`

  ```py
  # continue
  for i in range(1,10):
      if i==5:
          continue
      print(i)
  ```

- `pass`

  ```py
  # pass
  for i in range(1,11):
      pass
  ```

[⬆️ Go to Context](#context)

## **Code Visualization Tool**

- [Python Tutor](https://pythontutor.com/python-compiler.html)
- [Thonny](https://thonny.org/)

[⬆️ Go to Context](#context)

# [**Day 06 - Strings in Python**](./Day%2006%20-%20Strings%20in%20Python/)

## **Strings in Python**

### Creating Strings

- Single and multiline string

  ```py
  s = 'hello'
  s = "hello"

  # multiline strings
  s = '''hello'''
  s = """hello"""
  s = str('hello')
  print(s)
  ```

- String explicit type conversion (int to str)

  ```py
  a = 34
  str(a)
  ```

- `SyntaxError: unterminated string literal`

  - Use double quotes:

    ```py
    print("it's my birthday")
    ```

  - Escape the single quote:

    ```py
    print('it\'s my birthday')
    ```

  - Use triple quotes:

    ```py
    print('''it's my birthday''')
    ```

[⬆️ Go to Context](#context)

### Accessing Strings

- By Index (0-based)

  ```py
  s = "Python"
  print(s[0])  # P
  print(s[5])  # n
  ```

- Negative Indexing (from end)

  ```py
  s = "Python"
  print(s[-1])  # n
  print(s[-3])  # h
  ```

- String Slicing

  ```py
  s = "Python"
  print(s[0:3])   # Pyt
  print(s[2:])    # thon
  print(s[:4])    # Pyth
  print(s[::2])   # Pto
  ```

- Accessing Characters with Loop

  ```py
  s = "AI"
  for ch in s:
      print(ch)
  ```

- Index access

  ```py
  intro = "My name is Tansen"
  intro.index("T") - len(intro)
  ```

- Positive and negative index access (Multiple)

- Positive index using list comprehension

  ```py
  indices  = [i for i,c in enumerate(intro) if c =="n"]
  indices
  ```

- Negative index using list comprehension

  ```py
  neg_indices = [i - len(intro) for i in indices]
  neg_indices
  ```

[⬆️ Go to Context](#context)

### Adding Chars to Strings

- Using Concatenation (`+`)

  ```py
  s = "Hello"
  s = s + " World"
  print(s)  # Hello World
  ```

- Using `join()`

  ```py
  s = "-".join(["A", "B", "C"])
  print(s)  # A-B-C
  ```

[⬆️ Go to Context](#context)

### Editing Strings

- Strings are **immutable**, cannot change directly
- Using slicing and concatenation

  ```py
  s = "Hello"
  s = "J" + s[1:]
  print(s)  # Jello
  ```

- Using `replace()`

  ```py
  s = "Hello"
  s = s.replace("H", "J")
  print(s)  # Jello
  ```

[⬆️ Go to Context](#context)

### Deleting Strings

- Using `del` to remove entire string

  ```py
  s = "Hello"
  del s
  # print(s) → Error: s is not defined
  ```

[⬆️ Go to Context](#context)

### Operations on Strings

- Arithmetic Operations
  - Concatenation (` +`)

    ```py
    s1 = "Hello"
    s2 = "World"
    s3 = s1 + " " + s2
    print(s3)  # Hello World
    ```

  - Repetition (`*`)

    ```py
    s = "Hi! " * 3
    print(s)  # Hi! Hi! Hi!
    ```

- Relational Operations
  - Comparison (`==`, ` !=`, `<`, `>`, `<=`, `>=`)

    ```py
    s1 = "apple"
    s2 = "banana"
    print(s1 == s2)  # False
    print(s1 < s2)   # True
    ```

- Logical Operations
  - `and`, `or`, `not` on boolean results of comparisons

    ```py
    s1 = "apple"
    s2 = "banana"
    print(s1 < s2 and s2 > "aardvark")  # True
    print(not(s1 == s2))                 # True
    ```

- Loops on Strings
  - Iterating over characters

    ```py
    s = "Python"
    for ch in s:
        print(ch)
    ```

- Membership Operations
  - `in` and `not in`

    ```py
    s = "Python"
    print("P" in s)     # True
    print("z" not in s) # True
    ```

[⬆️ Go to Context](#context)

### String Functions

- `len()`: Get length of string

  ```py
  s = "Python"
  print(len(s))  # 6
  ```

- `ord()`: Get ASCII/Unicode value of character

  ```py
  print(ord('A'))  # 65
  ```

- `chr()`: Get character from ASCII/Unicode value

  ```py
  print(chr(65))  # 'A'
  ```

- `max()`: Get character with maximum ASCII value

  ```py
  s = "Python"
  print(max(s))  # y
  ```

- `min()`: Get character with minimum ASCII value

  ```py
  s = "Python"
  print(min(s))  # P
  ```

- `sorted()`: Return sorted list of characters

  ```py
  s = "Python"
  print(sorted(s))  # ['P', 'h', 'n', 'o', 't', 'y']
  ```

- `reversed()`: Return iterator to reverse string

  ```py
  s = "Python"
  print(''.join(reversed(s)))  # nohtyP
  ```

- `type()`: Get type of object

  ```py
  s = "Python"
  print(type(s))  # <class 'str'>
  ```

[⬆️ Go to Context](#context)

### String Methods

- `upper()`: Convert string to uppercase

  ```py
  s = "hello"
  print(s.upper())  # HELLO
  ```

- `lower()`: Convert string to lowercase

  ```py
  s = "HELLO"
  print(s.lower())  # hello
  ```

- `capitalize()`: Capitalize first character

  ```py
  s = "hello"
  print(s.capitalize())  # Hello
  ```

- `title()`: Capitalize first character of each word

  ```py
  s = "hello world"
  print(s.title())  # Hello World
  ```

- `strip()`: Remove leading and trailing whitespace

  ```py
  s = "  hello  "
  print(s.strip())  # hello
  ```

- `replace()`: Replace substring with another

  ```py
  s = "Hello World"
  print(s.replace("World", "Python"))  # Hello Python
  ```

- `split()`: Split string into list by separator

  ```py
  s = "a,b,c"
  print(s.split(","))  # ['a', 'b', 'c']
  ```

- `join()`: Join list of strings with separator

  ```py
  lst = ["a","b","c"]
  print("-".join(lst))  # a-b-c
  ```

- `find()`: Find index of substring (-1 if not found)

  ```py
  s = "Python"
  print(s.find("t"))  # 2
  ```

- `count()`: Count occurrences of substring

  ```py
  s = "banana"
  print(s.count("a"))  # 3
  ```

- `startswith()`: Check if string starts with substring

  ```py
  s = "Python"
  print(s.startswith("Py"))  # True
  ```

- `endswith()`: Check if string ends with substring

  ```py
  s = "Python"
  print(s.endswith("on"))  # True
  ```

- `isalpha()`: Check if all characters are alphabetic

  ```py
  s = "Python"
  print(s.isalpha())  # True
  ```

- `isalnum()`: Check if all characters are number

  ```py
  s = "123"
  print(s.isalnum())  # True
  ```

- `isdigit()`: Check if all characters are digits

  ```py
  s = "123"
  print(s.isdigit())  # True
  ```

- `isspace()`: Check if string contains only whitespace

  ```py
  s = "   "
  print(s.isspace())  # True
  ```

- `isidentifier()`: Checks if a string is a **valid Python identifier** (variable, function, class name).


  ```py
  s1 = "variable1"
  s2 = "1variable"
  print(s1.isidentifier())  # True
  print(s2.isidentifier())  # False
  ```

[⬆️ Go to Context](#context)

## **Strings Exercise**

### Find the length of a given string without using the len() function

```py
s = input("Enter a String: ")

counter = 1
for i in s:
    counter += 1

print(counter)
```

### Extract username from a given email

- If the email is `aatansen@gmail.com`
- Then the username should be `aatansen`

  ```py
  # email = "aatansen@gmail.com"
  email = input("Enter your email: ")
  pos = email.index("@")
  print(email[0:pos])
  ```

[⬆️ Go to Context](#context)

# [**Day 07 - List in Python**](./Day%2007%20-%20List%20in%20Python/)

## **List in Python**

### What are Lists?

- List is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.

  - A list is an **ordered**, **mutable**, and **dynamic** collection of elements.
  - Created using **square brackets `[]`** or the **list()** constructor.

- **Characteristics**
  - **Ordered** — Maintains insertion order
  - **Mutable / Changeable** — Elements can be modified
  - **Heterogeneous** — Can store different data types
  - **Allows Duplicates** — Repeated values are allowed
  - **Dynamic Size** — Can grow or shrink automatically
  - **Index-Based Access** — Supports positive and negative indexing
  - **Can Be Nested** — Lists can contain other lists
  - **Can Store Any Python Object** — Numbers, strings, functions, classes, etc.
  - **More Memory Usage** than tuples
  - **Slower** compared to tuples due to mutability

    ```py
    my_list = [10, "Hello", 3.14, True]
    print(my_list)
    ```

[⬆️ Go to Context](#context)

### Lists Vs Arrays

- **Lists**
  - Can store elements of **different data types**
  - Part of **core Python**
  - Flexible but slower for large numeric data

    ```py
    my_list = [1, "two", 3.0, True]
    print(my_list)
    ```

- **Arrays**
  - Can store elements of **same data type only**
  - Need to import from **array module** or **NumPy**
  - More **memory-efficient** for numeric operations

    ```py
    import array
    arr = array.array('i', [1, 2, 3, 4])
    print(arr)
    ```

  - **Key Differences**
    - **Data Type:** Lists → Heterogeneous | Arrays → Homogeneous
    - **Speed:** Arrays are faster for numeric operations
    - **Size:** Lists → Dynamic | Arrays → Fixed (unless NumPy array)
    - **Memory:** Arrays use less memory than lists
    - **Usage:** Lists are flexible | Arrays are optimized for computation

    ```mermaid
    flowchart TD

        %% --- Python List Section ---
        subgraph L1["Python List"]
            direction LR
            L1desc["(Dynamic Array: grows automatically)"]
            L1A["Index 0 → 10"]
            L1B["Index 1 → 20"]
            L1C["Index 2 → 30"]
        end

        %% --- Array Section ---
        subgraph A1["Array Module"]
            direction LR
            A1desc["(Fixed Size: array('i', [10,20,30]))"]
            A1A["Index 0 → 10"]
            A1B["Index 1 → 20"]
            A1C["Index 2 → 30"]
        end

        L1 -->|"append(40)"| L2
        A1 -->|"add new value"| A2

        %% --- After Adding Value (List) ---
        subgraph L2["After append(40)"]
            direction LR
            L2A["🆕 New Memory Block Allocated"]
            L2B["Values Copied: 10, 20, 30, 40"]
        end

        %% --- After Adding Value (Array) ---
        subgraph A2["Array Overflow"]
            direction LR
            A2A["❌ Memory Full"]
            A2B["✅ Must create new array and copy values"]
        end

        %% --- Style Definitions ---
        classDef list fill:#2E86C1,stroke:#1B4F72,color:#fff,font-weight:bold;
        classDef array fill:#B9770E,stroke:#873600,color:#fff,font-weight:bold;
        classDef resized fill:#1E8449,stroke:#145A32,color:#fff,font-weight:bold;
        classDef overflow fill:#C0392B,stroke:#641E16,color:#fff,font-weight:bold;

        class L1,L1A,L1B,L1C,L1desc list;
        class A1,A1A,A1B,A1C,A1desc array;
        class L2,L2A,L2B resized;
        class A2,A2A,A2B overflow;
    ```

[⬆️ Go to Context](#context)

### Characteristics of a List

- **Ordered** — Elements maintain their insertion order
- **Changeable / Mutable** — Elements can be modified after creation
- **Heterogeneous** — Can store elements of different data types
- **Can Have Duplicates** — Allows repeated elements
- **Dynamic** — Size can grow or shrink as needed
- **Can Be Nested** — Lists can contain other lists
- **Index-Based Access** — Elements can be accessed using indices
- **Can Contain Any Python Object** — Strings, numbers, lists, tuples, functions, etc.

[⬆️ Go to Context](#context)

### How to create a list

- Using square brackets `[]`

  ```py
  my_list = [1, 2, 3, 4]
  ```

- Using `list()` constructor

  ```py
  my_list = list((1, 2, 3, 4))
  ```

- Empty list

  ```py
  my_list = []
  ```

- Heterogeneous list

  ```py
  my_list = [1, "Hello", 3.5, True]
  ```

- Nested list

  ```py
  my_list = [[1, 2], [3, 4]]
  ```

[⬆️ Go to Context](#context)

### Access items from a List

- Using index (0-based)

  ```py
  my_list = [10, 20, 30, 40]
  print(my_list[1])  # 20
  ```

- Using negative index (from end)

  ```py
  my_list = [10, 20, 30, 40]
  print(my_list[-1])  # 40
  ```

- Using slicing

  ```py
  my_list = [10, 20, 30, 40, 50]
  print(my_list[1:4])  # [20, 30, 40]
  ```

- Accessing nested list

  ```py
  my_list = [[1, 2], [3, 4]]
  print(my_list[1][0])  # 3
  ```

[⬆️ Go to Context](#context)

### List Methods

- `append()` — Add an item to the end

  ```py
  my_list = [1, 2, 3]
  my_list.append(4)
  print(my_list)  # [1, 2, 3, 4]
  ```

- `extend()` — Add multiple items from another list

  ```py
  my_list = [1, 2, 3]
  my_list.extend([4, 5])
  print(my_list)  # [1, 2, 3, 4, 5]
  ```

- `insert()` — Insert item at specific position

  ```py
  my_list = [1, 3, 4]
  my_list.insert(1, 2)
  print(my_list)  # [1, 2, 3, 4]
  ```

- `remove()` — Remove first occurrence of an item

  ```py
  my_list = [1, 2, 3, 2]
  my_list.remove(2)
  print(my_list)  # [1, 3, 2]
  ```

- `pop()` — Remove and return item by index (default last)

  ```py
  my_list = [1, 2, 3]
  my_list.pop()
  print(my_list)  # [1, 2]
  ```

- `clear()` — Remove all elements

  ```py
  my_list = [1, 2, 3]
  my_list.clear()
  print(my_list)  # []
  ```

- `index()` — Return index of first occurrence

  ```py
  my_list = [10, 20, 30, 20]
  print(my_list.index(20))  # 1
  ```

- `count()` — Count occurrences of item

  ```py
  my_list = [1, 2, 2, 3]
  print(my_list.count(2))  # 2
  ```

- `sort()` — Sort list in ascending order

  ```py
  my_list = [3, 1, 2]
  my_list.sort()
  print(my_list)  # [1, 2, 3]
  ```

- `reverse()` — Reverse order of list

  ```py
  my_list = [1, 2, 3]
  my_list.reverse()
  print(my_list)  # [3, 2, 1]
  ```

- `copy()` — Return shallow copy of list

  ```py
  my_list = [1, 2, 3]
  new_list = my_list.copy()
  print(new_list)  # [1, 2, 3]
  ```

[⬆️ Go to Context](#context)

### List Functions

- `len()` — Returns number of elements in list

  ```py
  my_list = [1, 2, 3]
  print(len(my_list))  # 3
  ```

- `max()` — Returns maximum element

  ```py
  my_list = [1, 5, 3]
  print(max(my_list))  # 5
  ```

- `min()` — Returns minimum element

  ```py
  my_list = [1, 5, 3]
  print(min(my_list))  # 1
  ```

- `sum()` — Returns sum of elements

  ```py
  my_list = [1, 2, 3]
  print(sum(my_list))  # 6
  ```

- `sorted()` — Returns sorted list (ascending by default)

  ```py
  my_list = [3, 1, 2]
  print(sorted(my_list))  # [1, 2, 3]
  ```

- `reversed()` — Returns iterator to reverse list

  ```py
  my_list = [1, 2, 3]
  print(list(reversed(my_list)))  # [3, 2, 1]
  ```

- `any()` — Returns True if any element is True

  ```py
  my_list = [0, 0, 1]
  print(any(my_list))  # True
  ```

- `all()` — Returns True if all elements are True

  ```py
  my_list = [1, 2, 3]
  print(all(my_list))  # True
  ```

[⬆️ Go to Context](#context)

### Editing items in a List

  ```py
  # editing with slicing
  L = [1,2,3,4]
  L[1:4] = [200,300,400]
  print(L)
  ```

[⬆️ Go to Context](#context)

### Deleting items from a List

  ```py
  L = [1,2,3,4]
  del L[0]
  print(L)
  ```

[⬆️ Go to Context](#context)

### Operations on Lists

- **Concatenation (` +`)**

  ```py
  list1 = [1, 2]
  list2 = [3, 4]
  result = list1 + list2
  print(result)  # [1, 2, 3, 4]
  ```

- **Repetition (`*`)**

  ```py
  list1 = [1, 2]
  result = list1 * 3
  print(result)  # [1, 2, 1, 2, 1, 2]
  ```

- **Membership (`in`, `not in`)**

  ```py
  list1 = [1, 2, 3]
  print(2 in list1)     # True
  print(5 not in list1) # True
  ```

- **Iteration / Loops**

  ```py
  list1 = [1, 2, 3]
  for item in list1:
      print(item)
  ```

- **Indexing and Slicing**

  ```py
  list1 = [10, 20, 30, 40]
  print(list1[1])    # 20
  print(list1[1:3])  # [20, 30]
  ```

- **Length (`len()`)**

  ```py
  list1 = [1, 2, 3, 4]
  print(len(list1))  # 4
  ```

- **Minimum and Maximum (`min()`, `max()`)**

  ```py
  list1 = [5, 2, 9]
  print(min(list1))  # 2
  print(max(list1))  # 9
  ```

- **Sum (`sum()`)**

  ```py
  list1 = [1, 2, 3]
  print(sum(list1))  # 6
  ```

[⬆️ Go to Context](#context)

### List comprehension

- A concise way to **create lists** using a single line of code with loops and conditions.

- Basic Syntax

  ```py
  [expression for item in iterable if condition]
  ```

- Squares of numbers

  ```py
  squares = [x**2 for x in range(5)]
  print(squares)  # [0, 1, 4, 9, 16]
  ```

- Even numbers only

  ```py
  evens = [x for x in range(10) if x % 2 == 0]
  print(evens)  # [0, 2, 4, 6, 8]
  ```

- Convert strings to uppercase

  ```py
  fruits = ["apple", "banana", "cherry"]
  fruits_upper = [f.upper() for f in fruits]
  print(fruits_upper)  # ['APPLE', 'BANANA', 'CHERRY']
  ```

- Nested List Comprehension

  ```py
  matrix = [[1,2,3],[4,5,6]]
  flat = [num for row in matrix for num in row]
  print(flat)  # [1, 2, 3, 4, 5, 6]
  ```

[⬆️ Go to Context](#context)

### `zip()` Function in Python

- Combines multiple iterables (lists, tuples, etc.) element-wise into a single iterator of tuples.

- Syntax

  ```py
  zip(iterable1, iterable2, ...)
  ```

- Example — Basic usage

  ```py
  list1 = [1, 2, 3]
  list2 = ['a', 'b', 'c']
  zipped = zip(list1, list2)
  print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
  ```

- Example — More than two iterables

  ```py
  nums = [1, 2, 3]
  chars = ['x', 'y', 'z']
  bools = [True, False, True]
  zipped = zip(nums, chars, bools)
  print(list(zipped))  # [(1, 'x', True), (2, 'y', False), (3, 'z', True)]
  ```

- Example — Iterating directly

  ```py
  for num, char in zip([1,2], ['a','b']):
      print(num, char)
  # Output:
  # 1 a
  # 2 b
  ```

> [!NOTE]
>
> - Stops at the **shortest iterable**
> - Can be combined with `list()`, `dict()`, or unpacking

[⬆️ Go to Context](#context)

# **Day 08 - Tuples, Sets & Dictionary**

## **Tuples**

- **Tuples in Python**
  - A tuple is an **ordered**, **immutable** collection of elements.
  - Created using **parentheses `()`** or the **tuple()** constructor.

- **Characteristics**
  - **Ordered** — Maintains insertion order
  - **Immutable** — Cannot be changed after creation
  - **Heterogeneous** — Can store different data types
  - **Allows Duplicates** — Repeated items are allowed
  - **Index-Based Access** — Access elements using indices
  - **Hashable (if all elements are immutable)** — Can be used as dictionary keys
  - **Faster than lists** due to immutability
  - **Can be nested** — Tuples inside tuples
  - **Uses less memory** than lists

    ```py
    my_tuple = (10, "Hello", 3.14, True)
    print(my_tuple)
    ```

[⬆️ Go to Context](#context)

### Creating a Tuple

- Using parentheses `()`

  ```py
  t = (1, 2, 3)
  ```

- Without parentheses (tuple packing)

  ```py
  t = 1, 2, 3
  ```

- Single-element tuple (requires comma)

  ```py
  t = (5,)
  ```

- Using `tuple()` constructor

  ```py
  t = tuple([1, 2, 3])
  ```

[⬆️ Go to Context](#context)

### Accessing Items in Tuple

- Using index

  ```py
  t = (10, 20, 30)
  print(t[1])  # 20
  ```

- Negative indexing

  ```py
  t = (10, 20, 30)
  print(t[-1])  # 30
  ```

- Slicing

  ```py
  t = (1, 2, 3, 4)
  print(t[1:3])  # (2, 3)
  ```

[⬆️ Go to Context](#context)

### Editing Items in Tuple

- Not possible — tuples are **immutable**

  ```py
  t = (1, 2, 3)
  # t[0] = 5  → Error
  ```

[⬆️ Go to Context](#context)

### Adding Items in Tuple

- Create a **new tuple** using concatenation

  ```py
  t = (1, 2, 3)
  t = t + (4,)
  print(t)  # (1, 2, 3, 4)
  ```

[⬆️ Go to Context](#context)

### Deleting Items in Tuple

- Delete entire tuple

  ```py
  t = (1, 2, 3)
  del t
  # print(t) → Error: t is not defined
  ```

[⬆️ Go to Context](#context)

### Operations on Tuples

- Concatenation (` +`)

  ```py
  t1 = (1, 2)
  t2 = (3, 4)
  result = t1 + t2
  print(result)  # (1, 2, 3, 4)
  ```

- Repetition (`*`)

  ```py
  t = (1, 2)
  result = t * 3
  print(result)  # (1, 2, 1, 2, 1, 2)
  ```

- Membership (`in`, `not in`)

  ```py
  t = (10, 20, 30)
  print(20 in t)      # True
  print(50 not in t)  # True
  ```

- Indexing & Slicing

  ```py
  t = (5, 10, 15, 20)
  print(t[2])     # 15
  print(t[1:3])   # (10, 15)
  ```

- Iteration

  ```py
  t = ("a", "b", "c")
  for item in t:
      print(item)
  ```

- Length (`len()`)

  ```py
  t = (1, 2, 3)
  print(len(t))  # 3
  ```

- Maximum & Minimum (`max()`, `min()`)

  ```py
  t = (5, 2, 9)
  print(max(t))  # 9
  print(min(t))  # 2
  ```

- Count occurrences (`count()`)

  ```py
  t = (1, 2, 2, 3)
  print(t.count(2))  # 2
  ```

- Find index (`index()`)

  ```py
  t = (10, 20, 30)
  print(t.index(20))  # 1
  ```

[⬆️ Go to Context](#context)

### Tuple Methods

- **count() – Count occurrences of a value**

  ```py
  t = (1, 2, 2, 3, 2)
  print(t.count(2))  # 3
  ```

- **index() – Find the index of a value**

  ```py
  t = ("apple", "banana", "mango", "banana")
  print(t.index("banana"))  # 1
  ```

[⬆️ Go to Context](#context)

### Tuple Functions

- Length (`len()`)

  ```py
  t = (10, 20, 30)
  print(len(t))  # 3
  ```

- Maximum Value (`max()`)

  ```py
  t = (5, 9, 2)
  print(max(t))  # 9
  ```

- Minimum Value (`min()`)

  ```py
  t = (5, 9, 2)
  print(min(t))  # 2
  ```

- Sum of Elements (`sum()`)

  ```py
  t = (1, 2, 3, 4)
  print(sum(t))  # 10
  ```

- Sorting (`sorted()`)

  ```py
  t = (3, 1, 2)
  print(sorted(t))  # [1, 2, 3]
  ```

- Convert to List (`list()`)

  ```py
  t = (1, 2, 3)
  lst = list(t)
  print(lst)  # [1, 2, 3]
  ```

- Convert to Tuple (`tuple()`)

  ```py
  lst = [4, 5, 6]
  t = tuple(lst)
  print(t)  # (4, 5, 6)
  ```

- Check Type (`type()`)

  ```py
  t = (10, 20)
  print(type(t))  # <class 'tuple'>
  ```

- Check if any element is True (`any()`)

  ```py
  t = (0, False, 5)
  print(any(t))  # True
  ```

- Check if all elements are True (`all()`)

  ```py
  t = (1, 2, 3)
  print(all(t))  # True
  ```

[⬆️ Go to Context](#context)

### Tuple Unpacking

- Basic Unpacking

  ```py
  t = (10, 20, 30)
  a, b, c = t
  print(a, b, c)  # 10 20 30
  ```

- Unpacking with Different Variable Names

  ```py
  person = ("TT", 25, "Bangladesh")
  name, age, country = person
  print(name, age, country)  # TT 25 Bangladesh
  ```

- Unpacking with Asterisk (`*`)

  ```py
  t = (1, 2, 3, 4, 5)
  a, *b = t
  print(a)  # 1
  print(b)  # [2, 3, 4, 5]
  ```

- Asterisk in Middle

  ```py
  t = (10, 20, 30, 40, 50)
  a, *b, c = t
  print(a)  # 10
  print(b)  # [20, 30, 40]
  print(c)  # 50
  ```

- Nested Tuple Unpacking

  ```py
  t = ("TT", (10, 20))
  name, (x, y) = t
  print(name)  # TT
  print(x, y)  # 10 20
  ```

[⬆️ Go to Context](#context)

### Using `zip()` with Tuples

- Basic Zip

  ```py
  t1 = (1, 2, 3)
  t2 = ('a', 'b', 'c')
  zipped = zip(t1, t2)
  print(tuple(zipped))  # ((1, 'a'), (2, 'b'), (3, 'c'))
  ```

- Zip Multiple Tuples

  ```py
  t1 = (1, 2, 3)
  t2 = ('x', 'y', 'z')
  t3 = (True, False, True)
  zipped = zip(t1, t2, t3)
  print(tuple(zipped))  # ((1, 'x', True), (2, 'y', False), (3, 'z', True))
  ```

- Iterating Over Zipped Tuples

  ```py
  t1 = (1, 2, 3)
  t2 = ('a', 'b', 'c')
  for num, char in zip(t1, t2):
      print(num, char)
  # Output:
  # 1 a
  # 2 b
  # 3 c
  ```

- Unzipping Tuples

  ```py
  zipped = ((1, 'a'), (2, 'b'), (3, 'c'))
  t1, t2 = zip(*zipped)
  print(t1)  # (1, 2, 3)
  print(t2)  # ('a', 'b', 'c')
  ```

[⬆️ Go to Context](#context)

### Tuple Comprehension

- Python does **not have true tuple comprehensions**. Using parentheses `()` creates a **generator expression**, not a tuple.

  - Example (Generator Expression)

    ```py
    t_gen = (x*2 for x in range(5))
    print(t_gen)  # <generator object ...>
    print(list(t_gen))  # [0, 2, 4, 6, 8]
    ```

  - Convert Generator to Tuple

    ```py
    t = tuple(x*2 for x in range(5))
    print(t)  # (0, 2, 4, 6, 8)
    ```

  - With Condition

    ```py
    t = tuple(x for x in range(10) if x%2==0)
    print(t)  # (0, 2, 4, 6, 8)
    ```

[⬆️ Go to Context](#context)

### List vs Tuple

- **Mutability**
  - List → Mutable (can modify elements)
  - Tuple → Immutable (cannot modify elements)

- **Syntax**
  - List → Square brackets `[]`
  - Tuple → Parentheses `()`

- **Order**
  - Both are ordered (maintain insertion order)

- **Duplicates**
  - Both allow duplicates

- **Heterogeneity**
  - Both can store heterogeneous elements

- **Memory Usage**
  - List → Uses more memory
  - Tuple → More memory efficient

- **Speed**
  - List → Slower for iteration and operations
  - Tuple → Faster due to immutability

- **Methods**
  - List → Many methods like append, insert, remove, pop, sort
  - Tuple → Only count() and index()

- **Use Cases**
  - List → Use when collection may change
  - Tuple → Use when data should not change, faster access, can be used as dictionary key

[⬆️ Go to Context](#context)

## **Sets**

- **Set in Python**

  - **Definition**
    - A set is an **unordered**, **mutable**, and **unique** collection of elements.
    - Created using **curly braces `{}`** or the **set()** constructor.

  - **Characteristics**
    - **Unordered** — Does not maintain insertion order
    - **Mutable** — Elements can be added or removed
    - **Unique Elements** — Duplicates are automatically removed
    - **Heterogeneous** — Can store multiple data types (numbers, strings, tuples, etc.)
    - **Unindexed** — Cannot access elements by index
    - **Supports Set Operations** — Union, intersection, difference, symmetric difference
    - **Can Be Nested with Immutable Types** — Cannot have sets inside sets, but can contain tuples
    - **Faster Membership Testing** than lists or tuples

      ```py
      my_set = {1, 2, 3, 3}
      print(my_set)  # {1, 2, 3}
      ```

[⬆️ Go to Context](#context)

### Creating a Set

- Using curly braces

  ```py
  my_set = {1, 2, 3}
  ```

- Using `set()` constructor

  ```py
  my_set = set([1, 2, 3])
  ```

- Empty set

  ```py
  my_set = set()
  ```

### Accessing Items in Set

- Sets are **unordered**, so cannot access by index

  ```py
  my_set = {1, 2, 3}
  for item in my_set:
      print(item)
  ```

### Editing Items in Set

- Not possible directly, but can **remove and add** elements

### Adding Items in Set

- Using `add()`

  ```py
  my_set = {1, 2}
  my_set.add(3)
  print(my_set)  # {1, 2, 3}
  ```

- Using `update()` (multiple items)

  ```py
  my_set = {1, 2}
  my_set.update([3, 4, 5])
  print(my_set)  # {1, 2, 3, 4, 5}
  ```

### Deleting Items in Set

- Using `remove()` (raises error if not found)

  ```py
  my_set = {1, 2, 3}
  my_set.remove(2)
  print(my_set)  # {1, 3}
  ```

- Using `discard()` (no error if not found)

  ```py
  my_set = {1, 2, 3}
  my_set.discard(4)
  print(my_set)  # {1, 2, 3}
  ```

- Using `pop()` (removes arbitrary element)

  ```py
  my_set = {1, 2, 3}
  print(my_set.pop())  # 1 (or any element)
  ```

- Using `clear()` (remove all items)

  ```py
  my_set = {1, 2, 3}
  my_set.clear()
  print(my_set)  # set()
  ```

[⬆️ Go to Context](#context)

### Operations on Set

- Union (`|` or `union()`)

  ```py
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  print(set1 | set2)        # {1, 2, 3, 4, 5}
  print(set1.union(set2))   # {1, 2, 3, 4, 5}
  ```

- Intersection (`&` or `intersection()`)

  ```py
  set1 = {1, 2, 3}
  set2 = {2, 3, 4}
  print(set1 & set2)             # {2, 3}
  print(set1.intersection(set2)) # {2, 3}
  ```

- Difference (` -` or `difference()`)

  ```py
  set1 = {1, 2, 3}
  set2 = {2, 3, 4}
  print(set1 - set2)            # {1}
  print(set1.difference(set2))  # {1}
  ```

- Symmetric Difference (`^` or `symmetric_difference()`)

  ```py
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  print(set1 ^ set2)                        # {1, 2, 4, 5}
  print(set1.symmetric_difference(set2))   # {1, 2, 4, 5}
  ```

- Membership Testing (`in`, `not in`)

  ```py
  s = {1, 2, 3}
  print(2 in s)      # True
  print(5 not in s)  # True
  ```

- Iteration on Set

  - Using for loop

    ```py
    my_set = {1, 2, 3}
    for item in my_set:
        print(item)
    # Output may vary in order, e.g., 1 2 3
    ```

  - Using set comprehension

    ```py
    my_set = {1, 2, 3, 4}
    squared = {x**2 for x in my_set}
    print(squared)  # {1, 4, 9, 16}
    ```

- Subset (`<=`, `issubset()`)

  ```py
  set1 = {1, 2}
  set2 = {1, 2, 3}
  print(set1 <= set2)           # True
  print(set1.issubset(set2))    # True
  ```

- Superset (`>=`, `issuperset()`)

  ```py
  set1 = {1, 2, 3}
  set2 = {1, 2}
  print(set1 >= set2)           # True
  print(set1.issuperset(set2))  # True
  ```

[⬆️ Go to Context](#context)

### Set Methods

- `add()` – Add a single element

  ```py
  s = {1, 2}
  s.add(3)
  print(s)  # {1, 2, 3}
  ```

- `update()` – Add multiple elements

  ```py
  s = {1, 2}
  s.update([3, 4, 5])
  print(s)  # {1, 2, 3, 4, 5}
  ```

- `remove()` – Remove an element (raises error if not found)

  ```py
  s = {1, 2, 3}
  s.remove(2)
  print(s)  # {1, 3}
  ```

- `discard()` – Remove an element (no error if not found)

  ```py
  s = {1, 2, 3}
  s.discard(4)
  print(s)  # {1, 2, 3}
  ```

- `pop()` – Remove and return an arbitrary element

  ```py
  s = {1, 2, 3}
  print(s.pop())  # 1 (or any element)
  print(s)        # Remaining elements
  ```

- `clear()` – Remove all elements

  ```py
  s = {1, 2, 3}
  s.clear()
  print(s)  # set()
  ```

- `copy()` – Return a shallow copy of the set

  ```py
  s1 = {1, 2, 3}
  s2 = s1.copy()
  print(s2)  # {1, 2, 3}
  ```

- `union()` – Return a new set with all elements from both sets

  ```py
  s1 = {1, 2}
  s2 = {2, 3}
  print(s1.union(s2))  # {1, 2, 3}
  ```

- `intersection()` – Return common elements

  ```py
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  print(s1.intersection(s2))  # {2, 3}
  ```

- `intersection_update()` – Update set to keep only common elements

  ```py
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.intersection_update(s2)
  print(s1)  # {2, 3}
  ```

- `difference()` – Elements in first set but not in second

  ```py
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  print(s1.difference(s2))  # {1}
  ```

- `difference_update()` – Remove elements found in another set

  ```py
  s1 = {1, 2, 3}
  s2 = {2, 3}
  s1.difference_update(s2)
  print(s1)  # {1}
  ```

- `symmetric_difference()` – Elements in either set but not both

  ```py
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  print(s1.symmetric_difference(s2))  # {1, 2, 4, 5}
  ```

- `symmetric_difference_update()` – Update set with symmetric difference

  ```py
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  s1.symmetric_difference_update(s2)
  print(s1)  # {1, 2, 4, 5}
  ```

- `issubset()` – Check if set is subset of another

  ```py
  s1 = {1, 2}
  s2 = {1, 2, 3}
  print(s1.issubset(s2))  # True
  ```

- `issuperset()` – Check if set is superset of another

  ```py
  s1 = {1, 2, 3}
  s2 = {1, 2}
  print(s1.issuperset(s2))  # True
  ```

- `isdisjoint()` – Check if sets have no elements in common

  ```py
  s1 = {1, 2}
  s2 = {3, 4}
  print(s1.isdisjoint(s2))  # True
  ```

[⬆️ Go to Context](#context)

### Set Functions

- `len()` – Length of the set

  ```py
  s = {1, 2, 3}
  print(len(s))  # 3
  ```

- `max()` – Maximum element

  ```py
  s = {5, 2, 8}
  print(max(s))  # 8
  ```

- `min()` – Minimum element

  ```py
  s = {5, 2, 8}
  print(min(s))  # 2
  ```

- `sum()` – Sum of elements

  ```py
  s = {1, 2, 3, 4}
  print(sum(s))  # 10
  ```

- `any()` – Returns True if any element is truthy

  ```py
  s = {0, False, 5}
  print(any(s))  # True
  ```

- `all()` – Returns True if all elements are truthy

  ```py
  s = {1, 2, 3}
  print(all(s))  # True
  ```

- `sorted()` – Return sorted elements as a list

  ```py
  s = {3, 1, 2}
  print(sorted(s))  # [1, 2, 3]
  ```

- `type()` – Check the type**

  ```py
  s = {1, 2, 3}
  print(type(s))  # <class 'set'>
  ```

[⬆️ Go to Context](#context)

### Frozenset in Python

- An immutable version of a set.
- Elements cannot be added or removed once created.
- Created using `frozenset()`.

  ```py
  fs = frozenset([1, 2, 3, 3])
  print(fs)  # frozenset({1, 2, 3})
  ```

- Operations Allowed
  - Can perform union, intersection, difference, symmetric difference

    ```py
    fs1 = frozenset([1, 2, 3])
    fs2 = frozenset([2, 3, 4])
    print(fs1.union(fs2))  # frozenset({1, 2, 3, 4})
    print(fs1.intersection(fs2))  # frozenset({2, 3})
    ```

- Not Allowed
  - No `add()`, `remove()`, `pop()`, or `clear()` methods.

[⬆️ Go to Context](#context)

### Set Comprehension

- A concise way to create a set using expressions inside curly braces `{}`.

  ```py
  s = {x*2 for x in range(5)}
  print(s)  # {0, 2, 4, 6, 8}
  ```

- With Condition

  ```py
  s = {x for x in range(10) if x%2 == 0}
  print(s)  # {0, 2, 4, 6, 8}
  ```

- From Another Collection

  ```py
  lst = [1, 2, 2, 3, 4]
  s = {x for x in lst}
  print(s)  # {1, 2, 3, 4}
  ```

[⬆️ Go to Context](#context)

### Using `zip()` with Sets

- `zip()` can combine multiple iterables element-wise.
- When used with sets, the iteration order is **arbitrary** because sets are unordered.

    ```py
    s1 = {1, 2, 3}
    s2 = {'a', 'b', 'c'}
    zipped = zip(s1, s2)
    print(list(zipped))  # Example output: [(1, 'b'), (2, 'a'), (3, 'c')]
    ```

- **Iterating Directly**

  ```py
  s1 = {1, 2, 3}
  s2 = {'x', 'y', 'z'}
  for num, char in zip(s1, s2):
      print(num, char)
  # Output order may vary because sets are unordered
  ```

- **Unzipping**

  ```py
  zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
  s1, s2 = zip(*zipped)
  print(s1)  # (1, 2, 3)
  print(s2)  # ('a', 'b', 'c')
  ```

[⬆️ Go to Context](#context)

## **Dictionary**

- A dictionary is an **unordered**, **mutable**, and **key-value pair** collection.
- Keys must be **unique and immutable** (strings, numbers, tuples, etc.).
- Values can be **any data type** and duplicates are allowed.
- Created using **curly braces `{}`** or the **dict()** constructor.

- **Characteristics**
  - **Unordered** — Items have no fixed position (Python 3.7+ preserves insertion order as implementation detail)
  - **Mutable** — Can add, modify, or delete items
  - **Key-Value Pairs** — Data stored in key:value format
  - **Unique Keys** — Duplicate keys are not allowed
  - **Heterogeneous** — Keys and values can be of different data types
  - **Dynamic** — Can grow or shrink as needed
  - **Nested Structures Allowed** — Dictionaries can contain lists, tuples, or other dictionaries

    ```py
    my_dict = {"name": "TT", "age": 25, "country": "Bangladesh"}
    print(my_dict)  # {'name': 'TT', 'age': 25, 'country': 'Bangladesh'}
    ```

[⬆️ Go to Context](#context)

### Creating a Dictionary

- Using curly braces

  ```py
  my_dict = {"name": "TT", "age": 25}
  ```

- Using `dict()` constructor

  ```py
  my_dict = dict(name="TT", age=25)
  ```

- Empty dictionary

  ```py
  my_dict = {}
  ```

[⬆️ Go to Context](#context)

### Accessing Items in Dictionary

- Using `key`

  ```py
  my_dict = {"name": "TT", "age": 25}
  print(my_dict["name"])  # TT
  ```

- Using `get()`

  ```py
  print(my_dict.get("age"))  # 25
  ```

[⬆️ Go to Context](#context)

### Editing Items in Dictionary

- Modifying value

  ```py
  my_dict["age"] = 26
  print(my_dict)  # {'name': 'TT', 'age': 26}
  ```

[⬆️ Go to Context](#context)

### Adding Items in Dictionary

- Adding new key-value pair

  ```py
  my_dict["country"] = "Bangladesh"
  print(my_dict)  # {'name': 'TT', 'age': 26, 'country': 'Bangladesh'}
  ```

- Using `update()`

  ```py
  my_dict.update({"city": "Dhaka"})
  print(my_dict)  # {'name': 'TT', 'age': 26, 'country': 'Bangladesh', 'city': 'Dhaka'}
  ```

[⬆️ Go to Context](#context)

### Deleting Items in Dictionary

- Using `pop()`

  ```py
  my_dict.pop("city")
  print(my_dict)  # {'name': 'TT', 'age': 26, 'country': 'Bangladesh'}
  ```

- Using `popitem()` (removes last inserted item)

  ```py
  my_dict.popitem()
  print(my_dict)  # {'name': 'TT', 'age': 26}
  ```

- Using `del`

  ```py
  del my_dict["age"]
  print(my_dict)  # {'name': 'TT'}
  ```

- Using `clear()` (removes all items)

  ```py
  my_dict.clear()
  print(my_dict)  # {}
  ```

[⬆️ Go to Context](#context)

### Operations on Dictionary

- Membership Testing (`in`, `not in`)

  ```py
  my_dict = {"name": "TT", "age": 25}
  print("name" in my_dict)      # True
  print("country" not in my_dict)  # True
  ```

- Iteration over Keys

  ```py
  my_dict = {"name": "TT", "age": 25}
  for key in my_dict:
      print(key)
  # Output: name, age
  ```

- Iteration over Values

  ```py
  for value in my_dict.values():
      print(value)
  # Output: TT, 25
  ```

- Iteration over Items (key-value pairs)

  ```py
  for key, value in my_dict.items():
      print(key, value)
  # Output: name TT, age 25
  ```

- Length (`len()`)

  ```py
  print(len(my_dict))  # 2
  ```

- Copying Dictionary

  ```py
  new_dict = my_dict.copy()
  print(new_dict)  # {'name': 'TT', 'age': 25}
  ```

- Merging Dictionaries (update)

  ```py
  dict1 = {"a": 1, "b": 2}
  dict2 = {"b": 3, "c": 4}
  dict1.update(dict2)
  print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
  ```

- Get with Default

  ```py
  print(my_dict.get("country", "Not Found"))  # Not Found
  ```

- Keys, Values, Items

  ```py
  print(my_dict.keys())    # dict_keys(['name', 'age'])
  print(my_dict.values())  # dict_values(['TT', 25])
  print(my_dict.items())   # dict_items([('name', 'TT'), ('age', 25)])
  ```

[⬆️ Go to Context](#context)

### Dictionary Methods

- `clear()` – Remove all items

  ```py
  my_dict = {"name": "TT", "age": 25}
  my_dict.clear()
  print(my_dict)  # {}
  ```

- `copy()` – Return a shallow copy

  ```py
  my_dict = {"name": "TT", "age": 25}
  new_dict = my_dict.copy()
  print(new_dict)  # {'name': 'TT', 'age': 25}
  ```

- `fromkeys()` – Create dictionary with keys and default value

  ```py
  keys = ["a", "b", "c"]
  new_dict = dict.fromkeys(keys, 0)
  print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}
  ```

- `get()` – Return value of key (default if key not found)

  ```py
  my_dict = {"name": "TT"}
  print(my_dict.get("name"))       # TT
  print(my_dict.get("age", 0))     # 0
  ```

- `items()` – Return key-value pairs

  ```py
  my_dict = {"name": "TT", "age": 25}
  print(my_dict.items())  # dict_items([('name', 'TT'), ('age', 25)])
  ```

- `keys()` – Return keys

  ```py
  print(my_dict.keys())  # dict_keys(['name', 'age'])
  ```

- `values()` – Return values

  ```py
  print(my_dict.values())  # dict_values(['TT', 25])
  ```

- `pop()` – Remove item by key

  ```py
  my_dict.pop("age")
  print(my_dict)  # {'name': 'TT'}
  ```

- `popitem()` – Remove last inserted item

  ```py
  my_dict.popitem()
  print(my_dict)  # {}
  ```

- `setdefault()` – Return value if key exists, else set default

  ```py
  my_dict = {"name": "TT"}
  print(my_dict.setdefault("age", 20))  # 20
  print(my_dict)  # {'name': 'TT', 'age': 20}
  ```

- `update()` – Update dictionary with key-value pairs

  ```py
  my_dict.update({"name": "John", "country": "BD"})
  print(my_dict)  # {'name': 'John', 'age': 20, 'country': 'BD'}
  ```

[⬆️ Go to Context](#context)

### Dictionary Functions

- `len()` – Number of items

  ```py
  my_dict = {"name": "TT", "age": 25}
  print(len(my_dict))  # 2
  ```

- `type()` – Type of the object

  ```py
  print(type(my_dict))  # <class 'dict'>
  ```

- `all()` – True if all keys are truthy

  ```py
  my_dict = {"a": 1, "b": 2}
  print(all(my_dict))  # True
  ```

- `any()` – True if any key is truthy

  ```py
  my_dict = {"a": 0, "b": 2}
  print(any(my_dict))  # True
  ```

- `sorted()` – Return sorted list of keys

  ```py
  my_dict = {"c": 3, "a": 1, "b": 2}
  print(sorted(my_dict))  # ['a', 'b', 'c']
  ```

- `sum()` – Sum of keys if numeric

  ```py
  my_dict = {1: "a", 2: "b", 3: "c"}
  print(sum(my_dict))  # 6
  ```

- `max()` – Maximum key

  ```py
  print(max(my_dict))  # 3
  ```

- `min()` – Minimum key

  ```py
  print(min(my_dict))  # 1
  ```

[⬆️ Go to Context](#context)

### Dictionary Unpacking

- Extract keys and values directly into variables.

  ```py
  my_dict = {"name": "TT", "age": 25}
  k, v = list(my_dict.items())[0]
  print(k, v)  # name TT
  ```

- Using `**` to merge dictionaries

  ```py
  dict1 = {"a": 1, "b": 2}
  dict2 = {"c": 3, "d": 4}
  merged = {**dict1, **dict2}
  print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  ```

[⬆️ Go to Context](#context)

### Using `zip()` with Dictionary

- Combine two iterables into key-value pairs.

  ```py
  keys = ["name", "age", "country"]
  values = ["TT", 25, "Bangladesh"]
  my_dict = dict(zip(keys, values))
  print(my_dict)  # {'name': 'TT', 'age': 25, 'country': 'Bangladesh'}
  ```

- Iterating with zip()

  ```py
  for k, v in zip(keys, values):
      print(k, v)
  ```

[⬆️ Go to Context](#context)

### Dictionary Comprehension

- Create dictionaries using a single expression inside `{}`.

  ```py
  squares = {x: x**2 for x in range(5)}
  print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

- With condition

  ```py
  even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
  print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
  ```

- From two lists

  ```py
  keys = ["a", "b", "c"]
  values = [1, 2, 3]
  my_dict = {k: v for k, v in zip(keys, values)}
  print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}
  ```

[⬆️ Go to Context](#context)

### Simple Project Using Dictionary

- Restaurant Management

  ```py
  menu = {
      "Coffee": 2,
      "Pasta": 3,
      "Pizza": 5,
      "Burger": 6,
      "Chicken": 10
  }
  print(
      """
      Welcome to Inception's Restaurant. Please Order Food!

      Coffee: $2
      Pasta: $3
      Pizza: $5
      Burger: $6
      Chicken: $10

      """
  )

  item1 = input("Enter the name of the item you want to order: ")
  total_price = 0
  if item1 in menu:
      total_price += menu[item1]
      print(f"You ordered {item1}. Your total order is ${total_price}")
  else:
      print("Invalid item, Please order something from the Menu")
  another_order = input("Do you want to add another item? (Yes/No): ").lower()
  if another_order == "yes":
      item2 = input("Enter the name of the 2nd item you want to order: ")
      if item2 in menu:
          total_price += menu[item2]
          print(f"You ordered {item2}. Your total order is ${total_price}")
      else:
          print("Invalid item, Please order something from the Menu")
  print(f"Your total amount is ${total_price}. Thank you!")
  ```

[⬆️ Go to Context](#context)
