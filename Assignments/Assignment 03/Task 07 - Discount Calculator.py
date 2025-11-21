"""
### Task 07 - Discount Calculator

> 💼 **Real-world use:** Online store discount engine.

- Write a function `apply_discounts(products)` where:
  - `products` is a list of tuples: `(name, price, discount)`
  - returns a list of updated prices after applying the discount

- **Example**
  - **Input (List of Tuples):** `[("Keyboard", 80.00, 20), ("Mouse", 25.00, 10), ("Monitor", 300.00, 5)]`
  - **Output (List of Prices):** `[64.00, 22.50, 285.00]`
"""

import ast

def apply_discounts(products):
    updated_princes=[]
    for i in products:
        item,*prices=i
        price=prices[0]
        discount=prices[1]
        result=f"{price-price*(discount/100):.2f}"
        updated_princes.append(float(result))
    return updated_princes

prod=input("Enter products list tuple: ")
prod_list=ast.literal_eval(prod)

final_result = apply_discounts(prod_list)
print(final_result)
