
"""
    A very simple script to get a single Tarrot card
    using the TarrotCard class.

    Author: Scott Larson (scott.a.larson@gmail.com)
    Date: 2019-01-21

    2019-01-27 pylint score 10/10
"""

import os
from tarrot_card import get_random_tarrot_card
from support.logos import LOGO4 as logo

# This will get random cards from a TarrotDeck Object

while True:
    os.system('clear')
    print("Welcome to the single card Tarrot spread")

    YOUR_CARD = get_random_tarrot_card()
    print("Your card is: {}".format(YOUR_CARD.name))

    CONT = input("Get anther card ('n' to exit)")
    if CONT.lower() == "n":
        print("Thanks for playing")
        break

print("Thank you for using...{}".format(logo))
