#!/usr/bin/env python3
"""
builtin 'range' function returns a list
of numbers

range(3) ==> [0, 1, 2]

range(count) 
count of numbers starting at 0
"""
print('range(3):')
for n in range(3):
    print(n)


"""
range(start, count)
start at 0
"""
print('range(10, 20):')
for n in range(10, 20):
    print(n)

"""
range(start, count, step)
"""
print('range(1, 20, 2):')
for n in range(1, 20, 2):
    print(n)
