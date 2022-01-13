# A List is a collection which is ordered and changeable. Allows duplicate members.


"""
List at Python: it is very similiar to an array.

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.

Lists are created using square brackets:

"""
# Create List: Usage 1
numbers = [1, 2, 3, 4, 5, 6]

# Crate List : Usage 2 
numbers2 = list((1, 2, 3, 4, 5, 6))

print(numbers, numbers2)

# A list of strings
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get a single value from a list
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Get the last value
print(fruits[-1])

# Get length
print(len(fruits))

# Append to list: Add new item to the list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list: alphabetically
fruits.sort()

# Reverse sort: alphabetically reverse
fruits.sort(reverse=True)

print(fruits)
