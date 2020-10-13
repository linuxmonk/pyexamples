#!/usr/bin/env python3

# print supports string format using {} as location
# specifiers

print("I {} Python.".format("love"))
print("{} {} {}".format("I", "Love", "Python."))
print("{} {} {} {}.".format("I", "Love", "Python", 3))

# Use {N} where N specifies the location of the format
# specifier starting at 0 for the first one
print("I {0} {1}. {1} {2} {3}".format("Love", "Python", "Loves", "Me"))
print()

# Using format specifiers to create table
# {N:M}, where
#  N - position number 0 and upwards
#  M - minimum number of characters
print("{0:8} | {1:8}".format("Fruit", "Quantity"))
print("{0:8} | {1:8}".format("Apple", 3))
print("{0:8} | {1:8}".format("Orange", 10))
print()

# Using format specifiers with justification (left <, right >)
print("{0:8} | {1:<8}".format("Fruit", "Quantity"))
print("{0:8} | {1:<8}".format("Apple", 3))
print("{0:8} | {1:<8}".format("Orange", 10))
print()

# Format strings - Data Types
# f     Float
# .Nf   N = The number of the decimal places
# {:.2f} number with two decimal places
print("{0:8} | {1:8}".format("Fruit", "Quantity"))
print("{0:8} | {1:8.2f}".format("Apple", 2.33333))
print("{0:8} | {1:8.2f}".format("Orange", 1.2))
print()
