"""
### Task 06 - Remove Duplicates from Contact List

> 💼 **Real-world use:** Data cleaning in CRM or user databases.
- Given a list of names (comma separated), remove duplicates.
  - Input: "`Rahim, Karim, Rahim, Sultana`"
  - Output: `Rahim, Karim, Sultana`
"""

names=input("Enter list of names(comma separated): ")
name_list=names.split(", ")
non_duplicate=[]

for i in name_list:
    if i not in non_duplicate:
        non_duplicate.append(i)

print(", ".join(non_duplicate))