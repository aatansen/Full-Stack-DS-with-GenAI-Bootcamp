"""
- Genera a random number (1-100)
- Take an input from user -> guess the number
- Compare / match the num
- if user guess>generate number -> guess a lower num
- if guess < generate num-> guess a higher num
- if num correct show result
"""

import random

random_num=random.randint(1, 100)
num = int(input("Guess the number: "))
counter =1

while num!=random_num:
    if num>random_num:
        print("Guess a lower num")
    elif num<random_num:
        print("Guess a higher num")
    num = int(input("Guess the number: "))
    counter+=1
else:
    print(f"Total attempt: {counter}")
    print("You guess the correct number")


