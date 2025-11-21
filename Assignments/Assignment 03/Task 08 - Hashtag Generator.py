"""
### Task 08 - Hashtag Generator

> 💼 **Real-world use:** Social media automation tools.

- Write a function `generate_hashtags(sentence)` that:
  - converts every word in the sentence into a hashtag
  - returns a list of hashtags

- **Example**
  - **Input:** `"AI Data Science"`
  - **Output:** `["#ai", "#data", "#science"]`
"""

def generate_hashtags(sentence):
    hash_list=[]
    for i in sentence:
        i=i.lower()
        hash_list.append(f"#{i}")
    return hash_list

sentence = input("Enter a sentence: ").split(" ")

result = generate_hashtags(sentence)
print(result)
