"""
Jacob Padgett
W11 Team Activity
Bro Brian Wilson
"""

# Clear the terminal
clear = chr(27) + "[2J"
print(clear, "\n")


###############################################################################
max_chapters = -1
book_with_max = ""

chosen_volume = input(
    "Which volume of scripture would you like to learn about? \n(Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price)\n: "
)

with open("week_12/books_and_chapters.txt") as f:

    for line in f:

        section = line.strip().split(":")
        book = section[0]

        chapters = int(section[1])

        scripture = section[2]

        # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

        if scripture.lower() == chosen_volume.lower():

            # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

            if chapters > max_chapters:
                max_chapters = chapters
                book_with_max = book

print(f"The book with the most chapters is: {book_with_max}")
print(f"It has {max_chapters} chapters.")
