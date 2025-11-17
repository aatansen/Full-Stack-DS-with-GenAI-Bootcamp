"""
### Task 04 - Username Generator

> 💼 **Real-world use:** Automatically create usernames for users.
- Take user's full name and generate a short username.
- Rules: first 3 letters of first name + last 3 letters of last name + random number (use loops only).
  - Input: "`Mamun Malitha`"
  - Output: `mamitha57`
"""

import random

ran_num=random.randint(1,100)
user_input=input("Enter Full Name: ").lower()
username=""

for i in range(0,3,1):
    username+=user_input[i]

for j in range(-3,0,1):
    username+=user_input[j]

final_username=username+str(ran_num)
print(final_username)