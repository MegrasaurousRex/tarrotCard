#!/usr/bin/env python3.6
"""
    A three card tarrot spread generator written in Python.
    Uses the TarrotDeck class to receive a deck of tarrot card objects.

    The deck is shuffled at the begining of each run and the cards are
    displayed for the user.

    At the end of the reading the user is asked if they want another spread.
    If they do the cards are shuffled angain at the top of the loop.

    Author: Scott Larson (scott.a.larson@gmail.com)
    Date: 2019-01-27
"""

import os
from random import randint
from tarrot_card import TarrotDeck
from support.logos import LOGO2 as logo


def print_card_for_spread(card_number, card, color=30):
    """
        card is a tarrot card object, color is a string of 30,31,32,33,34 or 35
        The card number here is used to display the cards order for the spread.
    """
    # setup and format the message to print
    # The output message uses colored text, the follwoing string
    # is used as a template to build the colored message.
    the_output = """\033[31m{}: \033[0m \033[0{}m{} {}\033[0m"""
    reversed_card = " **Reversed**" if card.reversed else ""
    # the following is only good for 3 card spread
    card_msg_lst = ["Your", "The 1st", "The 2nd", "The 3rd"]
    card_message = card_msg_lst[card_number] + " Card is" + "\t"

    print(the_output.format(card_message, color, card.name, reversed_card))


if __name__ == "__main__":

    MY_DECK = TarrotDeck()

    while True:
        # randomize the cards
        MY_DECK.shuffle_deck(randint(13, 50))

        os.system('clear')

        print("\033[35mWelcome to the Tarrot simple three card spread \
            generator")
        WAIT_FOR_USER = \
            input("\033[36mTo create your spread press enter >>\033[0m")

        # Build and display the spread, using TarrotDeck.get_a_spread() method
        MY_DECK.get_a_spread(4)

        # Print the cards of the spread out for the user. 
        # This script is made for a 4 card spread
        for inc, a_card in enumerate(MY_DECK.spread):
            print_card_for_spread(inc, a_card, str(32 + inc))

        print("\n\033[35mPlease refer to google for the meanings of the cards and\
        \n\rhttps://thesimpletarot.com/3-card-tarot-spreads-for-beginners/\
        \n\rfor information on the many kinds of three card spreads that \
        exist.\033[0m")

        if input('Play again Enter or "n" to exit: ').lower() == 'n':
            break
    
    print("Thank you for using...{}".format(logo))
