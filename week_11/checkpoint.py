"""
Jacob Padgett
W10 Check Point
Bro Brian Wilson
"""

with open("week_11/books.txt") as f:
    for line in f:
        print(line.strip("\n").strip())
