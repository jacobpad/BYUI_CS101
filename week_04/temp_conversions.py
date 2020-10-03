"""
Jacob Padgett
W03 Fahrenheit to Celsius
Bro Brian Wilson
"""


def convert_Fahrenheit_to_Celsius(fahrenheit):
    """ Converts """
    return (fahrenheit - 32) * (5 / 9)


user_input = float(
    input(
        "Please enter a tempature you'dd like conveerted from Fahrenheit to Celsius: "
    )
)
print(f"The tempature converted is {convert_Fahrenheit_to_Celsius(user_input):.1f}")
