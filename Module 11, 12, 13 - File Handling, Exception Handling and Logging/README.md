# **Context**

- [**Context**](#context)
- [**Day 11 - File Handling, Exception Handling and Logging**](#day-11---file-handling-exception-handling-and-logging)
  - [**File Handling**](#file-handling)
    - [What is File Handling?](#what-is-file-handling)
    - [File Modes](#file-modes)
    - [File Handling Using `Open` All Modes](#file-handling-using-open-all-modes)
    - [File Handling Using `with` All Modes](#file-handling-using-with-all-modes)
    - [`Open` vs `With` in Python](#open-vs-with-in-python)
    - [Serialization and Deserialization](#serialization-and-deserialization)
    - [Pickling in Python](#pickling-in-python)
    - [JSON Dump vs Pickling](#json-dump-vs-pickling)
    - [File Handling Using `os` Module](#file-handling-using-os-module)
  - [**Exception Handling in Python**](#exception-handling-in-python)
    - [Try and Except](#try-and-except)
    - [Try, Except with Multiple Exceptions](#try-except-with-multiple-exceptions)
    - [Try, Except with Generic Exception](#try-except-with-generic-exception)
    - [Else Block](#else-block)
    - [Finally Block](#finally-block)
    - [Raising Exceptions](#raising-exceptions)
    - [Custom Exception](#custom-exception)
    - [Try-Except-Else-Finally Complete Structure](#try-except-else-finally-complete-structure)
  - [**Logging in Python**](#logging-in-python)
    - [Import Logging Module](#import-logging-module)
    - [Basic Configuration (Console Logging)](#basic-configuration-console-logging)
    - [Logging to a File](#logging-to-a-file)
    - [Logging Levels](#logging-levels)
    - [Custom Logger](#custom-logger)
    - [Advanced Format](#advanced-format)
    - [Exception Logging](#exception-logging)
- [**Day 11.1 - Python Standard Library**](#day-111---python-standard-library)
  - [**Common Built-in Modules**](#common-built-in-modules)
    - [File \& OS Operations](#file--os-operations)
    - [Data Handling](#data-handling)
    - [Math \& Statistics](#math--statistics)
    - [Date \& Time](#date--time)
    - [Command Line \& System](#command-line--system)
    - [Collections \& Data Structures](#collections--data-structures)
    - [Concurrency \& Performance](#concurrency--performance)
    - [Networking \& Internet](#networking--internet)
    - [Debugging \& Development](#debugging--development)
    - [Testing](#testing)
  - [**Advanced Modules**](#advanced-modules)
    - [Functional Programming Utilities](#functional-programming-utilities)
    - [Modern Data Structures](#modern-data-structures)
    - [Type Hints \& Static Analysis](#type-hints--static-analysis)
    - [Context \& Resource Management](#context--resource-management)
    - [Introspection \& Debugging](#introspection--debugging)
    - [Performance \& Profiling](#performance--profiling)
    - [Async Programming](#async-programming)
    - [Temporary Files \& System Utilities](#temporary-files--system-utilities)
    - [Compression \& Archiving](#compression--archiving)
    - [Hashing \& Security](#hashing--security)
    - [Memory \& Object Utilities](#memory--object-utilities)
    - [Configuration \& Parsing](#configuration--parsing)
    - [Text Processing](#text-processing)
    - [Unique Identifiers](#unique-identifiers)
    - [OOP Utilities](#oop-utilities)
    - [Concurrency Utilities](#concurrency-utilities)
  - [**Python Standard Library Map**](#python-standard-library-map)
    - [Data Science](#data-science)
    - [Web Development (e.g., Django, FastAPI)](#web-development-eg-django-fastapi)
    - [Automation \& Scripting](#automation--scripting)
    - [CLI Tools](#cli-tools)
    - [System Programming](#system-programming)

# [**Day 11 - File Handling, Exception Handling and Logging**](./Day%2011%20-%20File%20Handling,%20Exception%20Handling%20and%20Logging/)

## **File Handling**

### What is File Handling?

- A way to read from and write to files using Python’s built-in functions.
- To store data permanently.
- To read/write logs, configs, reports, user data, etc.

---

- Types of data used for I/O:
  - Text - '12345' as a sequence of unicode chars
  - Binary - 12345 as a sequence of bytes of its binary equivalent

- Hence there are 2 file types to deal with
  - Text files - All program files are text files
  - Binary Files - Images,music,video,exe files

- How File I/O is done in most programming languages
  - Open a file
  - Read/Write data
  - Close the file

[⬆️ Go to Context](#context)

### File Modes

- '`r`'  → read (default)
- '`w`'  → write (overwrites file)
- '`a`'  → append (adds to file)
- '`x`'  → create error if file exists
- '`b`'  → binary mode (images, videos)
- '`t`'  → text mode (default)
- Combinations: '`rb`', '`wb`', '`ab`', etc.

[⬆️ Go to Context](#context)

### File Handling Using `Open` All Modes

- '`r`'  → Read mode (default)
  - Opens file for reading.
  - Raises error if file does not exist.

    ```py
    f = open("data.txt", "r")
    content = f.read()
    f.close()
    ```

- '`w`'  → Write mode
  - Creates file if missing.
  - Overwrites file if exists.

    ```py
      f = open("data.txt", "w")
      f.write("Hello World")
      f.close()
      ```

- '`a`'  → Append mode
  - Creates file if missing.
  - Adds new data at the end (does not overwrite).

    ```py
    f = open("data.txt", "a")
    f.write("\nNew Line Added")
    f.close()
    ```

- '`x`'  → Exclusive creation mode
  - Creates new file.
  - Error if file already exists.

    ```py
    f = open("newfile.txt", "x")
    f.write("Created using x mode")
    f.close()
    ```

- '`b`'  → Binary mode
  - Used for images, videos, audio, PDFs.
  - Must combine with r/w/a.

    ```py
    f = open("image.jpg", "rb")
    data = f.read()
    f.close()
    ```

- '`t`'  → Text mode (default)
  - Handles normal text files.

    ```py
    f = open("notes.txt", "rt")
    print(f.read())
    f.close()
    ```

- '`rb`'  → Read Binary

  ```py
  f = open("file.bin", "rb")
  data = f.read()
  f.close()
  ```

- '`wb`'  → Write Binary

  ```py
  f = open("file.bin", "wb")
  f.write(b"Binary Data")
  f.close()
  ```

- '`ab`'  → Append Binary

  ```py
  f = open("file.bin", "ab")
  f.write(b"\nMore Binary Data")
  f.close()
  ```

- '`rt`'  → Read Text (same as 'r')

  ```py
  f = open("info.txt", "rt")
  ```

- '`wt`'  → Write Text (same as 'w')

  ```py
  f = open("info.txt", "wt")
  ```

- '`at`'  → Append Text (same as 'a')

  ```py
  f = open("info.txt", "at")
  ```

[⬆️ Go to Context](#context)

### File Handling Using `with` All Modes

- '`r`' → Read mode (default)
  - Opens file for reading.
  - Automatically closes file after block ends.

    ```py
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
    ```

- '`w`' → Write mode
  - Creates file if missing.
  - Overwrites file if it exists.

    ```py
    with open("data.txt", "w") as f:
        f.write("Hello World")
    ```

- '`a`' → Append mode
  - Creates file if missing.
  - Adds new data at the end.

    ```py
    with open("data.txt", "a") as f:
        f.write("\nNew Line Added")
    ```

- '`x`' → Exclusive creation mode
  - Creates new file.
  - Error if file already exists.

    ```py
    with open("newfile.txt", "x") as f:
        f.write("Created using x mode")
    ```

- '`b`' → Binary mode
  - Used for images, PDFs, videos.
  - Must combine with r/w/a.

    ```py
    with open("image.jpg", "rb") as f:
        data = f.read()
    ```

- '`t`' → Text mode (default)
  - For normal text files.

    ```py
    with open("notes.txt", "rt") as f:
        print(f.read())
    ```

- '`rb`' → Read Binary

    ```py
    with open("file.bin", "rb") as f:
        data = f.read()
    ```

- '`wb`' → Write Binary

    ```py
    with open("file.bin", "wb") as f:
        f.write(b"Binary Data")
    ```

- '`ab`' → Append Binary

    ```py
    with open("file.bin", "ab") as f:
        f.write(b"\nMore Binary Data")
    ```

- '`rt`' → Read Text (same as 'r')

    ```py
    with open("info.txt", "rt") as f:
        print(f.read())
    ```

- '`wt`' → Write Text (same as 'w')

    ```py
    with open("info.txt", "wt") as f:
        f.write("Hello!")
    ```

- '`at`' → Append Text (same as 'a')

    ```py
    with open("info.txt", "at") as f:
        f.write("\nAppended text")
    ```

[⬆️ Go to Context](#context)

### `Open` vs `With` in Python

- **Using `open()`**
  - Must manually close the file using `close()`.
  - If an error occurs, file may remain open (resource leak).
  - More lines of code and less safe.

    ```py
    f = open("data.txt", "r")
    content = f.read()
    f.close()
    ```

- **Using `with`**
  - Automatically closes the file after block ends.
  - Prevents resource leaks even if errors occur.
  - Cleaner, safer, and recommended.

    ```py
    with open("data.txt", "r") as f:
        content = f.read()
    ```

[⬆️ Go to Context](#context)

### Serialization and Deserialization

- **Serialization**
  - Process of converting Python data types into JSON format.
  - Useful for storing or transmitting data.

    ```py
    import json

    data = {"name": "TT", "age": 25, "city": "Dhaka"}
    json_str = json.dumps(data)  # Python dict → JSON string
    print(json_str)  # '{"name": "TT", "age": 25, "city": "Dhaka"}'
    ```

- **Deserialization**
  - Process of converting JSON data back into Python data types.

    ```py
    import json

    json_str = '{"name": "TT", "age": 25, "city": "Dhaka"}'
    data = json.loads(json_str)  # JSON string → Python dict
    print(data)  # {'name': 'TT', 'age': 25, 'city': 'Dhaka'}
    ```

[⬆️ Go to Context](#context)

### Pickling in Python

- **Pickling**
  - Process of converting Python objects into a byte stream.
  - Can also pickle functions for later use (if defined at top level).

    ```py
    import pickle

    def display_info():
        return "Hi my name is Tansen and I am a Programmer"

    with open("func.pkl", "wb") as f:
        pickle.dump(display_info, f)
    ```

- **Unpickling**
  - Process of converting byte stream back into Python objects.
  - Can call the unpickled function like normal.

    ```py
    import pickle

    with open("func.pkl", "rb") as f:
        func = pickle.load(f)

    print(func())  # Hi my name is Tansen and I am a Programmer
    ```

[⬆️ Go to Context](#context)

### JSON Dump vs Pickling

- **JSON Dump**
  - Converts Python objects to JSON string format.
  - Text-based, human-readable.
  - Can be shared across different programming languages.
  - Supports basic Python types (dict, list, str, int, float, bool, None).
  - Cannot serialize custom Python objects or functions directly.

    ```py
    import json

    def display_info():
        return "Hi my name is Tansen and I am a Programmer"

    data = {"name": "Tansen", "age": 25, "info": "Programmer"}
    json_str = json.dumps(data)  # Serialize Python dict
    print(json_str)  # '{"name": "Tansen", "age": 25, "info": "Programmer"}'
    ```

- **Pickling**
  - Converts Python objects to byte stream.
  - Binary format, not human-readable.
  - Python-specific, cannot be directly used in other languages.
  - Can serialize almost any Python object including custom classes and functions.

    ```py
    import pickle

    def display_info():
        return "Hi my name is Tansen and I am a Programmer"

    with open("func.pkl", "wb") as f:
        pickle.dump(display_info, f)  # Serialize function

    with open("func.pkl", "rb") as f:
        func = pickle.load(f)

    print(func())  # Hi my name is Tansen and I am a Programmer
    ```

[⬆️ Go to Context](#context)

### File Handling Using `os` Module

- Importing OS Module

  ```py
  import os
  ```

- Check if File or Directory Exists

  ```py
  os.path.exists("data.txt")        # True if file or folder exists
  os.path.isfile("data.txt")        # True if it is a file
  os.path.isdir("my_folder")        # True if it is a directory
  ```

- Create a Directory

  ```py
  os.mkdir("my_folder")             # Single directory
  os.makedirs("parent/child")       # Nested directories
  ```

- Remove/Delete a Directory

  ```py
  os.rmdir("my_folder")             # Only empty directories
  os.removedirs("parent/child")     # Nested empty directories
  ```

- Remove/Delete a File

  ```py
  os.remove("data.txt")
  ```

- Rename a File or Directory

  ```py
  os.rename("old_name.txt", "new_name.txt")
  ```

- List Files and Directories

  ```py
  os.listdir(".")                    # List current directory
  os.listdir("/path/to/folder")      # List specific folder
  ```

- Get Current Working Directory

  ```py
  cwd = os.getcwd()
  print(cwd)
  ```

- Change Directory

  ```py
  os.chdir("my_folder")
  print(os.getcwd())
  ```

- Join Paths

  ```py
  full_path = os.path.join("folder", "file.txt")
  print(full_path)                   # folder/file.txt (or folder\file.txt in Windows)
  ```

- Get Absolute Path

  ```py
  abs_path = os.path.abspath("data.txt")
  print(abs_path)
  ```

- Split Path

  ```py
  folder, file = os.path.split("/path/to/data.txt")
  print(folder, file)
  ```

- Get File Name and Extension

  ```py
  name, ext = os.path.splitext("data.txt")
  print(name, ext)                   # data .txt
  ```

- Check Access Permissions

  ```py
  os.access("data.txt", os.R_OK)    # True if readable
  os.access("data.txt", os.W_OK)    # True if writable
  os.access("data.txt", os.X_OK)    # True if executable
  ```

- File Size

  ```py
  size = os.path.getsize("data.txt")
  print(size)
  ```

- Modification and Creation Time

  ```py
  import time
  mod_time = os.path.getmtime("data.txt")
  print(time.ctime(mod_time))
  ```

[⬆️ Go to Context](#context)

## **Exception Handling in Python**

- Mechanism to handle runtime errors.
- Prevents program from crashing.

[⬆️ Go to Context](#context)

### Try and Except

  ```py
  try:
      x = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero")
  ```

[⬆️ Go to Context](#context)

### Try, Except with Multiple Exceptions

  ```py
  try:
      num = int("abc")
      x = 10 / 0
  except ValueError:
      print("Invalid value")
  except ZeroDivisionError:
      print("Cannot divide by zero")
  ```

[⬆️ Go to Context](#context)

### Try, Except with Generic Exception

  ```py
  try:
      x = 10 / 0
  except Exception as e:
      print("Error:", e)
  ```

[⬆️ Go to Context](#context)

### Else Block

- Executes if no exception occurs.

  ```py
  try:
      x = 10 / 2
  except ZeroDivisionError:
      print("Error")
  else:
      print("No error, result is", x)
  ```

[⬆️ Go to Context](#context)

### Finally Block

- Executes regardless of exception.

  ```py
  try:
      x = 10 / 0
  except ZeroDivisionError:
      print("Error")
  finally:
      print("Always runs")
  ```

[⬆️ Go to Context](#context)

### Raising Exceptions

- Manually trigger an exception.

  ```py
  age = -5
  if age < 0:
      raise ValueError("Age cannot be negative")
  ```

[⬆️ Go to Context](#context)

### Custom Exception

  ```py
  class CustomError(Exception):
      pass

  raise CustomError("This is a custom exception")
  ```

[⬆️ Go to Context](#context)

### Try-Except-Else-Finally Complete Structure

  ```py
  try:
      x = int(input("Enter a number: "))
      result = 10 / x
  except ValueError:
      print("Invalid input")
  except ZeroDivisionError:
      print("Cannot divide by zero")
  else:
      print("Result is", result)
  finally:
      print("End of program")
  ```

[⬆️ Go to Context](#context)

## **Logging in Python**

- Logging records events, errors, and messages during program execution.
- Useful for debugging and monitoring applications.

[⬆️ Go to Context](#context)

### Import Logging Module

  ```py
  import logging
  ```

[⬆️ Go to Context](#context)

### Basic Configuration (Console Logging)

  ```py
  logging.basicConfig(level=logging.DEBUG)
  logging.debug("This is a debug message")
  logging.info("Informational message")
  logging.warning("Warning message")
  logging.error("Error occurred")
  logging.critical("Critical issue")
  ```

[⬆️ Go to Context](#context)

### Logging to a File

  ```py
  log_path = "app.log"
  logging.basicConfig(
      filename=log_path,
      format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
      level=logging.INFO
  )

  logging.info("This will be written to a file with timestamp and format")
  logging.warning("This is a warning")
  logging.error("This is an error")
  ```

[⬆️ Go to Context](#context)

### Logging Levels

- `DEBUG` → Detailed information, for development.
- `INFO` → General events, program flow.
- `WARNING` → Indicates a potential problem.
- `ERROR` → Serious problem that prevents a function from running.
- `CRITICAL` → Very serious error, may stop program.

[⬆️ Go to Context](#context)

### Custom Logger

  ```py
  logger = logging.getLogger("myLogger")
  logger.setLevel(logging.DEBUG)
  logger.info("Using custom logger")
  ```

[⬆️ Go to Context](#context)

### Advanced Format

  ```py
  logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s', level=logging.INFO)
  logging.info("Custom formatted log")
  ```

[⬆️ Go to Context](#context)

### Exception Logging

  ```py
  try:
      x = 10 / 0
  except ZeroDivisionError:
      logging.exception("Exception occurred")
  ```

[⬆️ Go to Context](#context)

# **Day 11.1 - Python Standard Library**

- The Python Standard Library is a powerful collection of modules that come pre-installed with Python, requiring no external installations via `pip`.

## **Common Built-in Modules**

These are built-in modules commonly used in python

[⬆️ Go to Context](#context)

### File & OS Operations

- `os` : Interacts with the operating system for file/directory management and environment variables.
  - **Use Cases**: File management, automation scripts, system utilities.

    ```py
    import os
    print(os.getcwd())  # Prints current working directory
    os.mkdir("test_folder")  # Creates a new folder (raises error if exists)
    print(os.listdir())  # Lists files and directories in current folder
    ```

- `pathlib`: Object-oriented filesystem paths; more modern and readable than `os.path`.
  - **Use Cases**: File handling, data science pipelines, cross-platform development.

    ```py
    from pathlib import Path
    path = Path("data.txt")
    if path.exists():
        print("File exists")
    print(path.name)  # Prints the file name
    ```

- `shutil`: High-level file operations like copying, moving, and removing trees of directories.
  - **Use Cases**: Backup scripts, file management tools.

    ```py
    import shutil
    shutil.copy("data.txt", "backup.txt")  # Copies a file
    shutil.move("backup.txt", "folder/backup.txt")  # Moves a file (creates folder if needed)
    ```

[⬆️ Go to Context](#context)

### Data Handling

- `json`: Serializes and deserializes JSON data to/from Python objects.
  - **Use Cases**: APIs, configuration files, web development.

    ```py
    import json
    data = {"name": "TT", "age": 20}
    json_string = json.dumps(data, indent=4)  # Converts to JSON string (with indentation for readability)
    print(json_string)
    python_obj = json.loads(json_string)  # Converts back to Python dict
    print(python_obj["name"])
    ```

- `csv`: Reads and writes CSV files with support for dialects.
  - **Use Cases**: Data science, Excel/CSV processing.

    ```py
    import csv
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Prints each row as a list
    ```

- `pickle`: Serializes Python objects to binary files (not secure for untrusted data).
  - **Use Cases**: Saving machine learning models, caching complex objects.

    ```py
    import pickle
    data = {"model": "LinearRegression"}
    with open("model.pkl", "wb") as f:
        pickle.dump(data, f)  # Saves to file
    with open("model.pkl", "rb") as f:
        loaded = pickle.load(f)  # Loads from file
    print(loaded)
    ```

[⬆️ Go to Context](#context)

### Math & Statistics

- `math`: Basic mathematical functions like trigonometry and constants.
  - **Use Cases**: Scientific computing, data calculations.

    ```py
    import math
    print(math.sqrt(16))  # 4.0
    print(math.pi)  # 3.141592653589793
    ```

- `statistics`: Simple statistical operations on numeric data.
  - **Use Cases**: Data analysis, quick stats.

    ```py
    import statistics
    data = [10, 20, 30, 40]
    print(statistics.mean(data))  # 25
    print(statistics.median(data))  # 25
    ```

- `random`: Generates pseudo-random numbers and selections.
  - **Use Cases**: Simulations, games, data sampling.

    ```py
    import random
    print(random.randint(1, 10))  # Random integer between 1 and 10
    print(random.choice(["apple", "banana", "mango"]))  # Random selection
    ```

[⬆️ Go to Context](#context)

### Date & Time

- `datetime`: Manipulates dates, times, and timedeltas.
  - **Use Cases**: Logging, scheduling, time-based calculations.

    ```py
    from datetime import datetime
    now = datetime.now()
    print(now)  # e.g., 2026-03-09 14:20:00.000000
    print(now.year)  # e.g., 2026
    ```

- `time`: Low-level time access and conversions.
  - **Use Cases**: Performance timing, delays.

    ```py
    import time
    print("Start")
    time.sleep(2)  # Pauses for 2 seconds
    print("End after 2 seconds")
    ```

[⬆️ Go to Context](#context)

### Command Line & System

- `sys`: Accesses interpreter variables and functions.
  - **Use Cases**: CLI tools, script arguments.

    ```py
    import sys
    print(sys.version)  # Python version
    print(sys.argv)  # Command-line arguments
    ```

- `argparse`: Parses command-line options and arguments.
  - **Use Cases**: CLI applications, automation tools.

    ```py
    import argparse
    parser = argparse.ArgumentParser(description="Greet user")
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    print("Hello", args.name)
    ```

    - Run: `python script.py --name TT`

[⬆️ Go to Context](#context)

### Collections & Data Structures

- `collections`: Specialized container types like `Counter`, `defaultdict`, `namedtuple`.
  - **Use Cases**: Data processing, frequency counting.

    ```py
    from collections import Counter
    data = ["a", "b", "a", "c", "a"]
    print(Counter(data))  # Counter({'a': 3, 'b': 1, 'c': 1})
    ```

- `itertools`: Functions for creating iterators for efficient looping.
  - **Use Cases**: Data pipelines, combinatorics.

    ```py
    import itertools
    nums = [1, 2, 3]
    for combo in itertools.combinations(nums, 2):
        print(combo)  # (1, 2), (1, 3), (2, 3)
    ```

[⬆️ Go to Context](#context)

### Concurrency & Performance

- `threading`: Manages threads for concurrent execution (I/O-bound).
  - **Use Cases**: Background tasks, I/O operations.

    ```py
    import threading
    def task():
        print("Running task")
    t = threading.Thread(target=task)
    t.start()
    t.join()  # Waits for thread to finish
    ```

- `multiprocessing`: Spawns processes for parallel execution (CPU-bound).
  - **Use Cases**: CPU-intensive tasks, large data processing.

    ```py
    from multiprocessing import Process
    def work():
        print("Process running")
    p = Process(target=work)
    p.start()
    p.join()
    ```

[⬆️ Go to Context](#context)

### Networking & Internet

- `urllib`: Handles URLs for fetching data.
  - **Use Cases**: Simple HTTP requests, file downloads.

    ```py
    import urllib.request
    response = urllib.request.urlopen("https://example.com")
    print(response.status)  # 200
    print(response.read().decode("utf-8"))  # Page content
    ```

[⬆️ Go to Context](#context)

### Debugging & Development

- `logging`: Flexible logging for applications.
  - **Use Cases**: Production apps, debugging.

    ```py
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Application started")
    logging.warning("Something might be wrong")
    ```

[⬆️ Go to Context](#context)

### Testing

- `unittest`: Framework for writing and running tests.
  - **Use Cases**: Unit testing, TDD.

    ```py
    import unittest
    def add(a, b):
        return a + b
    class TestMath(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)
    if __name__ == "__main__":
        unittest.main()
    ```

[⬆️ Go to Context](#context)

## **Advanced Modules**

- These are more specialized modules often used in professional and advanced projects.

### Functional Programming Utilities

- `functools`: Tools for higher-order functions (e.g., `lru_cache` for memoization).
  - **Use Cases**: Caching, functional patterns, optimization.

    ```py
    from functools import lru_cache
    @lru_cache(maxsize=100)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    print(fibonacci(40))  # Fast due to caching
    ```

- `operator`: Function equivalents of operators for functional programming.
  - **Use Cases**: Sorting, performance-sensitive code.

    ```py
    import operator
    data = [("apple", 3), ("banana", 1), ("mango", 2)]
    sorted_data = sorted(data, key=operator.itemgetter(1))
    print(sorted_data)  # [('banana', 1), ('mango', 2), ('apple', 3)]
    ```

[⬆️ Go to Context](#context)

### Modern Data Structures

- `dataclasses`: Auto-generates boilerplate for data classes.
  - **Use Cases**: Data models, clean OOP.

    ```py
    from dataclasses import dataclass
    @dataclass
    class User:
        name: str
        age: int
    u = User("TT", 22)
    print(u)  # User(name='TT', age=22)
    ```

- `enum`: Defines enumerations for named constants.
  - **Use Cases**: Status codes, configurations.

    ```py
    from enum import Enum
    class Status(Enum):
        SUCCESS = 1
        ERROR = 2
    print(Status.SUCCESS)  # Status.SUCCESS
    ```

[⬆️ Go to Context](#context)

### Type Hints & Static Analysis

- `typing`: Supports type annotations for better code quality.
  - **Use Cases**: Large projects, IDE integration.

    ```py
    from typing import List
    def average(nums: List[int]) -> float:
        return sum(nums) / len(nums)
    print(average([1, 2, 3]))  # 2.0
    ```

- `types`: Runtime type utilities.
  - **Use Cases**: Metaprogramming, frameworks.

    ```py
    import types
    def hello():
        print("Hello")
    print(isinstance(hello, types.FunctionType))  # True
    ```

[⬆️ Go to Context](#context)

### Context & Resource Management

- `contextlib`: Simplifies context managers for resource handling.
  - **Use Cases**: File/DB management, cleanup.

    ```py
    from contextlib import contextmanager
    @contextmanager
    def open_file(name):
        f = open(name, "r")
        try:
            yield f
        finally:
            f.close()
    with open_file("data.txt") as f:
        print(f.read())
    ```

[⬆️ Go to Context](#context)

### Introspection & Debugging

- `inspect`: Inspects live objects like functions and classes.
  - **Use Cases**: Debugging, dynamic analysis.

    ```py
    import inspect
    def greet(name):
        return f"Hello {name}"
    print(inspect.getsource(greet))  # Prints the function source code
    ```

- `traceback`: Handles and prints exception stack traces.
  - **Use Cases**: Error logging in production.

    ```py
    import traceback
    try:
        1 / 0
    except Exception:
        traceback.print_exc()  # Prints detailed traceback
    ```

[⬆️ Go to Context](#context)

### Performance & Profiling

- `timeit`: Times small code snippets.
  - **Use Cases**: Benchmarking.

    ```py
    import timeit
    execution_time = timeit.timeit("sum(range(100))", number=1000)
    print(execution_time)  # Time in seconds
    ```

- `cProfile`: Profiles code execution for bottlenecks.
  - **Use Cases**: Optimization.

    ```py
    import cProfile
    def work():
        sum(range(10000))
    cProfile.run("work()")  # Prints profile stats
    ```

[⬆️ Go to Context](#context)

### Async Programming

- `asyncio`: Supports asynchronous I/O and coroutines.
  - **Use Cases**: Web servers, network apps.

    ```py
    import asyncio
    async def main():
        print("Hello")
        await asyncio.sleep(1)
        print("World")
    asyncio.run(main())
    ```

[⬆️ Go to Context](#context)

### Temporary Files & System Utilities

- `tempfile`: Creates temporary files/directories.
  - **Use Cases**: Testing, temp storage.

    ```py
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as f:
        print(f.name)  # Path to temp file
    ```

- `subprocess`: Executes external commands.
  - **Use Cases**: Shell integration, automation.

    ```py
    import subprocess
    result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
    print(result.stdout.strip())  # "Hello"
    ```

[⬆️ Go to Context](#context)

### Compression & Archiving

- `zipfile`: Handles ZIP files.
  - **Use Cases**: Compression, packaging.

    ```py
    import zipfile
    with zipfile.ZipFile("files.zip", "w") as z:
        z.write("data.txt")
    ```

- `tarfile`: Handles TAR archives.
  - **Use Cases**: Backups, archiving.

    ```py
    import tarfile
    with tarfile.open("files.tar", "w") as tar:
        tar.add("data.txt")
    ```

[⬆️ Go to Context](#context)

### Hashing & Security

- `hashlib`: Computes cryptographic hashes.
  - **Use Cases**: Passwords, integrity checks.

    ```py
    import hashlib
    h = hashlib.sha256(b"hello")
    print(h.hexdigest())  # 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
    ```

- `secrets`: Cryptographically secure random numbers.
  - **Use Cases**: Tokens, security.

    ```py
    import secrets
    token = secrets.token_hex(16)
    print(token)  # Secure hex string
    ```

[⬆️ Go to Context](#context)

### Memory & Object Utilities

- `weakref`: Weak references to avoid memory cycles.
  - **Use Cases**: Caching, memory management.

    ```py
    import weakref
    class Data:
        pass
    obj = Data()
    ref = weakref.ref(obj)
    print(ref())  # <Data object>
    ```

[⬆️ Go to Context](#context)

### Configuration & Parsing

- `configparser`: Parses INI-style config files.
  - **Use Cases**: App settings.

    ```py
    import configparser
    config = configparser.ConfigParser()
    config.read("config.ini")
    print(config.sections())  # List of sections
    ```

[⬆️ Go to Context](#context)

### Text Processing

- `re`: Regular expressions for pattern matching.
  - **Use Cases**: Validation, extraction.

    ```py
    import re
    text = "Email: test@example.com"
    match = re.search(r"\S+@\S+", text)
    print(match.group())  # test@example.com
    ```

[⬆️ Go to Context](#context)

### Unique Identifiers

- `uuid`: Generates UUIDs.
  - **Use Cases**: IDs in databases.

    ```py
    import uuid
    print(uuid.uuid4())  # Random UUID
    ```

[⬆️ Go to Context](#context)

### OOP Utilities

- `abc` (Abstract Base Classes): Defines abstract classes and methods.
  - **Use Cases**: Interfaces, enforcing contracts in OOP.

    ```py
    from abc import ABC, abstractmethod
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14 * self.radius ** 2
    print(Circle(5).area())  # 78.5
    ```

[⬆️ Go to Context](#context)

### Concurrency Utilities

- `queue`: Thread-safe FIFO queues.
  - **Use Cases**: Producer-consumer patterns, threading.

    ```py
    import queue
    q = queue.Queue()
    q.put("item")
    print(q.get())  # "item"
    ```

[⬆️ Go to Context](#context)

## **Python Standard Library Map**

### Data Science

- Core: `csv`, `json`, `pickle`, `math`, `statistics`, `random`, `collections`, `itertools`.
- Advanced: `functools` (caching), `dataclasses` (data models), `typing` (type safety), `timeit` (benchmarking), `re` (text processing).

[⬆️ Go to Context](#context)

### Web Development (e.g., Django, FastAPI)

- Core: `json`, `datetime`, `logging`, `urllib`.
- Advanced: `asyncio` (async APIs), `hashlib` (security), `secrets` (tokens), `configparser` (settings), `subprocess` (external tools), `uuid` (session IDs).

[⬆️ Go to Context](#context)

### Automation & Scripting

- Core: `os`, `pathlib`, `shutil`, `sys`, `argparse`, `datetime`, `time`.
- Advanced: `subprocess` (shell commands), `tempfile` (temps), `zipfile/tarfile` (archiving), `re` (parsing), `contextlib` (resource management).

[⬆️ Go to Context](#context)

### CLI Tools

- Core: `sys`, `argparse`, `logging`.
- Advanced: `operator` (sorting), `enum` (flags), `traceback` (error handling), `configparser` (configs), `cProfile` (profiling).

[⬆️ Go to Context](#context)

### System Programming

- Core: `os`, `threading`, `multiprocessing`.
- Advanced: `inspect` (introspection), `weakref` (memory), `abc` (OOP contracts), `queue` (concurrency), `types` (type checks).

[⬆️ Go to Context](#context)
