"""
### Task 01 - Email Validator (String Filtering + Loops)

> 💼 **Real-world use:** Used in signup forms or data cleaning tasks.
- Check if a given email is valid — must contain “`@`” and end with “`.com`” or “`.org`”.
  - **Input**: `hello@inceptionbd.com`
  - **Output**: `Valid Email`
"""

user_email=input("Enter email: ").lower()

if user_email.find("@")!=-1 and (user_email[-4:]==".com" or user_email[-4:]==".org"):
    print("Valid Email")
else:
    print("Not Valid Email")