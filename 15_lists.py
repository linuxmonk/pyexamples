#!/usr/bin/env python3

"""
appending to the list is done using append function
"""

print('create a list of 3 fruits')
fruits = ['apple', 'banana', 'grapes']
print(fruits)


print('append melon to it')
fruits.append('melon')
print(fruits)

"""
appending a list to another list using extend
"""
print('create a veggie list')
veggies = ['beans', 'cabbange']

shoppinglist = fruits
shoppinglist.extend(veggies)
print('append veggie to fruits list')
print(shoppinglist)

shoppinglist.insert(0, 'milk')
print('inserted milk to shopping list')
print(shoppinglist)

shoppinglist.insert(2, 'curd')
print('inserted curd in position 2 of shopping list')
print(shoppinglist)

"""
Slice is a part of a list.
Denoted by [n:m]
Where n is the starting position
      m is the count from the beginning of the list

which is in index represents the number m-1
"""
part = shoppinglist[1:4]
print("shoppinglist[1:4] => {}".format(part))
print("shoppinglist[0:2] is same as shoppinglist[:2] => {}".format(shoppinglist[0:2]))

"""
last two items of the list
"""
print("+ indexing: last two items of the shopping list => {}".format(shoppinglist[len(shoppinglist)-2:]))
print("- indexing: last two items of the shopping list => {}".format(shoppinglist[-2:]))


"""
string as slices (String Slices)
"""
phrase = 'test phrase'
print('part of phrase "{}" [1:3] => "{}"'.format(phrase, phrase[1:3]))
