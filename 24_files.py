#!/usr/bin/env python3

"""
open a file using builtin 'open()' function
"""

# cat the contents of a file
filename = "1_hello.py"
print("Read contents from {} and write to screen".format(filename))
helloworld = open(filename)
contents = helloworld.read()
print(contents)

"""
read returns the entire contents of the file
"""

"""
seek(offset) resets the file pointer to the offset
tell() returns the current offset/position in the file
"""

print("Read more contents from {}".format(filename))
morecontents = helloworld.read()
print(morecontents)
print("current file pointer position is {}".format(helloworld.tell()))

"""
read part of a file using read(N)
where N is number of bytes
"""
helloworld.seek(0)
magicbytes = helloworld.read(2)
print("helloworld.read(2) returns type {}".format(type(magicbytes)))
print("magicbytes: {}".format(magicbytes))

"""
close the file
"""
helloworld.close()
