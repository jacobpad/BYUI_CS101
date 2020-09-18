def get_name():
    """Get's user name"""
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    lst = [first_name.capitalize(), last_name.capitalize()]

    return lst


def give_name():
    """Returns back the name from above"""
    lst = get_name()

    print(f"Your name is {lst[1]}, {lst[0]} {lst[1]}.")


give_name()
