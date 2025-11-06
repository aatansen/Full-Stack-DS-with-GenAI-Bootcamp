"""
### Task 04 - Bus Ticket Discount

- Ask the user for `age` and print `ticket price`:
  - Below 5 → `Free`
  - 5-18 → `50% Discount`
  - 60 or above → `30% Discount`
  - Others → `Full Price`
"""

age = int(input("Enter age: "))

if age<5:
    print("Free")
elif age>=5 and age<=18:
    print("50% Discount")
elif age>=60:
    print("30% Discount")
else:
    print("Full Price")