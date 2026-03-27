# **Context**

- [**Context**](#context)
- [**Day 04 - Conditional Statements, Pip, Modules \& Loops**](#day-04---conditional-statements-pip-modules--loops)
  - [**Conditional Statements**](#conditional-statements)
  - [**PIP (Pip Installs Packages)**](#pip-pip-installs-packages)
  - [**Modules in Python**](#modules-in-python)
  - [**Loops in Python**](#loops-in-python)

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
