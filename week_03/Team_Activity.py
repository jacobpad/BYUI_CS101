"""
Jacob Padgett
W03 Team Activity
Bro Brian Wilson
"""

squ_len = float(input("\nWhat is the length of a side of the square: "))
print(f"The area of the square is: {squ_len **  2}")

rec_len = float(input("\nWhat is the length of rectangle: "))
wid_rec = float(input("What is the width of the rectangle: "))
print(f"The area of the rectangle is: {rec_len * wid_rec}")

cir_radius = float(input("\nWhat is the radius of the circle: "))
print(f"The area of the circle is: {3.14 * (cir_radius ** 2):.7}\n")


##############################################################################
# Stretch 1
##############################################################################

# import math

# def area_of_square(x):
#     return x ** 2


# def area_of_rectangle(x, y):
#     return x * y


# def area_of_circle(x):
#     return math.pi * (x ** 2) # Use `math.pi`


# squ_len = float(input("\nWhat is the length of a side of the square: "))
# print(f"The area of the square is: {area_of_square(squ_len)}")

# rec_len = float(input("\nWhat is the length of rectangle: "))
# wid_rec = float(input("What is the width of the rectangle: "))
# print(f"The area of the rectangle is: {area_of_rectangle(rec_len, wid_rec)}")

# cir_radius = float(input("\nWhat is the radius of the circle: "))
# print(f"The area of the circle is: {area_of_circle(cir_radius):.7}")


##############################################################################
# Stretch 2
##############################################################################


# def stretch_2(x):
#     print(f"Area of a square with that length of side: {area_of_square(x)}")
#     print(f"A circle with that radius: {area_of_circle(x):.7}")
#     print(f"And then the volume of a cube with that side: {x ** 3}")
#     print(f"A sphere with that radius: {((4/3) * math.pi) * (x ** 3):.7}")


# num = float(input("\nGive me some number: "))
# stretch_2(num)


##############################################################################
# Stretch 3
##############################################################################

# # Square
# squ_len = float(
#     input("\nWhat is the length of a side of the square (value in centimeters): ")
# )
# print(f"The area of the square is: {area_of_square(squ_len)} cm^2")
# print(f"The area of the square is: {area_of_square(squ_len) / 10000} m^2")

# # Rectangle
# rec_len = float(input("\nWhat is the length of rectangle (value in centimeters): "))
# wid_rec = float(input("What is the width of the rectangle (value in centimeters): "))
# print(f"The area of the rectangle is: {area_of_rectangle(rec_len, wid_rec)} cm^2")
# print(
#     f"The area of the rectangle is: {area_of_rectangle(rec_len, wid_rec) / 10000} m^2"
# )

# # Circle
# cir_radius = float(input("\nWhat is the radius of the circle (value in centimeters): "))
# print(f"The area of the circle is: {area_of_circle(cir_radius):.7} cm^2")
# print(f"The area of the circle is: {area_of_circle(cir_radius) / 10000:.7} m^2\n")
