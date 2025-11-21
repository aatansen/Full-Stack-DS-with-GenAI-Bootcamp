"""
### Task 01 - Inventory Price Calculator

> 💼 **Real-world use:** Used in e-commerce dashboards for price summaries.

- Write a function `calculate_inventory_summary(prices)` that:
  - receives a list of product prices
  - returns total_cost and average_cost
- **Input**: `[120, 250, 399, 150]`
- **Output**: `(919, 229.75)`
"""

import ast

def calculate_inventory_summary(prices):
    total_cost=0
    average_cost=0
    for i in prices:
        i=float(i)
        total_cost+=i
    average_cost=total_cost/len(prices)
    return (total_cost,average_cost)

all_prices=input("Enter prices: ")
all_prices_list = ast.literal_eval(all_prices)
result=calculate_inventory_summary(all_prices_list)
print(result)