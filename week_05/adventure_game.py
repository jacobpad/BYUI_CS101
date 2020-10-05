"""
Jacob Padgett
W05 Adventure Game
Bro Brian Wilson
"""


# Clear the terminal
clear = chr(27) + "[2J"
print(clear)


d = "-" * 75

print("RULES:\nType the capitalized word of the choice you'd like to follow.\n")

print(
    f"""{d}\n\nYou have been tossed into a new land. 
You find yourself on a road you've \nnever before seen..."""
)


input("\nPress Enter to continue...")
print(clear)

##############################################################################
# The option with 3 choices
##############################################################################
initial_choice = """
\nYou come to a fork in the road. Do you go LEFT or RIGHT (or QUIT)?
"""

##############################################################################
# LEFT
##############################################################################

# LEVEL_1 from initial_choice
LEFT = """
While going down the path to the left, you hear a noise, and monkeys begin to 
gather round you. Do you RUN or STAY still?
"""

# LEVEL_2 from LEFT
RUN = """
You run for your life and don't see the hole you fall into. Upon hitting the 
ground, you find a map etched onto the wall. Do you try to MEMORIZE the map, 
or just IGNORE it thinking this is all a dream anyways?"
"""

# LEVEL_2 from LEFT
STAY = """
You remember that you have a pocketknife in your pocket. You slowly move 
you hand to your pocket. As the monkeys close in, you quickly PULL out the 
knife and prepare to defend yourself, or KEEP your hand in your pocket?
"""

# LEVEL_3 from RUN
MEMORIZE = """
You memorize the map, and following it leads you to safty. As you are exiting 
the tunnel, you are met with a crowd of people, who are all cheering for you. 
You put the pieces together and realize you're on a TV show. Now you're famous!
Oh yeah, and rich. Life can't be shallower than this. The end.
"""

# LEVEL_3 from RUN
IGNORE = """
You begin to wonder around without any kind of direction. It's only a matter of
days until you die... (days pass) ...you're dead. The end.
"""

# LEVEL_3 from STAY
PULL = """
As the monkeys move in, they gain speed. They're angry! The sudden movement of
pulling out the pocketknife causes them to overtake you. You've lost the battle. 
You die. The end.
"""

# LEVEL_3 from STAY
KEEP = """
As your hand stays in your pocket, you remember that you had been given a lucky
coin that grants you a wish. You rub the coin and express your wish to be safe.
Poof! You're back in a familiar spot, safe and sound. The end.
"""

##############################################################################
# RIGHT
##############################################################################

# LEVEL_1 from initial_choice
# RIGHT
RIGHT = """
You go to the right, and hours later, when it's getting dark, you see lights in 
the distance. It's a village. As you approach, you have a decision to make. Do 
you SNOOP around a bit, or GO up to the first person you see and try to get 
some answers?
"""

# LEVEL_2 from RIGHT
SNOOP = """
You carefully advance. As you snoop around, you notice a large building in the 
center of the village. It's completely illuminated inside, and the walls seem 
to glow. You notice there's an open door around back. You cautiously approach. 
The entrance has a static-like veil blocking you from seeing inside, but it 
doesn't stop you from hearing the conversations going on. Do you TRY to go in 
or head towards ANOTHER building?
"""

# LEVEL_2 from RIGHT
GO = """
The first person you see is a child, it appears about 10 years old. You 
introduce yourself and ask where you are. The child looks at you, like you're 
some kind of alien, says a quick chant, and disappears in thin air. You're 
amazed! Do you RECITE the same chant, or keep LOOKING for someone else.
"""

# LEVEL_3 from SNOOP
TRY = """
You easily pass through, going in with no problem. However, the conversation 
going on is proving to be an issue. You can't understand it, but you sense it's
dangerous. You try to escape, but the way you came in was a one-way entrance. 
When it comes down to it, the suspense of what happens next kills you. The end.
"""

# LEVEL_3 from SNOOP
ANOTHER = """
You head off towards another building, but as you are snooping around, you hear
a voice call your name. Suddenly, you're captured, and wisped away to a 
Blackhawk Helicopter... Your countries armed forces have rescued you, you are 
no longer at risk of becoming a hostage, and upon returning to your native 
soil, you become a national icon and hero. The end.
"""

# LEVEL_3 from GO
RECITE = """
You recite the chant, word for word, as best as you can. Suddenly, you find 
yourself back in the presence of the 10-year-old, along with a crowd of 
thousands of others. They all look enough like you, which gives you enough time
to find an escape route. You do so, and your life is spared from this weird 
event. The end.
"""

# LEVEL_3 from GO
LOOKING = """
You continue looking for someone else... The place seems to be a ghost town, 
literally. That kid just disappeared. You begin looking around and see a boat. 
You get in the boat and suddenly the sky becomes a map, with a giant star 
marking your home. Eventually, you arrive safely back home to your family. 
The end.
"""


def get_input(question):
    print(clear)
    print(d)
    choice = input(f"{question}")
    return choice.upper()


inital = get_input(initial_choice)


an_error = f"""
\nMake sure to match the spelling of the capital word of your choice.
That input was incorrect.
"""

if inital == "LEFT" or inital == "RIGHT" or inital == "QUIT":
    if inital == "LEFT" or inital == "RIGHT":
        if inital == "LEFT":
            x = get_input(LEFT)
            if x == "RUN" or x == "STAY":
                if x == "RUN":
                    x = get_input(RUN)
                    if x == "MEMORIZE" or x == "IGNORE":
                        if x == "MEMORIZE":
                            print(clear)
                            print(d)
                            print(MEMORIZE)
                        if x == "IGNORE":
                            print(clear)
                            print(d)
                            print(IGNORE)
                    else:
                        print(an_error)
                elif x == "STAY":
                    x = get_input(STAY)
                    if x == "PULL" or x == "KEEP":
                        if x == "PULL":
                            print(clear)
                            print(d)
                            print(PULL)
                        if x == "KEEP":
                            print(clear)
                            print(d)
                            print(KEEP)
                    else:
                        print(an_error)
                else:
                    print(an_error)
            else:
                print(an_error)
        elif inital == "RIGHT":
            x = get_input(RIGHT)
            if x == "SNOOP" or x == "GO":
                if x == "SNOOP":
                    x = get_input(SNOOP)
                    if x == "TRY" or x == "ANOTHER":
                        if x == "TRY":
                            print(clear)
                            print(d)
                            print(TRY)
                        elif x == "ANOTHER":
                            print(clear)
                            print(d)
                            print(ANOTHER)
                    else:
                        print(an_error)
                elif x == "GO":
                    x = get_input(GO)
                    if x == "RECITE" or x == "LOOKING":
                        if x == "RECITE":
                            print(clear)
                            print(d)
                            print(RECITE)
                        elif x == "LOOKING":
                            print(clear)
                            print(d)
                            print(LOOKING)
                    else:
                        print(an_error)
                else:
                    print(an_error)
            else:
                print(an_error)
        else:
            print(an_error)
    elif inital == "QUIT":
        print(
            f"""\nThanks for opening the game... 
May you continue further another time!\n"""
        )
else:
    print(an_error)
