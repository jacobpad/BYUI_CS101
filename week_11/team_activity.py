"""
Jacob Padgett
W11 Team Activity
Bro Brian Wilson
"""

# Clear the terminal
clear = chr(27) + "[2J"
print(clear, "\n")


lst = []


with open("week_11/hr_system.txt") as f:

    for i in f:
        lst.append(i.strip().split())

    # for i in lst:
    #     print(f"Name: {i[0]}, Title: {i[2]}")

    for i in lst:
        name = i[0]
        id = i[1]
        job_title = i[2]
        salary = int(i[3])

        if job_title == "Engineer":
            bob = 1000 * 24
            salary += bob
        print(f"{name} (ID: {id}), {job_title} - ${salary/24:.02f}")
