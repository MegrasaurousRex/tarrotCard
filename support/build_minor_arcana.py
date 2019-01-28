"""
    This file was for fine tuning the the work with the json file
"""
MINOR_ARCANA_CNAMES = ("A", "2", "3", "4", "5", "6", "7", "8", "9",
                       "10", 'Jack', 'Knight', 'Queen', 'King')
SUITES = ("Cups", "Swords", "Wands", "Pentacles")

## The following is no good. We have define a minor suite as having a suite and a value... So
## the json structure should be <suite>:{<name>:<value>,<name>:<value>,...}
# for suite in SUITES:
#      for value, a_card in enumerate(MINOR_ARCANA_CNAMES):
#         # print("{} of {}".format(a_card, suite))
#         print("'{} of {}':{},".format(a_card, suite, value + 1))

# for suite in SUITES:
#     print('"{}": {\'\n'.format(suite))
#     for the_card in enumerate(MINOR_ARCANA_CNAMES):
#         print('\t{{{}}}')

def work_with_json_like_data():
    minor_arcana = {"minor_arcana":{
            "suites":['Cups', 'Swords', 'Wands', 'Pentacles'],
            "cards":["A", "2", "3", "4", "5", "6", "7", "8", "9",
                     "10", 'Jack', 'Knight', 'Queen', 'King']
            }
    }
    
    print(minor_arcana["minor_arcana"]['suites'])
    print(type(minor_arcana["minor_arcana"]['suites']))
    for suite in minor_arcana["minor_arcana"]['suites']:
        for value, a_card_name in enumerate(minor_arcana['minor_arcana']['cards']):
            print("{} of {} value: {}".format(a_card_name, suite, value))

## work with json like data (a dict) in the file
# work_with_json_like_data()

## Load data from the json file... real json data
def work_with_json_data():
    import json
    the_json_data_file = 'tarrot_cards_data.json'  # make this a param?
    with open(the_json_data_file) as base_data:
        the_data = json.load(base_data)
    
    # print(the_data['tarrot_cards'])
    deck_list = []

    for key, value in the_data['tarrot_cards']['major_arcana'].items():
        # print(key, value)
        deck_list.append(key + " " + value)

    for suite in the_data['tarrot_cards']['minor_arcana']['suites']:
        #print(suite)
        for value, card in enumerate(the_data['tarrot_cards']['minor_arcana']['cards']):
            # print('{} of {}, with value: {}'.format(card, suite, value))
            deck_list.append('{} of {}, with value: {}'.format(card, suite, value))
    
    for the_card in deck_list:
        print(the_card)
    
work_with_json_data()
