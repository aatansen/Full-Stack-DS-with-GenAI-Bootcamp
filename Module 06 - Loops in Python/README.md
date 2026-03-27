# **Context**

- [**Context**](#context)
- [**Day 05 - Loops in Python**](#day-05---loops-in-python)
  - [**Loops Recap**](#loops-recap)
  - [**Loop Control Statements**](#loop-control-statements)
  - [**Code Visualization Tool**](#code-visualization-tool)

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
