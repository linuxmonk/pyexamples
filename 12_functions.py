#!/usr/bin/env python3

"""
Functions

def function_name():
    # code block

To call a function -

function_name()

NOTE: A function has to be defined before it is called.
"""


def say_hello():
    print("Hello")


say_hello()


def say_hi(name):
    print("Hi {}".format(name))


say_hi("Sai")
say_hi("everybody")

# say_hi()
# would result in build error as positional argument is missing


def say_hi2(name="there"):
    print("Hi {}!".format(name))


say_hi2()
say_hi2("Sai")
say_hi2("everybody")


def say_hi3(first, last):
    print("Hi {}, {}!".format(last, first))


say_hi3("Sai", "Kiran")
say_hi3(last="Gummaraj", first="Sai Kiran")


def say_hi4(first, last="<None>"):
    """
    This function says hello to the person
    whose name is passed in as arguments
    """
    print("Hi {} {}!".format(first, last))


say_hi4("Sai")
say_hi4("Sai", "Kiran")
