# guess a random number
# Author: Sun Haoxiang
# Using read

import random

target = random.randint(10, 20)
while True:
    guess = int(input("guess a number between 10 and 20: "))
    if guess == target:
        print("right！")
        break
    print("wrong,try again！")
