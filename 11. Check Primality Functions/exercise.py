"""
Ask the user for a number and determine whether the number is prime or not.
"""


try:
    user_number = int(input("Give me a number: "))
    
    abs_user_number = abs(user_number)
    
    range_list = range(2, abs_user_number + 1)

    divisors_list = []

    for elem in range_list:
        if abs_user_number % elem == 0:
            divisors_list.append(elem)
    
    if len(divisors_list) == 1:
        print("\n{} is prime!\n".format(user_number))
    else:
        print("\n{} is NOT prime!\n".format(user_number))
        print("Divisors of {}: {}".format(user_number, divisors_list))


except ValueError:
    print("You didn't give me a number!")