"""
Jacob Padgett
W04 Speed of a Falling Object
Bro Brian Wilson
"""

import math


print("Welcome to the velocity calculator. Please enter the following:")

# m = float(input("Mass: "))
m = 5

# g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
g = 9.8

# t = float(input("Time (in seconds): "))
t = 10

# p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
p = 1.3

# A = float(input("Cross sectional area (in m^2): "))
A = 0.01

# C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
C = 0.5

c = (1 / 2) * p * A * C

print(f"{c:.3f}")

# for t in range(470):
#     """For the above inputs"""
#     v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
#     print(f"Terminal velocity happens at {v} seconds")

for t in range(154):
    """For the above inputs"""
    v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
    print(f"{t} - Terminal velocity happens at {v:.03f} seconds")
