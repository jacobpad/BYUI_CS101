"""
Jacob Padgett
W07 Checkpoint
Bro Brian Wilson
"""
d = "\n" * 2
dd = "-" * 50

ddd = d + dd
print(ddd)

colors = ["red", "blue", "green", "yellow"]

"""
Use a for loop to iterate through this list one by one and display each item on its own line as follows:
"""
for i in colors:
    print(i)

print(ddd)

for i in range(1, 9):
    print(i)

print(ddd)

go = True
while go:

    if input("May I have a piece of candy? ") == "no":
        input("May I have a piece of candy? ")
    else:
        print("Thank you")
        go = False

