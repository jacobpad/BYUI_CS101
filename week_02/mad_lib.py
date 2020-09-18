"""
Jacob Padgett
W02 Prove: Assignment - MadLib
Bro Brian Wilson
"""


def display_introduction():
    intro = "\nThis is a MadLib game, composed by Jacob Padgett\n\nYou will be asked for some words. Please provide the appropiate word when prompted.\n"
    return intro


def get_plural_noun():
    """
    Get's plural_noun word from user
    Returns users word
    """
    plural_noun = input("Please provide a Plural Noun: ")
    return plural_noun


def get_verb():
    """
    Get's verb word from user
    Returns users word
    """
    verb = input("Please provide a Verb: ")
    return verb


def get_adjective():
    """
    Get's adjective word from user
    Returns users word
    """
    adjective = input("Please provide an Adjective: ")
    return adjective


def get_noun():
    """
    Get's noun word from user
    Returns users word
    """
    noun = input("Please provide a Noun: ")
    return noun


def get_exclamation():
    """
    Get's exclamation word from user
    Returns users word
    """
    exclamation = input("Please provide an Exclamation: ")
    return exclamation


def get_animal():
    """
    Get's animal word from user
    Returns users word
    """
    animal = input("Please provide an Animal: ")
    return animal


# Prints the introduction text from line 9 above
print(display_introduction())

# Get's user input and stores it in a list for use in the story later
user_word_order = [
    get_adjective().lower(),  # index[0]
    get_animal().lower(),  # index[1]
    get_verb().lower(),  # index[2]
    get_exclamation().capitalize(),  # index[3]
    get_verb().lower(),  # index[4]
    get_verb().lower(),  # index[5]
]

# The game text
game_text = f"""
The other day, I was really in trouble. It all started when I saw a very
{user_word_order[0]} {user_word_order[1]} {user_word_order[2]} down the hallway. "{user_word_order[3]}!" I yelled. But all
I could think to do was to {user_word_order[4]} over and over. Miraculously,
that caused it to stop, but not before it tried to {user_word_order[5]}
right in front of my family.
"""

# Prints the final output
print(game_text)
