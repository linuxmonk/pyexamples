#!/usr/bin/env python3 
"""
There are ways to sort -
1. Use 'sorted' builtin
2. Use [].sort method
"""

nums = [2, 4, 1, 20, 39, 19, 18, 17, 22, 23, 28]
print('original list {}'.format(nums))

print('sorting using builtin "sorted"')
sorted_nums = sorted(nums)
print('sorted list {}'.format(sorted_nums))

print('sorting using ".sort()"')
nums.sort()
print('sorted list {}'.format(nums))
