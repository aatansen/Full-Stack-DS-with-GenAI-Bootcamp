"""
### Task 03 - Product Category Counter

> 💼 **Real-world use:** Inventory/category-based analytics.

- Write a function `count_categories(products)` that:
  - takes a list of product names
  - returns a dictionary counting each product type.

- **Example**
  - **Input**: `["Laptop", "Smartphone", "Monitor", "Laptop", "Smartphone", "Headphones", "Laptop"]`
  - **Output**: `{"Laptop": 3, "Smartphone": 2, "Monitor": 1, "Headphones": 1}`
"""

import ast

def count_categories(products):
    prod_list={}
    for i in products:
        if i not in prod_list:
            prod_list[i]=1
        else:
            prod_list[i]+=1

    return prod_list

products=input("Enter list of product names: ")
product_list=ast.literal_eval(products)

result=count_categories(product_list)
print(result)
