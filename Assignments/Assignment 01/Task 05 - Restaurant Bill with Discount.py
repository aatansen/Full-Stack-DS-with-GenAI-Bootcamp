"""
### Task 05 - Restaurant Bill with Discount

- Take total bill amount from the user:
  - If the bill is above 1000 → apply `10% discount`
  - Otherwise → `no discount`
- Then print the `final bill amount`.
"""

total_bill = int(input("Enter total bill amount: "))

if total_bill>1000:
    total_bill = (total_bill*10)/100
    print("10% discount applied")
else:
    print("no discount")

print(f"Final bill amount:{total_bill}")