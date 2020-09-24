#!/usr/bin/env python3

"""
Accessing an element in the list that isn't there or out-of-bounds
would give exceptions. Python has 'try' 'except' block.
"""

fruits = ['apple', 'banana', 'berries', 'melon']
iwant = 'pineapple'

try:
    juice = fruits[iwant]
except:
    juice = 'sorry we dont have the {} fruit you asked for'.format(iwant)

print(juice)
