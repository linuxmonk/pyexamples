#!/usr/bin/env python3

"""
Tuple is an immutable list

tupname = (v1, v2, ..., vN)
-or-
tupname = (v1,)
"""

months = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)
print("Months: {}".format(months))

for month in months:
    print("Month: {}".format(month))

print("First Month: {}".format(months[0]))

# throws 'TypeError' tuple object does not support assignment
# months[2] = 'February'

months_cp = months

# delete a tuple using 'del'
del months
# NameError - 'months' not defined
# print("Months: {}".format(months))

"""
Convert tuple to list using 'list()' builtin
'type()' builtin returns the type of an object
"""
months = months_cp
months_list = list(months)
print("months of type {} is - {}".format(type(months), months))
print("months_list of type {} is - {}".format(type(months_list), months_list))

"""
iterate a tuple
"""
print("Iterating months tuple")
for month in months:
    print(month)

"""
assigning multiple values of a tuple to multiple variables
at once
"""
point2d = (3, 4)
(x, y) = point2d
print("2-dimensional point x = {}, y = {}".format(x, y))


"""
assigning multiple values of a list into multiple variables
at once
"""
legobricks = ["1x1", "1x2", "2x2"]
(onepeg, twopegs, fourpegs) = legobricks
print("one peg lego {}".format(onepeg))
print("two peg lego {}".format(twopegs))
print("four peg legos {}".format(fourpegs))


"""
tuple multiple assignment in for loop
"""
print("print shape co-ordinates by looping a list of point tuples")
shape = [(2, 3), (4, 6), (7, 9), (10, 15), (2, 3)]
for (x, y) in shape:
    print(x, y)
