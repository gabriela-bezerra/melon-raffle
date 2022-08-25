"""Randomly pick customer and print customer info"""

from random import choice
from customers import get_customers_from_file


# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
def pick_winner():
    """Choose a random winner from list of customers."""

    chosen_customer = get_customers_from_file()
    chosen_customer = choice(chosen_customer)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won.")


pick_winner()
