""" 
    This file exists because I was having trouble putting all of the spread
    cards back in the deck. A regular for loop would only put 2 cards back.
    I had to use a while len(spread) > 0 with the for loop to make it work.
    pylint complains this shouldn't be done... dunno how else to make it work.

    completely removed the for loop. Used the while len(spread) > 0, pop()
    This worked.
"""
import sys
sys.path.append("..")
import tarrot_card

def print_spread_len(a_deck):
    print("len of spread: {}".format(len(a_deck.spread)))

def print_deck_len(a_deck):
    print("len of deck is: {}".format(len(a_deck.deck)))

print("Getting a deck")
a_deck = tarrot_card.TarrotDeck()
print_deck_len(a_deck)
print_spread_len(a_deck)
print()

print("Getting a spread of 4 cards")
a_deck.get_a_spread(4)
# print_deck_len(a_deck)
# print_spread_len(a_deck)
print()

print("Shuffeling")
a_deck.shuffle_deck(13)
print_deck_len(a_deck)
print_spread_len(a_deck)
