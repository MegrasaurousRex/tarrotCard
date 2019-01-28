"""
    Basic Tarrot card class used to simulate a Tarrot Card or Tarrot deck
    The TarrotCard objects have no mehtods only attributes

    Author: Scott Larson (scott.a.larson@gmail.com)
    Date: 2019-01-21
"""

import random
from random import shuffle
import uuid
import json

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
    # major_or_minor = random.randint(0, 1)
    # card_choice = 0

    # if major_or_minor == 0:
    #     suite = random.choice(SUITES)
    #     card_choice = random.randint(0, 13)
    # else:
    #     suite = None
    #     card_choice = random.randint(0, 21)

    # return TarrotCard(card_choice, suite)
    # a_deck = get_tarrot_deck()
    a_deck = TarrotDeck()
    a_deck.shuffle_deck(25)
    return random.choice(a_deck.deck)


def get_tarrot_deck() -> list:
    """ Return a Tarrot Deck, a python list of TarrotCard objects """
    # deck = []
    # # should this be passed in as a param?
    # deck_info_file = 'support/tarrot_cards_data.json'

    # for suite in SUITES:
    #     for value in range(14):
    #         deck.append(TarrotCard(value, suite))

    # for value in range(22):
    #     deck.append(TarrotCard(value, None))
    # with open(deck_info_file) as base_data:
    #     the_data = json.load(base_data)
    
    # # Append the major arcana to the deck
    # for card_name, rank in the_data['tarrot_cards']['major_arcana'].items():
    #     deck.append(TarrotCard(rank, card_name + " " + rank, None))
    
    # for suite in the_data['tarrot_cards']['minor_arcana']['suites']:
    #     for value, card_name in enumerate(the_data['tarrot_cards']['minor_arcana']['cards']):
    #         deck.append(TarrotCard(value, card_name + ' of ' + suite, suite))
    
    return TarrotDeck()


class TarrotCard:
    """ A tarrot card, requires a value and a suite, suite can be None"""
    card_count = 0
    def __init__(self, value, name, suite):

        # if suite:
        #     self.name = MINOR_ARCANA_CNAMES[value] + " of " + suite
        #     self.suite = suite
        #     self.value = value + 1
        #     self.rank = MINOR_ARCANA_CNAMES[value]
        #     self.arcana = "Minor"
        #     self.reversed = False
        # else:
        #     self.name = MAJOR_ARCANA_CNAMES[value] + " " + str(MAJOR_ARCANA_RANKS[value])
        #     self.suite = suite
        #     self.value = value + 1
        #     self.rank = MAJOR_ARCANA_RANKS[value]
        #     self.arcana = "Major"
        #     self.reversed = False

        if suite:
            self.name = name
            self.suite = suite
            self.value = value + 1
            self.rank = value + 1
            self.arcana = "Minor"
            self.reversed = False
        else:
            self.name = name
            self.suite = suite
            self.value = value
            self.rank = value
            self.arcana = "Major"
            self.reversed = False
        TarrotCard.card_count += 1

    def __str__(self):
        return self.name()

class TarrotDeck():
    '''A Tarrot Deck'''

    def __init__(self):
        """Each deck will have a GUID, a deck, and a spread """
        self.deck_guid = str(uuid.uuid1())
        self.deck = []
        self.spread = []

        # for suite in SUITES:
        #     for value in range(14):
        #         self.deck.append(TarrotCard(value, suite))

        # for value in range(22):
        #     self.deck.append(TarrotCard(value, None))
        # should this be passed in as a param?
        deck_info_file = 'support/tarrot_cards_data.json'

        with open(deck_info_file) as base_data:
            the_data = json.load(base_data)
        
        # Append the major arcana to the deck
        # for card_name, rank in the_data['tarrot_cards']['major_arcana'].items():
        #     self.deck.append(TarrotCard(rank, card_name + " " + rank, None))
        
        # for suite in the_data['tarrot_cards']['minor_arcana']['suites']:
        #     for card_name in the_data['tarrot_cards']['minor_arcana']['cards']:
        #         self.deck.append(TarrotCard(card_name + ' of ' + suite, suite))
        for card_name, rank in the_data['tarrot_cards']['major_arcana'].items():
            self.deck.append(TarrotCard(rank, card_name + " " + rank, None))
        
        for suite in the_data['tarrot_cards']['minor_arcana']['suites']:
            for value, card_name in enumerate(the_data['tarrot_cards']['minor_arcana']['cards']):
                self.deck.append(TarrotCard(value, card_name + ' of ' + suite, suite))

    def __str__(self):
        """String repr for the deck"""
        return "TarrotDeck ID: " + self.deck_guid

    def __len__(self):
        """Get the size of the deck """
        return len(self.deck)

    def shuffle_deck(self, times_to_shuffle=13):
        '''shuffle the deck 'times_to_shuffle', default is 13 '''
        if len(self.spread) > 0:
            for a_card in self.spread:
                # before shuffeling the deck, get cards from spread
                self.deck.append(self.spread.pop())

        for this_round in range(0, times_to_shuffle):
            shuffle(self.deck)
            if this_round == times_to_shuffle - 1:
                print("\r")

    def draw_a_card(self):
        """
            Draw, pop(), a card from the top of the deck 
        """
        return self.deck.pop()

    def get_a_spread(self, spread_size=3):
        ''' Return a list of cards, "a spread", default is 3 cards
            The cards are popped off of the deck
        '''
        self.shuffle_deck(15)

        for i in range(0, spread_size):
            self.spread.append(self.draw_a_card())

