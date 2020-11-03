"""
Jacob Padgett
W08 Checkpoint
Bro Brian Wilson
"""

"""
Ask the user for a number, then sum up all the numbers from 0 up to and including their number.
"""

import random
import math

# num = 5
# num = 42
# num = 25000
num = random.randint(1, 100000)

print(f"\nThe number is {num}\n")

sum = 0

for i in range(0, num):
    sum += i

print(f"The sum is {sum + num}\n")
