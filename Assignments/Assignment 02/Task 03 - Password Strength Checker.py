"""
### Task 03 - Password Strength Checker

> 💼 **Real-world use:** Used in user authentication systems.
- Check if a password is strong — must have at least one uppercase, one lowercase, one digit, and one special character.
  - Input: "`Hello@123`"
  - Output: `Strong Password`
"""

user_input=input("Enter Password:")
upper_found=False
lower_found=False
digit_found=False
special_found=False

for i in user_input:
    if 65 <=ord(i)<=90:
        upper_found=True
    elif 97 <=ord(i)<=122:
        lower_found=True
    elif 48 <=ord(i)<=57:
        digit_found=True
    elif (32 <= ord(i) <= 47) or (58 <= ord(i) <= 64) or (91 <= ord(i) <= 96) or (123 <= ord(i) <= 126):
        special_found=True

if all([upper_found,lower_found,digit_found,special_found]):
    print("Strong Password")
else:
    print("Not Strong Password")
