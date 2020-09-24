#!/usr/bin/env python3

if 27 < 30:
    print('Twenty seven is less than thirty')

"""
Code blocks are represented by indentation. Most common
indentation is 4 spaces in python. Though you can choose
other length
"""

age = 31
if age > 35:
    print('You are old enough to be the President')
else:
    print('You are not old enough to be the President')

print('Have a nice day!')

user_input = input('Enter your age:')
age = int(user_input)
if age > 35:
    print('You are old enough to be a Senator or the President')
elif age > 30:
    print('You are old enough to be a Senator')
else:
    print('You are not old enough to be a Senator or the President')

print('Have a nice day!')
