"""
### Task 01 - Temperature Check

- Write a program that takes the current temperature as input and prints:
  - "`It's too cold!`" if below 10°C
  - "`It's cool outside`" if between 10°C and 25°C
  - "`It's hot outside!`" if above 25°C
"""

temperature = int(input("Enter temperature: "))

if temperature<10:
    print("It's too cold!")
elif temperature>=10 and temperature<=25:
    print("It's cool outside")
elif temperature>25:
    print("It's hot outside!")