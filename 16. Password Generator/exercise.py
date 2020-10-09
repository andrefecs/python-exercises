"""
Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random

def main(strength):
    if strength == "strong":
        generated_password = str()
        while len(generated_password) < 10:
            a = str(random.choice("@!#$%&-"))
            b = str(random.randrange(10))
            c = str(random.choice("abcdefghijklmnopqrstuvwxyz")).upper()
            d = str(random.choice("abcdefghijklmnopqrstuvwxyz"))
            generated_password = generated_password + a + b + c + d

        l = list(generated_password)
        random.shuffle(l)
        generated_password = ''.join(l)

    elif strength == "weak":
        list_of_words = ["time", "third", "pickle", "cow", "exultant", "idea", "circle", "workable", "trace"]
        generated_password = random.choice(list_of_words)

    return generated_password

print("\n---Welcome to the greatest Password Generator!---\n")

try: 
    user_choice = str(input("Please tell me how strong you want your password to be (weak or strong): "))
    
    while user_choice != "weak" and user_choice != "strong":
        user_choice = str(input("Please tell me how strong you want your password to be (weak or strong): "))
    
    result = main(user_choice)
    print("\nGenerated password: {}\n".format(result))


except ValueError:
    print("* Not a valid choice! Please run again! *")
