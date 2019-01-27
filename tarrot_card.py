"""
    Basic Tarrot card class used to simulate a Tarrot Card or Tarrot deck
    The TarrotCard objects have no mehtods only attributes

    Author: Scott Larson (scott.a.larson@gmail.com)
    Date: 2019-01-21
"""

import random

# Unsure if these should go in the TarrotCard class or not...
MAJOR_ARCANA_CNAMES = ("The Magician", "The High Priestess", "The Empress",
                       "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
                       "Strength", "The Hermit", "Wheel of Fortune", "Justice",
                       "The Hanged Man", "Death", "Temperance", "The Devil",
                       "The Tower", "The Star", "The Moon", "The Sun", "Judgement",
                       "The World", "The Fool")
MAJOR_ARCANA_RANKS = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                      "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII",
                      "XVIII", "XIX", "XX", "XXI", None)
MINOR_ARCANA_CNAMES = ("A", "2", "3", "4", "5", "6", "7", "8", "9",
                       "10", 'Jack', 'Knight', 'Queen', 'King')
SUITES = ("Cups", "Swords", "Wands", "Pentacles")


def get_random_tarrot_card():
    """Return a random Tarrot card object"""
    major_or_minor = random.randint(0, 1)
    card_choice = 0

    if major_or_minor == 0:
        suite = random.choice(SUITES)
        card_choice = random.randint(0, 13)
    else:
        suite = None
        card_choice = random.randint(0, 21)

    return TarrotCard(card_choice, suite)


def get_tarrot_deck() -> list:
    """ Return a Tarrot Deck, a python list of TarrotCard objects """
    deck = []

    for suite in SUITES:
        for value in range(14):
            deck.append(TarrotCard(value, suite))

    for value in range(22):
        deck.append(TarrotCard(value, None))

    return deck


class TarrotCard:
    """ A tarrot card, requires a value and a suite, suite can be None"""
    card_count = 0
    def __init__(self, value, suite):

        if suite:
            self.name = MINOR_ARCANA_CNAMES[value] + " of " + suite
            self.suite = suite
            self.value = value + 1
            self.rank = MINOR_ARCANA_CNAMES[value]
            self.arcana = "Minor"
            self.reversed = False
        else:
            self.name = MAJOR_ARCANA_CNAMES[value] + " " + str(MAJOR_ARCANA_RANKS[value])
            self.suite = suite
            self.value = value + 1
            self.rank = MAJOR_ARCANA_RANKS[value]
            self.arcana = "Major"
            self.reversed = False

        TarrotCard.card_count += 1

    def __str__(self):
        return self.name()

class TarrotDeck():
    '''A Tarrot Deck'''
    from random import shuffle

    card_count = 0

    def __init__(self):
        import uuid
        self.deck_guid = str(uuid.uuid1())
        self.deck = []
        for suite in SUITES:
            for value in range(14):
                self.deck.append(TarrotCard(value, suite))
                TarrotDeck.card_count += 1

        for value in range(22):
            self.deck.append(TarrotCard(value, None))
            TarrotDeck.card_count += 1

    def get_deck_information(self):
        """Get information about the deck """
        return self.deck_guid

    def shuffle_deck(self, times_to_shuffle=13):
        '''shuffle the deck 'times_to_shuffle', default is 13 '''
        for this_round in range(0, times_to_shuffle):
            random.shuffle(self.deck)
            if this_round == times_to_shuffle - 1:
                print("\r")


    def get_a_spread(self, spread_size=3):
        ''' Get cards for a spread, default is 3 cards '''
        self.shuffle(self.deck)
        the_spread = []
        ### Pick UP Here:
        ### Need to implement getting x cards
        ### pop them to get uniqe cards
        ### return them to the deck, for future calls
        ### return the temp_deck
