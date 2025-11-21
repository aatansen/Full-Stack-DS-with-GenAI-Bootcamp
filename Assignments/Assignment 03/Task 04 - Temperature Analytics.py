"""
### Task 04 - Temperature Analytics

> 💼 **Real-world use:** Health tech temperature screening systems.

- Write a function `analyze_temperatures(temp_list)` that:
  - separates high (> 38°C) and normal temps
  - returns two lists: (`high_list`, `normal_list`)

- **Example**
  - **Input**: `[36.5, 38.0, 39.1, 37.2, 40.5, 38.0, 37.9]`
  - **Output**:
    - `High List (>38°C): [39.1, 40.5]`
    - `Normal List (<38°C): [36.5, 38.0, 37.2, 38.0, 37.9]`
    - `Full Output Tuple: ([39.1, 40.5], [36.5, 38.0, 37.2, 38.0, 37.9])`
"""

import ast

def analyze_temperatures(temp_list):
    high_list=[]
    normal_list=[]
    for i in temp_list:
        i=float(i)
        if i > 38:
            high_list.append(i)
        else:
            normal_list.append(i)
    return high_list,normal_list

temp=input("Enter temperatures: ")
temp_list=ast.literal_eval(temp)

result=analyze_temperatures(temp_list)
high_temp,normal_temp=result
print(f"""
High List (>38°C): {high_temp}
Normal List (<38°C): {normal_temp}
Full Output Tuple: {result}
""")
