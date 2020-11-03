"""
Jacob Padgett
W08 Team Activity
Bro Brian Wilson
"""

import random
import time

# Clear the terminal
clear = chr(27) + "[2J"

# Game loop
again = "y"
while again.lower() == "y":

    print("\nStarting\tThe\tGuessing\tGame")
    time.sleep(2)
    print(clear)

    number = random.randint(1, 10)

    print(f"The number is {number}, guess it last.\n")

    user_num = int(input("Your guess? "))

    num_of_gusses = 1

    if again.lower() == "y":
        while user_num != number:
            if user_num > number:
                print("Too high\n")
                user_num = int(input("Your guess? "))
                num_of_gusses += 1
            else:
                print("Too low\n")
                user_num = int(input("Your guess? "))
                num_of_gusses += 1

        print("You win\n")
        print(f"It took {num_of_gusses} guess(es).\n")
        time.sleep(2)
        again = input(f"Play again? (y/n)? ")

print(clear)
print("\nSee yaaaaaaaaaa later!")
time.sleep(1.5)
print(clear)
