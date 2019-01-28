"""
    Basic Tarrot card class to simulate a Tarrot Card and Tarrot deck

    Author: Scott Larson (scott.a.larson@gmail.com)
    Date: 2019-01-27
"""

from random import shuffle, randint, choice
import uuid
import json


def get_random_tarrot_card():
    """Return a random Tarrot card object"""
    a_deck = TarrotDeck()
    a_deck.shuffle_deck(25)
    return choice(a_deck.deck)


def get_tarrot_deck() -> list:
    """ Return a Tarrot Deck, a python list of TarrotCard objects """
    return TarrotDeck()


class TarrotCard:
    """ A tarrot card, requires a value and a suite, suite can be None"""
    def __init__(self, value, name, suite):

        if suite:
            self.name = name
            self.suite = suite
            self.value = value + 1
            self.rank = suite[0].upper() + str(value + 1)
            self.arcana = "Minor"
            self.reversed = False
        else:
            self.name = name
            self.suite = suite
            self.value = value
            self.rank = value
            self.arcana = "Major"
            self.reversed = False

    def __str__(self):
        return self.name()

    def __len__(self):
        return 1


class TarrotDeck():
    '''A Tarrot Deck class'''

    def __init__(self):
        """Each deck will have a GUID, a deck, and a spread """
        self.deck_guid = str(uuid.uuid1())
        self.deck = []
        self.spread = []

        # Get the data to build the deck
        deck_info_file = 'support/tarrot_cards_data.json'

        with open(deck_info_file) as base_data:
            the_data = json.load(base_data)

        # Append Major Arcana to the deck
        for card_name, rank in the_data['tarrot_cards']['major_arcana']\
                .items():
            self.deck.append(TarrotCard(rank, card_name + " " + rank, None))

        # Append Minor Arcana to the deck
        for suite in the_data['tarrot_cards']['minor_arcana']['suites']:
            for value, card_name in enumerate(the_data['tarrot_cards']['minor_arcana']['cards']):
                self.deck.append(TarrotCard(value, card_name + ' of ' + suite, suite))

    def __str__(self):
        """String repr for the deck, this may be excessive"""
        for card in self.deck:
            print(card.name, card.rank, card.value)
        return "TarrotDeck ID: " + self.deck_guid

    def __len__(self):
        """Get the size of the deck """
        return len(self.deck)

    def shuffle_deck(self, times_to_shuffle=13):
        '''shuffle the deck 'times_to_shuffle', default is 13 '''

        # if a spread list exists, put those cards back into the deck.
        while self.spread:
            a_card = self.spread.pop()
            a_card.reversed = False
            self.deck.append(a_card)

        # shuffle the cards sufficently to randomize the deck
        for this_round in range(0, times_to_shuffle):
            shuffle(self.deck)
            if this_round == times_to_shuffle - 1:
                pass  # to make pylint shut up

        # Ensure we have the right number of cards, alert if not
        if len(self.deck) != 78:
            print("Something is wrong, there are: {} \
                   cards".format(len(self.deck)))

    def draw_a_card(self):
        """
            Draw, pop(), a card from the top of the deck, just pops a card
            You have to manage the card and put it back in the deck.
            Randomly causes a card to be reversed.
        """
        card = self.deck.pop()
        if randint(1, 243) % 19 == 9:  # should be roughly 5% of all cards.
            card.reversed = True
        return card

    def get_a_spread(self, spread_size=4):
        ''' Return a list of cards, "a spread", default is 4 cards
            The cards are popped off of the deck
        '''
        if spread_size > 78:
            spread_size = 78

        # Randomize again, just to be sure
        self.shuffle_deck(15)

        # Put all of the cards into the spread
        for i in range(0, spread_size):
            if i == 8:
                pass  # to shut up pylint
            self.spread.append(self.draw_a_card())
