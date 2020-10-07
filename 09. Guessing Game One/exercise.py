"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random

game_control = str()

print("Welcome to the Guessing Game! Get ready to have LOTS of fun!\n")

while game_control != "exit":

    try: 
        number_to_guess = random.randint(1, 9)
        user_guess = int(input("Guess a number between 1 and 9 (including both of them!): "))
        number_of_tentatives = 1

        while user_guess != number_to_guess:
            if user_guess > number_to_guess:
                print("Too high!\n")
                user_guess = int(input("Try again: "))
                number_of_tentatives += 1
            else:
                print("Too low!\n")
                user_guess = int(input("Try again: "))
                number_of_tentatives += 1

        print("\nYou're goddam right!\n")
        print("You guessed in {} tentatives!\n".format(number_of_tentatives))
        game_control = input("Want to play again? Type 'exit' to quit: ")
    
    except ValueError:
        print("Not an integer! Please try again!\n")
