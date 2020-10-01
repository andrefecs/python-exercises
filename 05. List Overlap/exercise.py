"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this.
"""

#generating two random lists
import random
from tabulate import tabulate

random_list_a = []
random_list_b = []

for i in range(0,30):
    n = random.randint(1, 100)
    random_list_a.append(n)
    m = random.randint(1, 100)
    random_list_b.append(m)

random_list_a.sort()
random_list_b.sort()

table = [["List A", random_list_a], ["List B", random_list_b]]

print ("Generated lists:\n" + tabulate(table))

#generates a new list with the common elements
common_elements = []

for x in random_list_a:
    if x in random_list_b:
        common_elements.append(x)

#removing duplicates
common_elements = list(dict.fromkeys(common_elements))

print ("Common elements: {}".format(common_elements))