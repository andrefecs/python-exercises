"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

try:
    user_number = int(input("Give me a number and I'll give you a list of all the divisors of it: "))
    
    abs_user_number = abs(user_number)
    
    range_list = range(1, abs_user_number + 1)

    divisors_list = []

    for elem in range_list:
        if abs_user_number % elem == 0:
            divisors_list.append(elem)
    
    print("Divisors of {}: {}".format(user_number, divisors_list))


except ValueError:
    print("You didn't give me a number!")