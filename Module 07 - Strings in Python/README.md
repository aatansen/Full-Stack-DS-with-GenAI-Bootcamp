# **Context**

- [**Context**](#context)
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
