"""
### Task 10 - Electricity Bill Calculator

- Input number of units consumed and calculate bill:
  - Up to `100` units → `5` BDT per unit
  - `101-200` units → `7` BDT per unit
  - Above `200` units → `10` BDT per unit
- Print `total payable amount`.
"""

units = int(input("Enter number of units consumed: "))
amount = 0

if units<=100:
    amount=units*5
elif units>=101 and units<=200:
    amount=units*7
else:
    amount=units*10

print(f"Amount to pay: {amount}")
