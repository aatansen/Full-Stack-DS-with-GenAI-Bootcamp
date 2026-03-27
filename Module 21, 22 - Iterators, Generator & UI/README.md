# **Context**

- [**Context**](#context)
- [**Day 21 - Decorator, Iterators \& Generator**](#day-21---decorator-iterators--generator)
  - [**Namespaces**](#namespaces)
    - [Types of Namespaces in Python](#types-of-namespaces-in-python)
      - [1. Built-in Namespace](#1-built-in-namespace)
      - [2. Global Namespace](#2-global-namespace)
      - [3. Local Namespace](#3-local-namespace)
    - [Namespace Lifetime](#namespace-lifetime)
    - [LEGB Rule (Name Resolution Order)](#legb-rule-name-resolution-order)
    - [Global Keyword](#global-keyword)
    - [Nonlocal Keyword](#nonlocal-keyword)
    - [Checking Namespaces](#checking-namespaces)
    - [Namespace vs Scope](#namespace-vs-scope)
  - [**Decorator**](#decorator)
  - [**Iterators**](#iterators)
  - [**Generators**](#generators)
    - [Generator vs Normal Function](#generator-vs-normal-function)
    - [`yield` Keyword Explained](#yield-keyword-explained)
    - [Generator is an Iterator](#generator-is-an-iterator)
    - [Generator Expression](#generator-expression)
    - [`yield` vs `return`](#yield-vs-return)
    - [Where To Use Generators](#where-to-use-generators)
- [**Day 22 - User Interface (UI) Creation**](#day-22---user-interface-ui-creation)
  - [**Design simple UI**](#design-simple-ui)

# [**Day 21 - Decorator, Iterators & Generator**](./Day%2021%20-%20Namespaces,%20Decorator,%20Iterators%20&%20Generator/)

## **Namespaces**

- A **mapping of names to objects**
- Prevents naming conflicts
- Determines **where** a name is accessible

  ```py
  x = 10
  ```

Here, `x` exists in a namespace.

[⬆️ Go to Context](#context)

### Types of Namespaces in Python

#### 1. Built-in Namespace

- Contains built-in functions and keywords
- Available everywhere

Examples:

```py
print()
len()
int()
```

[⬆️ Go to Context](#context)

#### 2. Global Namespace

- Created when a module is loaded
- Names defined at the top level of a file

  ```py
  x = 100   # global namespace

  def show():
      pass
  ```

[⬆️ Go to Context](#context)

#### 3. Local Namespace

- Created when a function is called
- Exists only inside that function

  ```py
  def demo():
      y = 50   # local namespace
      print(y)
  ```

[⬆️ Go to Context](#context)

### Namespace Lifetime

- Built-in → Exists until interpreter exits
- Global   → Exists until module execution ends
- Local    → Exists during function call

[⬆️ Go to Context](#context)

### LEGB Rule (Name Resolution Order)

- L → Local
- E → Enclosing (nested functions)
- G → Global
- B → Built-in

  ```py
  x = "global"

  def outer():
      x = "enclosing"
      def inner():
          x = "local"
          print(x)
      inner()

  outer()
  ```

- **Output**

  ```txt
  local
  ```

[⬆️ Go to Context](#context)

### Global Keyword

  ```py
  x = 10

  def change():
      global x
      x = 20

  change()
  print(x)
  ```

[⬆️ Go to Context](#context)

### Nonlocal Keyword

  ```py
  def outer():
      x = 5
      def inner():
          nonlocal x
          x = 10
      inner()
      print(x)

  outer()
  ```

[⬆️ Go to Context](#context)

### Checking Namespaces

  ```py
  print(globals())
  print(locals())
  ```

[⬆️ Go to Context](#context)

### Namespace vs Scope

- Namespace → Where names are stored
- Scope     → Where names are accessible

[⬆️ Go to Context](#context)

## **Decorator**

- A **function that modifies another function**
- Uses the `@decorator_name` syntax
- Works because **functions are first-class objects**
- Commonly used for logging, authentication, timing, caching
- Code reusability
- Cleaner function logic
- Separation of concerns
- Easy to apply/remove behavior

- Basic Decorator Example

  ```py
  def my_decorator(func):
      def wrapper():
          print("Before function call")
          func()
          print("After function call")
      return wrapper

  @my_decorator
  def say_hello():
      print("Hello!")

  say_hello()
  ```

- **Output**

  ```txt
  Before function call
  Hello!
  After function call
  ```

- Decorator Without `@` Syntax

  ```py
  def say_hi():
      print("Hi")

  say_hi = my_decorator(say_hi)
  say_hi()
  ```

- Decorator with Arguments

  ```py
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print("Before function")
          return func(*args, **kwargs)
      return wrapper

  @my_decorator
  def add(a, b):
      return a + b

  print(add(2, 3))
  ```

- Using `functools.wraps` (Best Practice)

  ```py
  from functools import wraps

  def my_decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          return func(*args, **kwargs)
      return wrapper
  ```

- Preserves function name and docstring
- Important for debugging and documentation

- Authentication using Decorator

  ```py
  def login_required(func):
      def wrapper(user):
          if not user:
              print("Login required")
              return
          return func(user)
      return wrapper

  @login_required
  def dashboard(user):
      print("Welcome to dashboard")

  dashboard(None)
  dashboard("Admin")
  ```

- Decorators with Parameters

  ```py
  def repeat(n):
      def decorator(func):
          def wrapper(*args, **kwargs):
              for _ in range(n):
                  func(*args, **kwargs)
          return wrapper
      return decorator

  @repeat(3)
  def greet():
      print("Hello")

  greet()
  ```

- Class-Based Decorator

  ```py
  class MyDecorator:
      def __init__(self, func):
          self.func = func

      def __call__(self):
          print("Before call")
          self.func()
          print("After call")

  @MyDecorator
  def hello():
      print("Hello")

  hello()
  ```

- Common Built-in Decorators

  ```py
  @staticmethod
  @classmethod
  @property
  ```

- Example

  ```py
  class Demo:
      @staticmethod
      def show():
          print("Static method")
  ```

[⬆️ Go to Context](#context)

## **Iterators**

- **Iteration**: Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

  ```py
  num = [1,2,3]

  for i in num:
    print(i)
  ```

- **Iterator**: An Iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory. It produce values one at a time during iteration and remember their current state.

  ```py
  nums = [1, 2, 3]
  it = iter(nums)

  print(next(it))
  print(next(it))
  print(next(it))
  ```

- **Iterables**: Iterables are objects that can be looped over and provide an iterator when passed to the iter() function.
  - `list`
  - `tuple`
  - `set`
  - `string`
  - `dictionary`
  - `range`

- Iterable vs Iterator
  - Iterable
    - Can be iterated over
    - Returns a new iterator
    - Has `__iter__()`
    - Example: `list`, `tuple`, `string`
  - Iterator
    - Produces values
    - Remembers state
    - Has `__iter__()` and `__next__()`
    - Example: `iter(list)`

> [!NOTE]
>
> - Iterable → Object you can loop over (list, tuple, set, string)
> - Iterator → Object that produces values using `__next__()`

[⬆️ Go to Context](#context)

## **Generators**

- A **generator** is a function that:
  - Returns an iterator
  - Uses `yield` instead of `return`
  - It **pauses execution**, remembers state, and resumes later
- Generators are a way to create **iterators** easily
- It allow us to **produce values one at a time**, instead of storing everything in memory
- Especially useful for:
  - Large data processing
  - Streams
  - Infinite sequences
  - Performance-critical code

  ```py
  def count_up():
      yield 1
      yield 2
      yield 3
  ```

- Calling the function does **not** run it immediately

  ```py
  g = count_up()
  ```

- Values are produced only when requested

  ```py
  print(next(g))  # 1
  print(next(g))  # 2
  print(next(g))  # 3
  ```

[⬆️ Go to Context](#context)

### Generator vs Normal Function

- Normal Function

  ```py
  def get_numbers():
      return [1, 2, 3]
  ```

- Executes fully
- Returns all values at once
- Uses memory to store everything

- Generator Function

  ```py
  def get_numbers():
      yield 1
      yield 2
      yield 3
  ```

- Executes lazily
- Produces values one by one
- Very memory efficient

[⬆️ Go to Context](#context)

### `yield` Keyword Explained

- `yield`:

  - Sends a value to the caller
  - Pauses the function
  - Saves local variables & execution state

- Execution Flow

  ```py
  def demo():
      print("Start")
      yield 1
      print("Middle")
      yield 2
      print("End")
  ```

- Calling step-by-step

  ```py
  g = demo()
  next(g)  # prints "Start", returns 1
  next(g)  # prints "Middle", returns 2
  next(g)  # prints "End", StopIteration raised
  ```

[⬆️ Go to Context](#context)

### Generator is an Iterator

- Generators:

  - Implement `__iter__()`
  - Implement `__next__()`
- Can be used in loops directly

  ```py
  for value in count_up():
      print(value)
  ```

[⬆️ Go to Context](#context)

### Generator Expression

- Produces values lazily
- Uses far less memory
- Similar to list comprehensions
- Use `()` instead of `[]`

  ```py
  nums = (x * 2 for x in range(5))
  ```

[⬆️ Go to Context](#context)

### `yield` vs `return`

- `return`
  - Ends function execution
- `yield`
  - Pauses function
  - Can be used multiple times

  ```py
  def test():
      yield 1
      return
      yield 2  # never runs
  ```

[⬆️ Go to Context](#context)

### Where To Use Generators

- Data is large
- Don’t need random access
- Avoid generators when need to reuse values multiple times
- Prefer generator expressions for simple transformations
- Always close resources properly

[⬆️ Go to Context](#context)

# [**Day 22 - User Interface (UI) Creation**](./Day%2022%20-%20User%20Interface%20(UI)%20Creation/)

## **Design simple UI**

- Official docs: [Streamlit Fundamentals](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
- Transform CLI interface of [Day 20 - Mega OOP Project](../Module%2020%20-%20Mega%20OOP%20Project/) to [Day 22 - User Interface (UI) Creation](./Day%2022%20-%20User%20Interface%20(UI)%20Creation/) GUI interface
- To save data locally `st.session_state` is used
- Full code can be found in [Day 22 - User Interface (UI) Creation/app.py](./Day%2022%20-%20User%20Interface%20(UI)%20Creation/app.py)

[⬆️ Go to Context](#context)
