"""
### Task 09 - User Authentication Mock

> 💼 **Real-world use:** Login systems (basic level).

- Write a function `login(username, password)` that:
  - checks if the `username` exists
  - checks if the `password` matches
  - returns "Login Successful" or "Invalid Credentials"

- **Example Setup (Mock Database):** Assume the following credential database is used internally:
  - `CREDENTIALS` = `{"alex_s": "securepwd1", "maria_t": "password101", "john_d": "johndoe123"}`

- **Example 1: Successful Login**
  - Input (Username): "maria_t"
  - Input (Password): "password101"
  - Output: "Login Successful"

- **Example 2: Failed Login (Wrong Password)**
  - Input (Username): "alex_s"
  - Input (Password): "securepwd12"
  - Output: "Invalid Credentials"

- **Example 3: Failed Login (Non-existent User)**
  - Input (Username): "peter_z"
  - Input (Password): "any_password"
  - Output: "Invalid Credentials"
"""

def login(username, password):
    CREDENTIALS = {"alex_s": "securepwd1", "maria_t": "password101", "john_d": "johndoe123"}
    if username in CREDENTIALS.keys():
        if CREDENTIALS[username] == password:
            return "Login Successful"
        else:
            return "Invalid Credentials"
    else:
        return "Invalid Credentials"

username=input("Enter username: ")
password=input("Enter username: ")

result=login(username,password)
print(result)
