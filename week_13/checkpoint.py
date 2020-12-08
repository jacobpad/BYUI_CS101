"""
Jacob Padgett
W13 Check Point
Bro Brian Wilson
"""

# Clear the terminal
clear = chr(27) + "[2J"
print(clear, "\n")

###############################################################################


text = "This is a string of text."


def display_regular(x):
    """
    display_regular—Receives a string and prints it out, exactly as received.
    """
    return x


print(display_regular(text))


def display_upper(x):
    """
    display_uppercase—Receives a string, converts it to upper case, and then prints it out.
    """
    return x.upper()


print(display_upper(text))


def display_lowercase(x):
    """
    display_lowercase—Receives a string, converts it to lower case, and then prints it out.
    """
    return x.lower()


print(display_lowercase(text))
