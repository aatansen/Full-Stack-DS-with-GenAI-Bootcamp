"""
### Task 03 - Student Grade Calculator

- Input marks (0-100) and print grade based on:
  - 90-100 → `A+`
  - 80-89 → `A`
  - 70-79 → `B`
  - 60-69 → `C`
  - Below 60 → `Fail`
"""

mark = int(input("Input marks (0-100): "))

if mark>=90 and mark<=100:
    print("A+")
elif mark>=80 and mark<=89:
    print("A")
elif mark>=70 and mark<=79:
    print("B")
elif mark>=60 and mark<=69:
    print("C")
elif mark<60:
    print("Fail")
else:
    print("Invalid! Input marks (0-100)")
