"""
Jacob Padgett
W07 Prove
Bro Brian Wilson

NOTE: here is a colab notebook I used to play around in 
https://colab.research.google.com/drive/14YEtmyD5E5cJpKzuq3VtwGyMayoyFP8A?usp=sharing
"""

d = "\n" * 2
dd = "-" * 50
ddd = d + dd
print(ddd)

# This line imports or includes the library we will need
from PIL import Image
import random

# Background Images
beach = Image.open("cse110_images/b_beach.jpg")
desert = Image.open("cse110_images/b_desert.jpg")
earth = Image.open("cse110_images/b_earth.jpg")
field = Image.open("cse110_images/b_field.jpg")
forest = Image.open("cse110_images/b_forest.jpg")
snowscape = Image.open("cse110_images/b_snowscape.jpg")
sunset = Image.open("cse110_images/b_sunset.jpg")

background_images = [beach, desert, earth, field, forest, snowscape, sunset]

# GreenScreen Images
boat = Image.open("cse110_images/boat.jpg")
cactus = Image.open("cse110_images/cactus.jpg")
cat_small = Image.open("cse110_images/cat_small.jpg")
cat = Image.open("cse110_images/cat.jpg")
harvester = Image.open("cse110_images/harvester.jpg")
hiker = Image.open("cse110_images/hiker.jpg")
penguin = Image.open("cse110_images/penguin.jpg")
spaceshuttle = Image.open("cse110_images/spaceshuttle.jpg")

GreenScreen_Images = [
    boat,
    cactus,
    cat_small,
    cat,
    harvester,
    hiker,
    penguin,
    spaceshuttle,
]


def my_pic_func(img_b, img_g):
    """
    Take the img_g and add it onto the img_b to make it look like it's 
    (not) supposed to be there.

    Args:
        img_b (image) 
        img_g (image)
    """

    new_img = Image.new("RGB", img_b.size)  # Make new image

    width, height = img_b.size

    img_b_pixels = img_b.load()
    img_g_pixels = img_g.load()
    new_img_pixels = new_img.load()

    # Change it
    for y in range(height):
        for x in range(width):

            new_img_pixels[x, y] = img_g_pixels[x, y]
            (r, g, b) = img_g_pixels[x, y]
            if g >= 150:
                if r >= 100:
                    new_img_pixels[x, y] = img_g_pixels[x, y]
                else:
                    new_img_pixels[x, y] = img_b_pixels[x, y]

    # Save the image
    new_img.save(f"zzz_new_img.jpg")  # Uncomment this to save the file
    # new_img.show()

    return


# Call it
my_pic_func(random.choice(background_images), random.choice(GreenScreen_Images))
