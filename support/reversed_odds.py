
from random import randint

def display_results(modulo=19, top_range=243, target_left_over=7):
    hits = 0
    print("Modulo is: {}".format(modulo))
    print("Top range is: {}".format(top_range))
    for i in range(1, top_range):
        if i % modulo == target_left_over:
            hits += 1
            print('Hit # {}: {} % {} == {}'.format(hits, i, modulo, target_left_over))

def display_random_results():
    hits = 0
    # if modulo and target left over are equal no results, prevent that
    while True:
        modulo = randint(1,33)
        top_range = randint(75,300)
        target_left_over = randint(1,9)
        if modulo != target_left_over:
            break

    print("Modulo is: {}".format(modulo))
    print("Top range is: {}".format(top_range))
    print("Target leftover is: {}".format(target_left_over))

    for i in range(0, top_range):
        if i % modulo == target_left_over:
            hits += 1
            print('Hit # {}: {} % {} == {}'.format(hits, i, modulo, target_left_over))


if __name__ == "__main__":
    # display_results(13, 100)
    print("Welcome to the modulus evaluator")
    # print("You will need to enter the modulo and the top range.")
    # while True:
    #     modulo = input("Enter a modulus integer: ")
    #     top_range = input("Enter the top of the range: ")
    #     display_results(int(modulo), int(top_range))

    #     go_on = input("Generate another ('n' to exit): ")
    # for i in range(0,5):':
    #     print("\nRun #{}".format(i))
    #     display_random_results()

    for i in range(0,5):
        print("\nRun #{}".format(i))
        display_random_results()

    
    display_results()    