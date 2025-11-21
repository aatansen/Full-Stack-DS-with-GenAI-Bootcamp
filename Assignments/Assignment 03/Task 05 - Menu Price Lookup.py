"""
### Task 05 - Menu Price Lookup

> 💼 **Real-world use:** Restaurant ordering apps.

- Write a function `get_price(menu, item)` that:
  - receives a dictionary `menu` and an item name
  - returns the price if it exists
  - otherwise returns `"Item not found"`

- **Example 1: Item Found**
  - **Input (Menu):** `{"Coffee": 3.50, "Tea": 2.75, "Muffin": 4.00, "Sandwich": 8.50}`
  - **Input (Item):** `"Muffin"`
  - **Output:** `4.00`

- **Example 2: Item Not Found**
  - **Input (Menu):** `{"Coffee": 3.50, "Tea": 2.75, "Muffin": 4.00, "Sandwich": 8.50}`
  - **Input (Item):** `"Donut"`
  - **Output:** `"Item not found"`
"""

import ast

def get_price(menu, item):
    if item in menu.keys():
        return menu[item]
    else:
        return "Item not found"

input_menu = input("Enter Input (Menu): ")
input_menu_dict=ast.literal_eval(input_menu)

input_item = input("Enter Input (Item): ")
result=get_price(input_menu_dict,input_item)
print(result)
