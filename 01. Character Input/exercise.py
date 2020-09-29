"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
from datetime import datetime
now = datetime.now()

name = input("Give me your name: ")
age = int(input("Give me your age (don't be shy): "))
current_year = now.year

if age <= 100:
    hundreth_year = (100 - age) + current_year
    print("Hi {}, you'll be 100 years old in {}.".format(name, hundreth_year))
else:
    hundreth_year = current_year - (age - 100)
    if  hundreth_year > 0:
        print("Hi {}, you're probably dead and turned 100 years old in {}.".format(name, hundreth_year))
    else:
        hundreth_year = abs(hundreth_year)
        print("Hi {}, you're probably dead and turned 100 years old in {} a.C.".format(name, hundreth_year))
        
        
