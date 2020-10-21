"""
Jacob Padgett
W06 Check Point
Bro Brian Wilson
"""


loan_size = int(input("\nHow large is the loan? "))
credit_hist = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_pmt = int(input("How large is your down payment? "))

give_loan = True

# First, check if the loan size is at least 5. If it is, use the following rules:
if loan_size > 4:
    # If the credit history and income are both at least 7, then the decision is "yes"
    if credit_hist > 6 and income > 6:
        give_loan = True
    # If either the credit history or income is at least 7,
    elif credit_hist > 6 or income > 6:
        # then check if the down payment is at least 5, if it is, the decision is "yes",
        if down_pmt > 4:
            give_loan = True
        # if not, the decision is "no"
        else:
            give_loan = False

# Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
else:
    if credit_hist <= 7 or income <= 7:
        give_loan = False

    # Otherwise (if the loan is not 5 or greater), use these rules:
    if loan_size >= 5:
        # If the credit is less than 4, then the decision is "no"
        if credit_hist < 4:
            give_loan = False
        # Otherwise, check the following:
        else:
            # If either the income or the down payment is at least 7, the decision is "yes"
            if income >= 7 or down_pmt >= 7:
                give_loan = True
            # If both the income and the down payment are at least 4, then the answer is "yes"
            if income >= 4 or down_pmt >= 4:
                give_loan = True
            # Otherwise, the decision is "no"
            else:
                give_loan = False

# Finally, display the decision to the user.
print(give_loan)
