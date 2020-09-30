"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 10.

Extras:

- Instead of printing the elements one by one, make a new list that has all the elements less than 10 from this list in it and print out this new list.

"""

given_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for x in given_list:
    if x < 10:
        new_list.append(x)   
    
print(new_list)