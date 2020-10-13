#!/usr/bin/env python3
"""
dictionary holds key value pair
aka associative array or hash tables

dict_name = {key1: val1, key2: val2, .... keyN: valN}
"""

contacts = {"A": "0930-9492011", "B": "0890-0384912"}
print("contacts dictionary: {}".format(contacts))

print("contact: A - {}".format(contacts["A"]))
print("contact: B - {}".format(contacts["B"]))

contacts["C"] = "0980-1249301"
print("contacts dictionary after adding 'C': {}".format(contacts))

contacts["A"] = "0123-456789"
print("contacts dictionary after updating  'A': {}".format(contacts))

print("length of a dictionary: {}".format(len(contacts)))

del contacts["C"]
print("contacts dictionary after deleting 'C': {}".format(contacts))

mcontacts = {"Ketan": "080-12345698", "Abhishek": ["080-994002912", "080-993883123"]}
print("mcontacts: {}".format(mcontacts))

print('check if key exists ("Ketan") - {}'.format("Ketan" in mcontacts.keys()))
if "Abhishek" in mcontacts.keys():
    print("Found 'Abhishek' in the contacts")

print("Iterating over mcontacts loop")
for k in mcontacts:
    print("Name: {}, Phone: {}".format(k, mcontacts[k]))

print("Iterating over mcontacts loop key, value variant")
for k, v in mcontacts.items():
    print("Name: {}, Phone: {}".format(k, v))

phonebook = {
    "Ketan": {"Phone": "020-99889388", "Email": "ketan@gmail.com"},
    "Abhi": {"Phone": "080-9878342", "Email": "abhi@gmail.com"},
}
for contact in phonebook:
    print("Contact Name...........{}".format(contact))
    print("Contact Phone..........{}".format(phonebook[contact]["Phone"]))
    print("Contact Email..........{}".format(phonebook[contact]["Email"]))
