"""
### Task 09 - Job Eligibility Checker

- Input age and qualification.
- If `age ≥ 18` and qualification is "`graduate`" → print "`Eligible for Job`"
- Else → "`Not Eligible`"
"""

age = int(input("Enter age: "))
qualification = input("Enter qualification: ")

if age>=18 and qualification == "graduate":
    print("Eligible for Job")
else:
    print("Not Eligible")
