"""
### Task 10 - Word Reversal for Data Encryption

> 💼 **Real-world use:** Simple text obfuscation or playful encoding.
- Reverse each word in a sentence while keeping word order the same.
  - Input: "`AI is fun`"
  - Output: `IA si nuf`
"""

sentence=input("Enter text:")
words=sentence.split(" ")

reverse_words=[]
for i in words:
    reverse_words.append(i[::-1])

new_sentence=" ".join(reverse_words)

print(new_sentence)