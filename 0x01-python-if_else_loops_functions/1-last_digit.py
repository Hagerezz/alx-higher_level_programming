#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    numbers = number % 10
else:
    numbers = (-number % 10) * -1
if abs(numbers) > 5:
    hi = "and is greater than 5"
elif abs(numbers) == 0:
    hi = "and is 0"
else:
    hi = "and is less than 6 and not 0"
print(f"Last digit of {number} is {numbers} " + hi)
