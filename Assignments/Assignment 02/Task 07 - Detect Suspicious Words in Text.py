"""
### Task 07 - Detect Suspicious Words in Text (Moderation)

> 💼 **Real-world use:** Used in chat moderation or email filtering.
- If any “banned” words like ['spam', 'scam', 'fake'] are found in a text, print “Warning”.
  - Input: "`This is a scam offer`"
  - Output: `Warning: Suspicious content detected`
"""

text=input("Enter text: ").lower()

word_list=text.split(" ")
if "spam" in word_list or "scam" in word_list or "fake" in word_list:
    print("Warning: Suspicious content detected")
else:
    print("No Suspicious content detected")