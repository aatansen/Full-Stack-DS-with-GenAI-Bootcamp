"""
### Task 10 - Shopping Cart Bill Calculator

> 💼 **Real-world use:** Billing systems in e-commerce apps.

- Write a function `calculate_total(cart, prices)` that:
  - takes a shopping cart list
  - takes a dictionary of `item: price`
  - returns the total bill amount

- **Example**
  - **Input (Cart):** `["Milk", "Bread", "Milk", "Cheese", "Bread"]`
  - **Input (Price):** `{"Milk": 3.00, "Bread": 2.50, "Eggs": 4.00, "Cheese": 5.00}`
  - **Output (Total Bill Amount):** `16.00`
"""

import ast

def calculate_total(cart, prices):
    cart_dict={}
    total_bill=0

    # count cart items
    for i in cart:
        if i not in cart_dict:
            cart_dict[i]=1
        else:
            cart_dict[i]+=1

    # calculate cost
    for i in cart_dict.keys():
        if i in prices:
            cart_dict[i]*=prices[i]
        total_bill+=cart_dict[i]
    return total_bill

cart=input("Enter shopping cart list: ")
item_prices=input("Enter dictionary of item & price: ")
cart_list=ast.literal_eval(cart)
item_prices_dict=ast.literal_eval(item_prices)

result = calculate_total(cart_list,item_prices_dict)
print(result)
