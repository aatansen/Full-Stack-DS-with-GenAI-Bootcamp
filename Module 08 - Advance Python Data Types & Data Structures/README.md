# **Context**

- [**Context**](#context)
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

# [**Day 08 - Tuples, Sets & Dictionary**](./Day%2008%20-%20Tuples,%20Sets%20&%20Dictionary/)

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
