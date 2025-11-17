"""
### Task 02 - Count Word Frequency in Customer Reviews

> 💼 **Real-world use:** Analyzing reviews or comments in text analytics.
- Given a review text, count how many times each word appears (ignore case).
  - Input: "`This product is good and this service is excellent`"
  - Output: `{'this': 2, 'product': 1, 'is': 2, 'good': 1, 'and': 1, 'service': 1, 'excellent': 1}`
"""

text = input("Enter text: ").lower()
words=text.split(" ")

clean_words=[]
for i in words:
    if i not in clean_words:
        clean_words.append(i)

for x in clean_words:
    print(f"{x} : {words.count(x)}")