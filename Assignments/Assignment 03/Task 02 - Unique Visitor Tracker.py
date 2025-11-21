"""
### Task 02 - Unique Visitor Tracker

> 💼 **Real-world use:** Website analytics tools calculating daily active users.

- Write a function `count_unique_visitors(visitor_list)` that:
  - takes a list of visitor IDs
  - returns the number of unique visitors

- **Example**
  - **Input**: `[101, 205, 101, 310, 205, 550]`
  - **Output**: `4 (The unique IDs are 101, 205, 310, 550)`
"""

import ast

def count_unique_visitors(visitor_list):
    unique_visitors=set()
    for i in visitor_list:
        i=int(i)
        unique_visitors.add(i)
    return unique_visitors

all_visitor=input("Enter prices: ")
all_visitor_list=ast.literal_eval(all_visitor)

result=sorted(count_unique_visitors(all_visitor_list))
unique_values=(", ".join(map(str, result)))
unique_count=len(result)

print(f"{unique_count} (The unique IDs are {unique_values})")
