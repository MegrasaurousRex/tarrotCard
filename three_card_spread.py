#!/usr/bin/env python3.6
"""
    A python three card tarrot spread generator.
    Uses the TarrotCard class to receive a deck (list) of tarrot card objects.

    The deck is shuffled at the begining of each run and the cards are 
    removed (popped) from the deck and put into the spread, another list. 

    At the end of the reading the user is asked if they want another spread. 
    If they do the spread cards are inserted back into the deck and the loop starts 
    again.

    I have tried to model the deck, cards and flow of the spread as realistically
    as possible.
    
    Author: Scott Larson (scott.a.larson@gmail.com)
    Date: 2019-01-21
"""

from tarrotCard import getTarrotDeck
from support.logos import logo2 as logo
from random import randint, shuffle
import os


def shuffle_the_deck(the_deck, max_shuffles=15):
    """
        Shuffle the deck a random number of times to simulate a real shuffling.
        Shuffle a minimum of 2 times, and a random max number having a default 
        max of 15 times. Note: 'random.shuffle()' shuffles a sequence in place. 
    """
    
    for round_of_shuffeling in range(2,randint(3,max_shuffles)):
        if round_of_shuffeling == 5: # pep8, unused var wrng, this to stop it
            print('',end='')
        shuffle(the_deck)

def print_card_for_spread(card_number, card, color=30):
    """
        card is a tarrot card object, color is a string of 30,31,32,33,34 or 35
    """
    # setup and format the message to print
    # The output message uses colored text, the follwoing string
    # is used as a template to build the colored message.
    the_output = """\033[31m{}: \033[0m \033[0{}m{} {}\033[0m"""
    reversed_card = " **Reversed**" if card.reversed == True else ""
    card_msg_lst = ["Your", "The 1st","The 2nd","The 3rd"]
    card_message = card_msg_lst[card_number] + " Card is" + "\t"

    print(the_output.format(card_message, color, card.name, reversed_card))

if __name__ == "__main__":

    myDeck = getTarrotDeck()

    while True:
        
        # randomize the cards
        shuffle_the_deck(myDeck, 50)
        
        os.system('clear')

        spread = []
        print("\033[35mWelcome to the Tarrot simple three card spread generator")
        do_the_reading = input("\033[36mTo create your spread press enter >>\033[0m")
        
        # Build and display the spread.
        while True:
            # get the top 4 cards, as you would in a physical reading.
            card = myDeck.pop(0)

            # Tarrot cards can be reversed, see if this card is 'reversed'. 
            if randint(1,243) % 19 == 9: # should be roughly 5% of all cards. Because 13. Really, Just Because.
                card.reversed = True
            
            # Add the card to the spread
            spread.append(card)
            
            # Only get 4 cards for this spread
            if len(spread) == 4:
                break

        # Print the cards of the spread out for the user
        for inc, card in enumerate(spread):
            print_card_for_spread(inc, card, str(32 + inc))

        print("\n\033[35mPlease refer to google for the meanings of the cards and\
        \n\rhttps://thesimpletarot.com/3-card-tarot-spreads-for-beginners/\
        \n\rfor information on the many kinds of three card spreads that exist.\033[0m")

        if input('Play again Enter or "n" to exit: ').lower() == 'n':
            break

        # reset reversed, and put the cards back into the deck for another round
        for card in spread:
            card.reversed = False
            myDeck.insert(card.value, card)

    print("Thank you for using...{}".format(logo))

