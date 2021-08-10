#make a list. Guess the power_ranger
from random import random, randrange
power_rangers = [ "Red", "Yellow", "Green", "Blue", "Black", "Pink"]
random_number = randrange (6)
random_ranger = power_rangers[random_number]

print("I'm thinking of a Power Ranger. Can you guess?")
input_ranger = input ("Which color do you think I have in mind?")

number_of_guesses = 1

while input_ranger != random_ranger:
    print("No", input_ranger, "is not the one!")
    input_ranger = input("Which one do you think now?")
    # can use this for the login system to throw them out whenever they have tried it too many times
    number_of_guesses = number_of_guesses + 1

print("Yes", input_ranger, "is the correct power ranger, well done! It took you", number_of_guesses, "guesses")