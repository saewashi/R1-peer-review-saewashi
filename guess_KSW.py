#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

#Variables
guess = 0
guesses = 0

range_low = 1
range_high = 20

# Intro to the game, and welcoming the player.
print("Welcome to Guess a Number!")



# Random ranges for the user to guess between
number = random.randrange(range_low, range_high)


# Assigning guess to be converted into int, and asking for the users input

while guess != number:
    try: 
        guess = int(input(f"Please Guess a number between {range_low} and {range_high}: "))
        guesses = guesses + 1

    # Sees if the user's guesses are too low, too high, or the correct answer.
        if guess < number:
            print('Too Low! Guess again.')
        elif guess > number:
            print("Too High! Guess again.")
        else:
            print("You got it! Great job!")
    except:
        print('Please guess a number.')



#Prints the number of guess/tries it took the user to guess.
print("Number of guesses:", guesses)

# Bonus Material
# Asks user for the bonus question
print("Bonus Question: What's my age?")


# Set age number. . .Just pretend not to see that. :)
number = 20


# Assigning guess to be converted into int, and asking for the users input

while guess != number:
    try:
        guess = int(input("Please Guess my age: "))
        guesses = guesses + 1

    # Sees if the user's guesses are too low, too high, or the correct answer.

        if guess < number:
            print('Nope! Too low. Guess again.')
        elif guess > number:
            print("Nope! Too high Guess again.")
        else:
            print("You got my age! Great job!")
    except:
        print("Please choose a number.")