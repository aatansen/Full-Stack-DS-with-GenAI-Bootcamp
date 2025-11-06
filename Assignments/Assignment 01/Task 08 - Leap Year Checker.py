"""
### Task 08 - Leap Year Checker

- Take a year as input and check:
  - If it is divisible by `400` → `Leap Year`
  - Else if divisible by `4` but not by `100` → `Leap Year`
  - Otherwise → `Not a Leap Year`
"""

year = int(input("Enter a year: "))

if year%400==0:
    print("Leap Year")
elif year%4==0 and year%100!=0:
    print("Leap Year")
else:
    print("Not a Leap Year")