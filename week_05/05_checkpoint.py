"""
Jacob Padgett
W05 Prepare: Checkpoint
Bro Brian Wilson
"""


d = "-" * 75

# Ask for two ints
num1 = int(input(f"\n{d}\nFirst integer: "))
num2 = int(input("Second integer: "))

if num1 > num2:
    print("The first number is greater")
else:
    print("The first number is not greater")

if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers not are equal")


if num2 > num1:
    print("The second number is greater")
else:
    print("The second number is not greater")


# Favorite Animal
my_favorite_animal = "tiger"
users_favorite_animal = input(f"\n{d}\nWhat is your favorite animal: ")

if users_favorite_animal.lower() == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
