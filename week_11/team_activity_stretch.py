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

    for i in lst:
        name = i[0]
        id_n = i[1]
        job_title = i[2]
        salary = int(i[3])
        if job_title == "Engineer":
            salary += 24000
        print(f"{name} (ID: {id_n}), {job_title}, ${int(salary)/24:.02f}")

