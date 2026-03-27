# **Context**

- [**Context**](#context)
- [**Day 09 - Functions in Python**](#day-09---functions-in-python)
  - [**Functions in Python**](#functions-in-python)
    - [Characteristics of Function](#characteristics-of-function)
    - [Creating a Function](#creating-a-function)
    - [Parameter vs Argument](#parameter-vs-argument)
    - [Types of Arguments](#types-of-arguments)
    - [`*args` vs `**kwargs`](#args-vs-kwargs)
    - [Variable Scope in Functions](#variable-scope-in-functions)
    - [Nested Functions](#nested-functions)
    - [Functions are First-Class Citizens](#functions-are-first-class-citizens)
    - [Benefits of Using a Function](#benefits-of-using-a-function)
    - [Lambda Function](#lambda-function)
    - [Lambda vs Normal Function](#lambda-vs-normal-function)
    - [Higher-Order Functions](#higher-order-functions)
    - [`enumerate()` Function](#enumerate-function)

# [**Day 09 - Functions in Python**](./Day%2009%20-%20Functions%20in%20Python/)

## **Functions in Python**

- A function is a reusable block of code that performs a specific task.
- Created using the `def` keyword.
- Can take inputs (parameters) and return outputs.

[⬆️ Go to Context](#context)

### Characteristics of Function

- Defined using the 'def' keyword.
- Executes only when it is called.
- Can accept inputs (parameters).
- Can return outputs using '`return`'.
- Helps avoid code repetition.
- Improves code readability and organization.
- Can be built-in (print, len) or user-defined.
- Supports default parameter values.
- Supports variable arguments (`*args`,`**kwargs`).
- Has its own local scope separate from global scope.
- May or may not return a value.
- Can be nested (function inside another).
- Can be passed as arguments or stored in variables (first-class functions).

[⬆️ Go to Context](#context)

### Creating a Function

- Defined using the 'def' keyword

  ```py
  def greet():
      print("Hello, TT!")
  greet()
  ```

- Function with Parameters

  ```py
  def add(a, b):
      return a + b

  print(add(5, 3))  # 8
  ```

- Function with Default Parameter

  ```py
  def greet(name="TT"):
      print("Hello,", name)

  greet()         # Hello, TT
  greet("John")   # Hello, John
  ```

- Function with Return Value

    ```py
    def square(n):
        return n * n

    print(square(4))  # 16
    ```

- Keyword Arguments

  ```py
  def info(name, age):
      print(name, age)

  info(age=25, name="TT")
  ```

- Variable-Length Arguments (`*args`)

  ```py
  def total(*nums):
      print(sum(nums))

  total(1, 2, 3, 4)  # 10
  ```

- Variable-Length Keyword Arguments (`**kwargs`)

  ```py
  def show(**data):
      print(data)

  show(name="TT", age=25)
  ```

- Lambda (Anonymous Function)

  ```py
  double = lambda x: x * 2
  print(double(5))  # 10
  ```

- Pass Statement

  ```py
  def todo():
      pass  # empty function
  ```

- Docstring - A string used to describe what a function does, placed at the beginning of the function

  ```py
  def add(a, b):
      """Returns the sum of two numbers."""
      return a + b

  print(add.__doc__)
  ```

- Calling Functions

  ```py
  def hello():
      print("Hi!")

  hello()
  ```

- Deleting Functions

  ```py
  def hello():
      print("Hi!")

  del hello
  ```

[⬆️ Go to Context](#context)

### Parameter vs Argument

- **Parameter** – Variable defined in the function to accept input

  ```py
  def greet(name, age):  # name and age are parameters
      print(f"Hello {name}, you are {age} years old")
  ```

- **Argument** – Actual value passed to the function when calling it

  ```py
  greet("TT", 25)  # "TT" and 25 are arguments
  ```

- **Key Difference** – Parameters exist in function definition, arguments exist in function call

  ```py
  # Parameters: name, age
  # Arguments: "TT", 25
  ```

[⬆️ Go to Context](#context)

### Types of Arguments

- **Positional Arguments** – Passed in order

  ```py
  def greet(name, age):
      print(f"Hello {name}, you are {age} years old")

  greet("TT", 25)  # Hello TT, you are 25 years old
  ```

- **Keyword Arguments** – Passed using parameter names

  ```py
  greet(age=25, name="TT")  # Hello TT, you are 25 years old
  ```

- **Default Arguments** – Use default value if not provided

  ```py
  def greet(name, age=18):
      print(f"Hello {name}, you are {age} years old")

  greet("TT")  # Hello TT, you are 18 years old
  ```

- **Variable-length Arguments (`*args`)** – Accepts any number of positional arguments

  ```py
  def add(*numbers):
      print(sum(numbers))

  add(1, 2, 3, 4)  # 10
  ```

- **Variable-length Keyword Arguments (`**kwargs`)** – Accepts any number of keyword arguments

  ```py
  def info(**details):
      print(details)

  info(name="TT", age=25)  # {'name': 'TT', 'age': 25}
  ```

- **Required Arguments** – Must be provided, no default

  ```py
  def greet(name, age):
      print(f"Hello {name}, you are {age}")

  # greet("TT")  # Error: missing required argument 'age'
  ```

- **Positional-only Arguments (Python 3.8+)** – Must be passed by position

  ```py
  def greet(name, /, age):
      print(f"{name} is {age}")

  greet("TT", age=25)  # TT is 25
  ```

- **Keyword-only Arguments** – Must be passed by keyword

  ```py
  def greet(*, name, age):
      print(f"{name} is {age}")

  greet(name="TT", age=25)  # TT is 25
  ```

[⬆️ Go to Context](#context)

### `*args` vs `**kwargs`

- **`*args`** – Accepts any number of positional arguments as a tuple

  ```py
  def add(*numbers):
      print(numbers)
      print(sum(numbers))

  add(1, 2, 3, 4)
  # Output:
  # (1, 2, 3, 4)
  # 10
  ```

- **`**kwargs`** – Accepts any number of keyword arguments as a dictionary

  ```py
  def info(**details):
      print(details)

  info(name="TT", age=25)
  # Output:
  # {'name': 'TT', 'age': 25}
  ```

- **Key Difference**
  - `*args` → positional arguments, tuple
  - `**kwargs` → keyword arguments, dictionary

[⬆️ Go to Context](#context)

### Variable Scope in Functions

- **Local Scope** – Variables defined inside a function, accessible only within that function

  ```py
  def my_func():
      x = 10  # local variable
      print(x)

  my_func()  # 10
  # print(x)  # Error: x is not defined
  ```

- **Global Scope** – Variables defined outside all functions, accessible anywhere

  ```py
  y = 20  # global variable

  def show():
      print(y)

  show()  # 20
  print(y)  # 20
  ```

- **Using `global` Keyword** – Modify global variables inside a function

  ```py
  count = 0

  def increment():
      global count
      count += 1

  increment()
  print(count)  # 1
  ```

- **Enclosing / Nonlocal Scope** – Variables in outer (enclosing) function, accessible in nested function

  ```py
  def outer():
      a = 5
      def inner():
          nonlocal a
          a += 1
          print(a)
      inner()
      print(a)

  outer()
  # Output:
  # 6
  # 6
  ```

[⬆️ Go to Context](#context)

### Nested Functions

- **Nested Function** – A function defined inside another function

  ```py
  def outer():
      print("This is the outer function")

      def inner():
          print("This is the inner function")

      inner()  # Calling inner function inside outer

  outer()
  # Output:
  # This is the outer function
  # This is the inner function
  ```

- **Accessing Outer Variable** – Inner function can access variables from outer function

  ```py
  def outer():
      x = 10
      def inner():
          print(f"Value from outer: {x}")
      inner()

  outer()
  # Output:
  # Value from outer: 10
  ```

[⬆️ Go to Context](#context)

### Functions are First-Class Citizens

- Functions in Python can be treated like any other object: assigned to variables, passed as arguments, and returned from other functions.

- **Assigning Function to a Variable**

  ```py
  def greet():
      print("Hello TT")

  say_hello = greet  # assigning function to a variable
  say_hello()  # Hello TT
  ```

- **Passing Function as Argument**

  ```py
  def greet():
      print("Hello TT")

  def call_func(func):
      func()

  call_func(greet)  # Hello TT
  ```

- **Returning Function from Another Function**

  ```py
  def outer():
      def inner():
          print("Inside inner function")
      return inner

  my_func = outer()
  my_func()  # Inside inner function
  ```

[⬆️ Go to Context](#context)

### Benefits of Using a Function

- **Code Modularity** – Breaks program into smaller, manageable parts

  ```py
  def calculate_area(radius):
      return 3.14 * radius * radius

  def calculate_circumference(radius):
      return 2 * 3.14 * radius
  ```

- **Code Readability** – Improves clarity and understanding of the program

  ```py
  def greet_user(name):
      print(f"Hello {name}, welcome!")
  ```

- **Code Reusability** – Functions can be reused multiple times without rewriting code

  ```py
  def add(a, b):
      return a + b

  print(add(5, 10))
  print(add(20, 30))
  ```

[⬆️ Go to Context](#context)

### Lambda Function

- A small anonymous function defined using the `lambda` keyword, usually for simple operations

  ```py
  # Syntax: lambda arguments: expression

  square = lambda x: x ** 2
  print(square(5))  # 25
  ```

- **Multiple Arguments**

  ```py
  add = lambda a, b: a + b
  print(add(10, 20))  # 30
  ```

- **Used with `map()`**

  ```py
  nums = [1, 2, 3, 4]
  squared = list(map(lambda x: x**2, nums))
  print(squared)  # [1, 4, 9, 16]
  ```

- **Used with `filter()`**

  ```py
  nums = [1, 2, 3, 4, 5]
  even = list(filter(lambda x: x % 2 == 0, nums))
  print(even)  # [2, 4]
  ```

- **Used with `sorted()`**

  ```py
  points = [(1, 2), (3, 1), (5, 0)]
  sorted_points = sorted(points, key=lambda x: x[1])
  print(sorted_points)  # [(5, 0), (3, 1), (1, 2)]
  ```

[⬆️ Go to Context](#context)

### Lambda vs Normal Function

- **Normal Function** – Defined using `def`, can have multiple statements, name is mandatory

  ```py
  def add(a, b):
      result = a + b
      return result

  print(add(5, 10))  # 15
  ```

- **Lambda Function** – Anonymous function using `lambda`, limited to a single expression

  ```py
  add = lambda a, b: a + b
  print(add(5, 10))  # 15
  ```

- **Key Differences**

  - Normal Function:
    - Defined with 'def'
    - Can contain multiple statements
    - Has a function name
    - Can include loops, conditions, etc.

  - Lambda Function:
    - Defined with 'lambda'
    - Single expression only
    - Anonymous (no name, unless assigned)
    - Mostly used for short, simple operations

[⬆️ Go to Context](#context)

### Higher-Order Functions

- Functions that can take other functions as arguments and/or return functions as results

- **Passing Function as Argument**

  ```py
  def greet():
      print("Hello TT")

  def call_func(func):
      func()  # function passed as argument

  call_func(greet)  # Hello TT
  ```

- **Returning Function from Another Function**

  ```py
  def outer():
      def inner():
          print("Inside inner function")
      return inner  # returning function

  my_func = outer()
  my_func()  # Inside inner function
  ```

- **Built-In Higher Order Functions**

- **`map()`** – Applies a function to all items in an iterable

  ```py
  nums = [1, 2, 3, 4]
  squared = list(map(lambda x: x**2, nums))
  print(squared)  # [1, 4, 9, 16]
  ```

- **`filter()`** – Filters items in an iterable based on a function

  ```py
  nums = [1, 2, 3, 4, 5]
  even = list(filter(lambda x: x % 2 == 0, nums))
  print(even)  # [2, 4]
  ```

- **`reduce()`** – Applies a function cumulatively to items (from `functools`)

  ```py
  from functools import reduce
  nums = [1, 2, 3, 4]
  total = reduce(lambda x, y: x + y, nums)
  print(total)  # 10
  ```

- **`sorted()`** – Can take a key function for custom sorting

  ```py
  points = [(1, 2), (3, 1), (5, 0)]
  sorted_points = sorted(points, key=lambda x: x[1])
  print(sorted_points)  # [(5, 0), (3, 1), (1, 2)]
  ```

- **`any()` and `all()`** – Can be combined with functions in comprehension or `map`

  ```py
  nums = [0, 1, 2, 3]
  print(all(map(lambda x: x > 0, nums)))  # False
  print(any(map(lambda x: x > 0, nums)))  # True
  ```

- **`zip()` with function** – Combine iterables and apply function using `map`

  ```py
  a = [1, 2, 3]
  b = [4, 5, 6]
  sum_list = list(map(lambda x: x[0]+x[1], zip(a, b)))
  print(sum_list)  # [5, 7, 9]
  ```

[⬆️ Go to Context](#context)

### `enumerate()` Function

- Adds a counter to an iterable and returns it as an `enumerate` object, which can be converted to a list or tuple

  ```py
  fruits = ["apple", "banana", "cherry"]
  for index, fruit in enumerate(fruits):
      print(index, fruit)

  # Output:
  # 0 apple
  # 1 banana
  # 2 cherry
  ```

- **Start Index** – You can specify a starting index

  ```py
  fruits = ["apple", "banana", "cherry"]
  for index, fruit in enumerate(fruits, start=1):
      print(index, fruit)

  # Output:
  # 1 apple
  # 2 banana
  # 3 cherry
  ```

- **Usage with List Conversion**

  ```py
  fruits = ["apple", "banana", "cherry"]
  enum_list = list(enumerate(fruits))
  print(enum_list)  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
  ```

[⬆️ Go to Context](#context)
