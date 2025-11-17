"""
### Task 09 - Count Hashtags and Mentions (Social Media Analytics)

> 💼 **Real-world use:** Used in analyzing social media posts.
- Count how many hashtags (#) and mentions (@) appear in a post.
  - Input: "`Check out #AIWorkshop and follow @inceptionbd`"
  - Output: `Hashtags = 1, Mentions = 1`
"""

post=input("Enter post text: ")

hash_count=post.count("#")
mention_count=post.count("@")

print(f"Hashtags = {hash_count}, Mentions = {mention_count}")