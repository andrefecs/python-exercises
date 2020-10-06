"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner.
Ask if the players want to start a new game).

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""



print ("\nHi! Welcome to the Rock-Paper-Scissors game!\n\nInvite your best friend and get ready to have lots of FUN!")

game_control = input("\nAre you ready? Type 'yes' to start playing or 'no' to quit: ")

def player_input_verification(player_input):
    player_input = player_input.lower()
    while player_input != "rock" and player_input != "paper" and player_input != "scissors":
        player_input = input("Typo? Type again: ")
    return player_input
    
    

while game_control != "yes" and game_control != "no":
    game_control = input ("Typo? Type 'yes' to start playing or 'no' to quit: ")


while game_control != "no":
    print ("\nMake sure you choose between: rock, paper or scissors!\n")
    
    #player one
    
    player_one = input("Player One: ")
    player_one = player_input_verification(player_one)
    
    #player two
    player_two = input("Player Two: ")
    player_two = player_input_verification(player_two)

    #result
    if  player_one == player_two:
        print("\nTIE!\n")
    
    elif player_one == "rock" and player_two == "paper":
        print("\nPlayer two WIN!\n")

    elif player_one == "rock" and player_two == "scissors":
        print("\nPlayer one WIN!\n")
    
    elif player_one == "paper" and player_two == "rock":
        print("\nPlayer one WIN!\n")
    
    elif player_one == "paper" and player_two == "scissors":
        print("\nPlayer two WIN!\n")

    elif player_one == "scissors" and player_two == "rock":
        print("\nPlayer two WIN!\n")

    elif player_one == "scissors" and player_two == "paper":
        print("\nPlayer one WIN!\n")

    game_control = input("\nDo you want to start a new game? Type 'no' to quit: ")

print ("\n----Thanks for playing!----")

