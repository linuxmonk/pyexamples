#!/usr/bin/env python3

"""
index method returns the index of an item in the list
"""

fruits = ['apple', 'banana', 'mango']
print('fruits => {}'.format(fruits))
print('position of "mango" in the list is {}'.format(fruits.index('mango')))

# throws a 'ValueError'
print('position of "melon" in the list is {}'.format(fruits.index('melon')))
