"""
Jacob Padgett
W03 Prepare: Checkpoint
Bro Brian Wilson
"""

"""
Write a program that does the following:

Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
"""

print("\n")

user_age = int(input("How old are you: "))
print(f"On your next birthday, you will be {user_age  + 1}\n")


egg_cartons = int(input("So you like eggs, how many egg cartons do you have: "))
print(f"You have {egg_cartons * 12} eggs\n")

n_cookies = int(input("How many cookies do you have: "))
n_people = int(input("You'll be sharing with how many people: "))
print(f"Each person may have {num_cookies / num_people} cookies\n")
# print(
#     f"""
#                 .---. .---.
#                :     : o   :    Each person may have {n_cookies / n_people} cookies!
#            _..-:   o :     :-.._    /
#        .-''  '  `---' `---' "   ``-.
#      .'   "   '  "  .    "  . '  "  `.
#     :   '.---.,,.,...,.,.,.,..---.  ' ;
#     `. " `.                     .' " .'
#      `.  '`.                   .' ' .'
#       `.    `-._           _.-' "  .'  .----.
#         `. "    '"--...--"'  . ' .'  .'  o   `.
#         .'`-._'    " .     " _.-'`. :       o  :
#       .'      ```--.....--'''    ' `:_ o       :
#     .'    "     '         "     "   ; `.;";";";'
#    ;         '       "       '     . ; .' ; ; ;
#   ;     '         '       '   "    .'      .-'
#   '  "     "   '      "           "    _.-'
#   """
# )
