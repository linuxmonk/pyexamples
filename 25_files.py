#!/usr/bin/env python3
"""
automatically close a file using 'with'
"""

filename = "1_hello.py"
with open(filename) as helloworld:
    print("is the file {} closed? {}".format(filename, helloworld.closed))
    print("contents:")
    print("---------")
    print(helloworld.read())
    print("---------")

print("file operation on {} complete. is file closed? {}".format(filename, helloworld.closed))

"""
to read one line at a time there are two ways -

1. use fp.readline()
2. with open('filename') as file:
    for line in file:
        print(line)
"""

print("cat the contents of the file '{}'".format(filename))
with open(filename) as pyfile:
    for line in pyfile:
        print(line.rstrip())

"""
open files in different modes 
open(filename, mode)

modes:
    r - open in read mode (default)
    w - open in write mode. truncate first
    x - create a new file and open it for writing
    a - open file for writing appending to it

    + - read and write to the same file
    b - binary mode
    t - text mode (default)
   
   fp = open('/pictures/pic.jpg', rb)
   fp.mode # gives the mode of the file
"""

print("writing something about a cat in cat.txt")
with open("cat.txt", "w") as txtfile:
    txtfile.write("cat is a pet animal\n")
    txtfile.write("i like dogs too\n")

print("reading cat.txt")
with open("cat.txt") as rtxtfp:
    print(rtxtfp.read())


"""
Use exceptions when dealing with file operations
"""
nofname = "nofile.txt"
try:
    print("opening nofile.txt")
    fp = open(nofname)
    print("opeened nofile.txt, reading contents")
    contents = fp.read()
except:
    print("file does not exist!")
