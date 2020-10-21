"""
Jacob Padgett
W06 Team Activity
Bro Brian Wilson
"""

"""The basic rules are as follows:

No one under 36 inches may ever ride, either by themselves or with another rider.

Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

If there are two riders and one of them is at least 18 years old, they may ride together.
"""


"""CORE REQUIREMENTS
Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.

Handle the case of a single rider.

Finish implementing the basic rules.
"""


"""STRETCH CHALLENGE
In addition to the basic rules, the amusement park has added the following. Please implement each one for the stretch challenges:

If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)
"""


# print()
# print()
# print()
# print()
# print()

# ############################################################################################################

# rider_1_age = int(input("What is the age of the first rider? "))
# rider_1_height = int(input("What is the height of the first rider? "))


# second_rider_bool = input("Is there a second rider (yes/no)? ")
# only_1_rider = True

# if second_rider_bool.upper() == "YES":
#     only_1_rider = False

# ###########################


# if only_1_rider == True:
#     # Basic Rule 1
#     if rider_1_height < 36:
#         print("Sorry, you may not ride...")

#     # Basic Rule 2
#     elif rider_1_age >= 18 and rider_1_height >= 62:
#         print("You may ride 1")

#     else:
#         print("Sorry, you may not ride...")


# # Basic Rule 1
# else:
#     second_rider_age = int(input("What is the age of the second rider? "))
#     second_rider_height = int(input("What is the height of the second rider? "))

#     if rider_1_height < 36 or second_rider_height < 36:
#         print("Sorry, you may not ride...")

#     # Basic Rule 2
#     elif rider_1_age >= 18 and rider_1_height >= 62:
#         print("You may ride")

#     # Basic Rule 3
#     elif (
#         second_rider_bool.upper() == "YES"
#         and rider_1_age >= 18
#         or second_rider_age >= 18
#     ):
#         print("You may ride")

#     else:
#         print("Sorry, you may not ride...")


############################################################################################################


"""
Sample Stretch
"""

"""
File: teach06_sample.py
Author: Brother Burton

Purpose: Amusement park ride requirements.
"""
# Notice the use of a boolean variable, set to False by default
can_ride = False

age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))

is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))

    # Rule 1
    if height1 < 36 or height2 < 36:
        can_ride = False
    else:
        # Rule 3
        if age1 >= 18 or age2 >= 18:
            # At least one is an adult
            can_ride = True
        else:
            # Neither is an adult
            can_ride = False
else:  # There is only one rider
    # Rule 2
    if age1 >= 18 and height1 >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
