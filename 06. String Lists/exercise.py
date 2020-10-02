"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

try: 
    user_string = str(input("Give me a string: "))
    user_string_backwards = user_string[::-1]
    user_string = user_string.lower()
    user_string_backwards = user_string_backwards.lower()

    if user_string == user_string_backwards:
        print("You gave me a palindrome!")
    else:
        print("You DID NOT give me a palindrome!")
    

except ValueError:
    print("That is not a string!")