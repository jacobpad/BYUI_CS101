"""
Jacob Padgett
W12 Check Point
Bro Brian Wilson
"""

d = "-" * 80


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10",
]


age = 1000
n_name = ""
print(d)

for person in people:
    p = person.split()

    n = p[0]
    a = int(p[1])

    if a < age:
        age = a
        n_name = n

print(f"Youngest in the list: {n_name} ••• {age}")

