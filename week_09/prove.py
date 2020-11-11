"""
Jacob Padgett
W09 Prove
Bro Brian Wilson
"""
import time


# Use the lists because the asignment calls for it...
# even though a dictionary would be a better choice.
items = []
prices = []

# Other variables
d = "-" * 25
pair = "Price\tItem"
clear = chr(27) + "[2J"  # clear the terminal

prompt_user = """
What would you like to do: (enter the number)

1 - Add a new item
2 - Display the contents of the shopping cart
3 - Remove an item (only needed for the final project deliverable)
4 - Compute the total (only needed for the final project deliverable)

5 - Quit\n
"""

print(clear)

response = None

while response != 5:

    response = int(input(prompt_user))

    # Add a new item
    if response == 1:
        print(clear)
        x = input("What is the new item you'd like to add? ")
        time.sleep(0.25)
        y = float(input(f"What is the price/cost of the {x}: "))
        print(f"{clear}Adding {x.upper()} to your cart\n...Please wait...")
        time.sleep(1.25)
        items.append(x.title())
        prices.append(y)
        print(clear)

    # Display the contents of the shopping cart
    elif response == 2:
        print(clear)
        print(pair)
        print(d)

        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        input("\n\nPress Enter to continue...")

    # Remove an item
    elif response == 3:
        print(clear)
        print(pair)
        print(d)

        # display initial cart before item is removed
        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        # remove item and price
        delete_item = input(
            "\nType the name of the item would you like to remove? "
        ).title()

        print(clear)
        print("Deleting item\n...Please wait...")
        time.sleep(1.5)
        print(clear)

        # get the index number for item to be deleted
        idx_num = items.index(delete_item)

        items.pop(idx_num)
        prices.pop(idx_num)

        # display updated cart
        print(pair)
        print(d)
        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        input("\n\nPress Enter to continue...")
        print(clear)

    # Compute the total
    elif response == 4:
        print(clear)

        # display cart
        print(pair)
        print(d)
        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        print(f"\nYour total cart value is ${sum(prices):.2f}")

        input("\n\nPress Enter to continue...")
        print(clear)

print(clear)
print("\nThanks for using the cart!\n")
