"""
Jacob Padgett
W07 Team Activity
Bro Brian Wilson
"""

d = "\n" * 2
dd = "-" * 50
ddd = d + dd
print(ddd)


import math

question = (
    int(input("How many columns and rows do you want in your multiplication table? "))
    + 1
)

max = question * question

digits = int(math.log10(max)) + 1

for i in range(1, question):
    for j in range(1, question):
        num = i * j
        print(f"{num:{digits}}", end=" ")

    print()
