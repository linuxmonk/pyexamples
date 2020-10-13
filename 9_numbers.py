#!/usr/bin/env python3

# use numbers in the source code as is without quotes
# integers
# floating point

# numeric operations
# + add
# - subtract
# * multiply
# / divide
# ** exponentiate
# % modulo

print("2 ** 4: {}".format(2 ** 4))
m = 9 % 3
print("9 % 3: {}".format(m))

fpnum = 8 / 2
print("8 / 2 (division returns a floating point result): {}".format(fpnum))

# int builtin converts something to int
quantity_string = "5"
total = int(quantity_string)
print("quantity string {0} to int('{0}') -> {1}".format(quantity_string, total))

float_qty = 5.2
total = int(float_qty)
print("float quantity {0} to int({0}) -> {1}".format(float_qty, total))

# to convert something to float using 'float' builtin
fp_string = "3.1415"
pi = float(fp_string)
print("pi string {0} to float({0}) is {1}".format(fp_string, pi))
