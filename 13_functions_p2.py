#!/usr/bin/env python3

"""
The first line after the function definition is the 
docstring
"""

def odd_or_even(number):
    """Determine if the number is an odd or even number"""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print('20 odd / even: {}'.format(odd_or_even(20)))

def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

print('20 is odd: {}'.format(is_odd(20)))
