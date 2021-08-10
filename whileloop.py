#while loop : continue working/happen until a certain condition is met.
#use this for the login system

#magic_word = "Please"input_user = input("What is the magic word?")

# == equal != not equal
#while input_user == magic_word:
    #input_user = input("What is the magic word?")

#print("You're Welcome")


#import randrage
from random import randrange
#get a random number
random_number = randrange (1,100)

guess = input("Guess a number between 1 and 100: ")
#typecast to int
guess = int(guess)

while random_number != guess:
    print(guess, "is not the one!")
    if random_number < guess:
        print("The random number is lower than", guess)
    
    if random_number > guess:
        print("The random number is higher than", guess)
    
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
#print number 
print("Well done! The number was", random_number)