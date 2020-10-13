#!/usr/bin/env python3

"""
lists in python is an order collection of items.
The items can be of various / different types.
list can even contain other lists. i.e. list of lists.
"""
# create a list with 3 items
# list_name = [item1, item2, item3]

# create empty list
# list_name = []

fruits = ["apple", "orange", "melon"]
emptylist = []


def print_fruits():
    print("Fruits:")
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])


print_fruits()
print("empty basket {}".format(emptylist))

fruits[0] = "zzzzzz"
print('changed first item of fruits list to "grapes"')
print_fruits()

# will print IndexError
# print("accessing beyond the last element {}".format(fruits[3]))

"""
accesing elements using negative indexes

l = [1, 2, 3, 4, 5]

|---------|-------------|
|  index  |  neg index  |
|---------|-------------|
| 0 => 1  | -1 => 5     |
| 1 => 2  | -2 => 4     |
| ....       .....      |
|---------|-------------|

fruits[-1] would be the last element => melon
fruits[-2] would be the 2nd last element => orange
fruits[-3] would be the 3rd last element => apple
"""


def print_fruits_negindex():
    print("Fruits (neg index):")
    print(fruits[-1])
    print(fruits[-2])
    print(fruits[-3])


print("Printing fruits using negative index")
print_fruits_negindex()
