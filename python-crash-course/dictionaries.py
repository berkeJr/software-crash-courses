# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

"""
Dictionary at Python

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

Dictionary in Python is very similar to object literal at JavaScript.

"""

# Create a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor to create a dictionary
# person2 = dict(first_name='Sara', last_name='Williams')

print(person, type(person))

# Get a value from dictionary
print(person['first_name'])
print(person.get('last_name')) # with get() function

# Add key/value to dictionary
person['phone'] = '555-555-5555'

# Get dictionary keys
print(person.keys())

# Get dictionary items: each key/value pair is an item.
print(person.items())

# Copy dictionary to create another same d,ctionary
person2 = person.copy()
person2['city'] = 'Boston'  # Add key/value to dictionary (person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length: how many key/value pairs
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])

print(people)