"""
### Task 05 - SMS Word Counter

> 💼 **Real-world use:** Used in messaging apps or social media post limit check.
- Count how many characters and words are in a message, and tell if it exceeds 160 characters (SMS limit).
  - Input: "`This is a demo message.`"
  - Output: `Words = 5, Characters = 23, Status = Within Limit`
"""

msg=input("Enter message: ")

char_count=len(msg)
words=msg.split(" ")
words_count=len(words)

if words_count<=160:
    status = "Within Limit"
else:
    status = "Not Within Limit"

print(f"Words = {words_count}, Characters = {char_count}, Status = {status}")