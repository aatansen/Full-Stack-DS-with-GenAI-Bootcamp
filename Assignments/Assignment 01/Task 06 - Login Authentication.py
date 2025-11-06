"""
### Task 06 - Login Authentication

- Take a `username` and `password` input.
  - If `username == "admin"` and `password == "12345"` → print "`Login Successful`"
  - Else → print "`Invalid Credentials`"
"""

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Credentials")