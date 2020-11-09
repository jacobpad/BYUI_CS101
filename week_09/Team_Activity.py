"""
Jacob Padgett
W9 Team Activity
Bro Brian Wilson
"""

import math
import numpy as np
import random

# Clear the terminal
clear = chr(27) + "[2J"
print(clear)

user_num = None
# user_num = "Your number?\nEnter 0 to stop...\n"
nums = []

while user_num != 0:
    user_num = int(input("Enter number: "))
    nums.append(user_num)

# Remove the 0 from the end of the list
nums.pop()

print(f"\nThe LIST is: {nums}\n")
print(f"The SUM is: {sum(nums)}\n")
print(f"The AVERAGE is: {np.mean(nums)}\n")
print(f"The MAX number is: {max(nums)}\n")

# Make a list of positive numbers
x = [x for x in sorted(nums) if x > 0]

# Make a list of negative numbers
y = [x for x in sorted(nums) if x < 0]

print(f"The CLOSTEST GREATER THAN ZERO number is: {x[0]}\n")
print(f"The SORTED LIST is: {sorted(nums)}\n")
print(f"The MIN number is: {min(nums)}\n")
print(f"The POSITIVE NUMBERS in the list are {x}\n")
print(f"The NEGATIVE NUMBERS in the list are {y}")
