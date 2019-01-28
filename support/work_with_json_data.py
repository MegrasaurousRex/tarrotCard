"""
    Utility file to learn to work with JSON data from a file.
    We know the structure of the file so it is easy to nav.
"""
import json

the_file = 'tarrot_cards_data.json'

with open(the_file) as data:
    the_data = json.load(data)

# print(the_data)
# print("Major Arcana: ")
# print(type(the_data['tarrot_cards']['major_arcana']))
# print(the_data['tarrot_cards']['major_arcana'])

# print("\nMinor Arcana: ")
# print(type(the_data['tarrot_cards']['minor_arcana']))
# print(the_data['tarrot_cards']['minor_arcana'])

for key, value in the_data['tarrot_cards']['major_arcana'].items():
    print(key, value)

for key, value in the_data['tarrot_cards']['minor_arcana'].items():
    print(key, value)
