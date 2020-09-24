#!/usr/bin/env python3

"""
for item in list_name:
    # code block
"""

fruits = ['apple', 'banana', 'pineapple']
print("Looping through fruits:")
for fruit in fruits:
    print(fruit.title())


"""
while condition:
    # code block
"""

n = 10
i = 0
l = [2, 4, 6, 8, 10, 12, 14]
print('Finding {} in a list of {} items and printing the position'.format(n, l))
found = False
while found == False:
    if n == l[i]:
        found = True
    i = i + 1

if found:
    print('Found {} in {} position'.format(n, i))
else:
    print('{} not found'.format(n))
