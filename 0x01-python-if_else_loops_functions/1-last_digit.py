#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numbers = number % 10
if numbers > 5:
    hi = "and is greater than 5"
elif numbers == 0:
    hi = "and is 0"
else:
    hi = "and is less than 6 and not 0"
print(f"Last digit of {number} is {numbers} " + hi)
