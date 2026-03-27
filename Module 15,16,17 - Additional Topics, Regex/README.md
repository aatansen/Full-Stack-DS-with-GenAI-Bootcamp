# **Context**

- [**Context**](#context)
- [**Day 14 - Additional Topics, Regex**](#day-14---additional-topics-regex)
  - [**Additional Topics**](#additional-topics)
    - [Python Code In Text Files](#python-code-in-text-files)
    - [Command Line Utility](#command-line-utility)
  - [**Regular Expression (Regex)**](#regular-expression-regex)
    - [Email Extract Using Regex](#email-extract-using-regex)
  - [**Organize Files Using Python**](#organize-files-using-python)

# [**Day 14 - Additional Topics, Regex**](./Day%2014%20-%20Additional%20Topics,%20Regex/)

## **Additional Topics**

### Python Code In Text Files

- We can execute a [text file](./Day%2014%20-%20Additional%20Topics,%20Regex/text_file.txt) that contains python code
  - `python text_file.txt`

[⬆️ Go to Context](#context)

### Command Line Utility

- Normal function

  ```py
  def calculator(a, b, operation):
      if operation == 'add':
          return a + b
      elif operation == 'subtract':
          return a - b
      elif operation == 'multiply':
          return a * b
      elif operation == 'divide':
          if b != 0:
              return a / b
          else:
              return "Error: Division by zero."
      else:
          return "Error: Invalid operation."

  result=calculator(3,5,'multiply')
  print(result)
  ```

- Command line utility

  ```py
  import argparse
  import sys

  def calculator(args):
      if args.o == 'add':
          return args.a + args.b
      elif args.o == 'sub':
          return args.a - args.b
      elif args.o == 'mul':
          return args.a * args.b
      elif args.o == 'div':
          if args.b != 0:
              return args.a / args.b
          else:
              return "Error: Division by zero."
      else:
          return "Error: Invalid operation."

  parser = argparse.ArgumentParser()
  parser.add_argument("--a", type=float, default=1.0)
  parser.add_argument("--b", type=float, default=2.0)
  parser.add_argument("--o", type=str, default="add")

  # args = parser.parse_args()
  # sys.stdout.write(str(calculator(args)))

  args = parser.parse_args()
  result = calculator(args)
  print(result)
  ```

[⬆️ Go to Context](#context)

## **Regular Expression (Regex)**

- Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.
  - [Meta characters in regular expressions](https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions)

- **Basic Matching** – Check if a pattern exists in a string

  ```py
  import re

  text = "I love Python"
  result = re.search("Python", text)

  print(bool(result))  # True
  ```

- **Find All Matches** – Get all occurrences of a pattern

  ```py
  import re

  text = "cat bat rat cat"
  matches = re.findall("cat", text)

  print(matches)  # ['cat', 'cat']
  ```

- **Match at Beginning** – Check pattern only at start of string

  ```py
  import re

  text = "Python is powerful"
  result = re.match("Python", text)

  print(bool(result))  # True
  ```

- **Character Classes** – Match digits, words, or whitespace

  ```py
  import re

  text = "Order ID: 4598"
  digits = re.findall(r"\d+", text)

  print(digits)  # ['4598']
  ```

- **Wildcard (.)** – Match any single character

  ```py
  import re

  text = "cat bat rat"
  matches = re.findall(".at", text)

  print(matches)  # ['cat', 'bat', 'rat']
  ```

- **Repetition (*, +, ?)** – Control how many times a pattern repeats

  ```py
  import re

  text = "ha hahaha hahahaha"
  laughs = re.findall(r"ha+", text)

  print(laughs)  # ['ha', 'hahaha', 'hahahaha']
  ```

- **Anchors (^, $)** – Match start or end of string

  ```py
  import re

  text = "hello"
  print(bool(re.search("^he", text)))  # True
  print(bool(re.search("lo$", text)))  # True
  ```

- **Replace Text (sub)** – Replace matching patterns

  ```py
  import re

  text = "My number is 12345"
  masked = re.sub(r"\d", "*", text)

  print(masked)  # My number is *****
  ```

- **Split String** – Split text using regex pattern

  ```py
  import re

  text = "apple,banana;orange"
  parts = re.split(r"[,;]", text)

  print(parts)  # ['apple', 'banana', 'orange']
  ```

- **Common Validation Example (Email)** – Simple email format check

  ```py
  import re

  email = "test@example.com"
  pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

  print(bool(re.match(pattern, email)))  # True
  ```

- **finditer()** – Iterate over all matches with position details

  ```py
  text = '''Cyclone Dumazile was a strong tropical cyclone in
  the South-West Indian Ocean that affected Madagascar
  and Réunion in early March 2018. Dumazile originated
  from a Cyclone low-pressure Dyclone Pyclone area that formed
  near Agaléga on 27 February. It became a tropical
  disturbance on 2 March, and was named the next day
  after attaining tropical storm status.
  '''

  match_iteam = re.finditer(pattern, text)
  for match in match_iteam:
      index = match.span()
      print(text[index[0]: index[1]])
  ```

[⬆️ Go to Context](#context)

### Email Extract Using Regex

  ```py
  text = '''Cyclone Dumazile was a strong tropical cyclone in
  the South-West Indian Ocean that affected Madagascar
  and Réunion in early March 2018. Dumazile originated
  from a Cyclone low-pressure bappy@gmail.com area that formed
  near Agaléga on 27 February. It became a tropical
  disturbance on 2 March, and was named the next day
  after attaining tropical storm status. contact to
  contact77@gmail.com and alex.gray@amazon.co.uk
  '''
  pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
  emails = re.findall(pattern, text)
  print(emails)
  ```

[⬆️ Go to Context](#context)

## **Organize Files Using Python**

  ```py
  import os
  import shutil

  path = input("Enter the path: ")
  files = os.listdir(path)

  for file in files:
      filename, extension = os.path.splitext(file)
      extension = extension[1:]
      if os.path.exists(path+"/"+extension):
          shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
      else:
          os.makedirs(path+"/"+extension)
          shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
  ```

[⬆️ Go to Context](#context)
