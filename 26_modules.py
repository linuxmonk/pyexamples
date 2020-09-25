#!/usr/bin/env python3

"""
Python modules are just python files ending in '.py'.
They implement a set of attributes, methods, classes

to import a module name use 

    import module_name 

or to import just a function

    from module_name import method_name

here call just 'method_name()'

or you can import an attribute too.

"""

import time

print(time.asctime())

from math import ceil

print("ceil(2.8) = {}".format(ceil(2.8)))

"""
To look at module search path
where python loads the modules see
"""

import sys
print(sys.path)

"""
to modify the module serach path there are two ways -
1. append to the sys.path 
2. Set the PYTHONPATH environment variable
"""

print('Module path:')
for path in sys.path:
    print(path)


