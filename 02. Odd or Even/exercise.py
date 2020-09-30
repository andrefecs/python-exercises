"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

Extras:
If the number is a multiple of 4, print out a different message.
"""

try:
    user_number = int(input("Give me an integer number: "))
    
    user_number = abs(user_number)

    if user_number % 4 == 0:
        print("Your number is even and divided by 4.")
    elif user_number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

except ValueError:
    print("That's not an integer number!")
