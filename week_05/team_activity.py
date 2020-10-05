"""
Jacob Padgett
W05 Team Activity
Bro Brian Wilson
"""

# A >= 90

# B >= 80

# C >= 70

# D >= 60

# F < 60

grade = float(input("\nWhat was you percentage: "))

# # A
# if grade >= 93:
#     print("Your letter grade is: A")
# elif grade >= 90:
#     print("Your letter grade is: A-")

# # B
# elif grade >= 87:
#     print("Your letter grade is: B+")
# elif grade >= 83:
#     print("Your letter grade is: B")
# elif grade >= 80:
#     print("Your letter grade is: B-")


# # C
# elif grade >= 77:
#     print("Your letter grade is: C+")
# elif grade >= 73:
#     print("Your letter grade is: C")
# elif grade >= 70:
#     print("Your letter grade is: C-")


# # D
# elif grade >= 67:
#     print("Your letter grade is: D+")
# elif grade >= 63:
#     print("Your letter grade is: D")
# elif grade >= 60:
#     print("Your letter grade is: D-")

# # F
# else:
#     print("Your letter grade is: F")


def tell_letter_grade(x):
    x = float(x)
    grade = ""
    plus_minus = ""
    second_digit = x % 10

    if second_digit >= 7:
        plus_minus = "+"
    elif second_digit < 3:
        plus_minus = "-"

    if x >= 90:
        grade = "A"
    elif x >= 80:
        grade = "B"
    elif x >= 70:
        grade = "C"
    elif x >= 60:
        grade = "D"
    elif x < 60:
        grade = "F"

    if x >= 93 or x < 60:
        plus_minus = ""

    print(f"Your letter grade is {grade}{plus_minus}")

    if x >= 70:
        print("You passed")
    else:
        print("Better luck next time, pal.")


tell_letter_grade(grade)
