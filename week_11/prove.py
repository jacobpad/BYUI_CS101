"""
Jacob Padgett
W11 Prove
Bro Brian Wilson
"""

# Clear the terminal
clear = chr(27) + "[2J"
print(clear, "\n")

d = "-" * 79  # Divider

###############################################################################

import pandas as pd


url = "https://byui-cse.github.io/cse110-course/lesson11/life-expectancy.csv"
df = pd.read_csv(url)

# Milestone Requirements
print("The following two lines are to satisify the Milestone Requirements")

lowest_life_years = df["Life expectancy (years)"].min()
print(f"Lowest Life expectancy (years): {lowest_life_years}")

highest_life_years = df["Life expectancy (years)"].max()
print(f"Highest Life expectancy (years): {highest_life_years}")

print("\n", d, "\n")

###############################################################################
# Assignment Requirements
sorted_life_expectancy = (
    df.sort_values("Life expectancy (years)")
    .reset_index()
    .drop(columns="index", axis=1)
)

###############################################################################
# What is the year and country that has the lowest life expectancy in the dataset?
###############################################################################
# Get the lowest
lowest = sorted_life_expectancy[["Year", "Entity"]].iloc[0]
lowest_year = lowest[0]
lowest_country = lowest[1]

print(
    f"The lowest Life expectancy (year) was the year {lowest_year} in {lowest_country}."
)

###############################################################################
# What is the year and country that has the highest life expectancy in the dataset?
###############################################################################
# Get the highest
highest = sorted_life_expectancy[["Year", "Entity"]].iloc[-1]
highest_year = highest[0]
highest_country = highest[1]

print(
    f"And the highest Life expectancy (year) was the year {highest_year} in {highest_country}."
)

print("\n", d, "\n")

###############################################################################
# Allow the user to type in a year, then, find the average life expectancy for that year.
# Then find the country with the minimum and the one with the maximum life expectancies
# for that year.
###############################################################################

user_year = int(input("Will you please choose a year to view? "))

life_expectancy_list = []
ntity_list = []
tup_list = []

for i in range(len(sorted_life_expectancy["Year"])):
    if user_year == sorted_life_expectancy["Year"][i]:
        life_expectancy = sorted_life_expectancy["Life expectancy (years)"][i]
        ntity = sorted_life_expectancy["Entity"][i]

        life_expectancy_list.append(life_expectancy)
        ntity_list.append(ntity)


for country, age in zip(ntity_list, life_expectancy_list):
    combo = (country, age)
    tup_list.append(combo)


def sort_lists(list_of_tuples):
    list_of_tuples.sort(key=lambda x: x[1])
    return list_of_tuples


user_year_average = sum(life_expectancy_list) / len(life_expectancy_list)

fin = sort_lists(tup_list)

minimum = fin[0]
maximum = fin[-1]

print(
    f"""
\nThe average life expectancy during the year {user_year} was {user_year_average:.1f}
\nYou may be interested to know some more information about the year...
\nThe countries with the minimum and maximum life expectancies for {user_year} were:
   • Minimum: {minimum[0]} with a life expectancy of {minimum[1]:.01f} years.
   • Maximum: {maximum[0]} with a life expectancy of {maximum[1]:.01f} years.
"""
)
