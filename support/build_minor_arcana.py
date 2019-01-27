
MINOR_ARCANA_CNAMES = ("A", "2", "3", "4", "5", "6", "7", "8", "9",
                       "10", 'Jack', 'Knight', 'Queen', 'King')
SUITES = ("Cups", "Swords", "Wands", "Pentacles")

for suite in SUITES:
     for value, a_card in enumerate(MINOR_ARCANA_CNAMES):
        # print("{} of {}".format(a_card, suite))
        print("'{} of {}':{},".format(a_card, suite, value + 1))