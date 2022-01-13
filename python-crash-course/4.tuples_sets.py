# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, 
all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor: Create tuple: Usage 2
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',) # if we don't put a comma, it is done string by default. 

print(fruits, fruits2)

print(fruits[1])

# Get value from a tuple
print(fruits[1])

# We Can't change value at tuple
fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length of tuple 
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

"""
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, 
all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

"""

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set: it just clear items. Set still appears.
fruits_set.clear()

# Delete set: it deletes set and items entirely.
del fruits_set

print(fruits_set)