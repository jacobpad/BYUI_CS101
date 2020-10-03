"""
Jacob Padgett
W04 Meal Price Calculator
Bro Brian Wilson
"""


def childs_meal_price():
    x = input("\nThe price of a child's meal: $")
    return x


def adults_meal_price():
    x = input("The price of an adult's meal: $")
    return x


def num_children():
    x = input("The number of children: ")
    return x


def num_adults():
    x = input("The number of adults: ")
    return x


def sales_tax():
    x = input("The sales tax rate (Example: 6.5% = 0.065): 0.")
    return float(x) / 100


lst = [
    float(childs_meal_price()),  # lst[0]
    float(adults_meal_price()),  # lst[1]
    int(num_children()),  # lst[2]
    int(num_adults()),  # lst[3]
    sales_tax(),  # lst[4]
]

subtotal = (lst[0] * lst[2]) + (lst[1] * lst[3])
tax = subtotal * (1 * lst[4])
total = subtotal + tax

details = f"""
\nSubtotal: ${subtotal:0.2f}
Sales Tax: ${tax:0.2f}
Total: ${total:0.2f}
"""
print(details)

payment_amount = float(input("\nWhat is the payment amount: $"))
print(f"Change: ${payment_amount - total:0.2f}\n")
