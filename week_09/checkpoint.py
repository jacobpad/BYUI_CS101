"""
Jacob Padgett
W09 Check Point
Bro Brian Wilson
"""

# Clear the terminal
clear = chr(27) + "[2J"
print(clear)

friends = []
name = None

while name != "End":
    name = input("\nWhat are your friends names?\n(type 'end' to be done)\n")

    name = name.title()

    if name.title() != "End":
        friends.append(name)

    print(clear)
    print("Add another friend...")

print(clear)
print(f"\nYour friends are:")
print("-" * 17)

for i in friends:
    print(i)

print()
