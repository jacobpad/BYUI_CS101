"""
Jacob Padgett
W02 Team Activity: 
Bro Brian Wilson
"""

First_name = input("What is you first name: ")
Last_name = input("What is you last name: ")
Email_Address = input("What is you email: ")
Phone_Number = input("What is you number: ")
Job_Title = input("What is you job: ")
ID_Number = input("What is you id: ")
Hair_Color = input("What is your hair color: ")
Eye_Color = input("What is your eye color: ")
Month_Started = input("What is the month you started: ")
In_Training = input("Are you in training (Yes/No): ")

d = "----------------------------------------"

print("The ID Card is:")
print(d)
print(f"{Last_name.upper()}, {First_name.capitalize()}")
print(Job_Title.title())
print(ID_Number, "\n")

print(Email_Address.lower())
print(Phone_Number, "\n")

print(f"Hair: {Hair_Color.capitalize()}\t\tEyes: {Eye_Color.capitalize()}")
print(
    f"Month Started: {Month_Started.capitalize()}\tTraining: {In_Training.capitalize()}"
)
print(d)


""" Below is my personal code for the assignment """

# d = "----------------------------------------"

# First_Name = input("What is your first name: ")
# Last_Name = input("What is your last name: ")
# Email_Address = input("What is your email address: ")
# Phone_Number = input("What is your phone number: ")
# Job_Title = input("What is your job title: ")
# ID_Number = input("What is your ID number: ")
# Hair_Color = input("What is your hair color: ")
# Eye_Color = input("What is your eye color: ")
# Month_Started = input("What is the month you started: ")
# In_Training = input("Are you in training (Yes/No): ")


# lst = [
#     First_Name,  # index 0
#     Last_Name,  # index 1
#     Email_Address,  # index 2
#     Phone_Number,  # index 3
#     Job_Title,  # index 4
#     ID_Number,  # index 5
#     Hair_Color,  # index 6
#     Eye_Color,  # index 7
#     Month_Started,  # index 8
#     In_Training,  # index 9
# ]


# badge = f"""
# {d}
# {lst[1].upper()}, {lst[0].capitalize()}
# {lst[4].title()}
# ID: {lst[5]}

# {lst[2].lower()}
# {lst[3]}

# Hair: {lst[6].capitalize()}\tEyes: {lst[7].capitalize()}
# Month: {lst[8].capitalize()}\tTraining: {lst[9].capitalize()}
# {d}
# """

# print(badge)
