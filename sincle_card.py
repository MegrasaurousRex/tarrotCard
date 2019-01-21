import os
from tarrotCard import getRandomTarrotCard
# This will only get random cards and the cards may not be unique



while True:
    os.system('clear')
    print("Welcome to the single card fortune teller")

    your_card = getRandomTarrotCard()
    print("Your card is: {}".format(your_card.name))

    cont = input("Get anther card(y/n)")
    if cont.lower() == "n":
        print("Thanks for playing")
        break
