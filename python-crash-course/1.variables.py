# A variable is a container for a value, which can be of various types


# Multi-line comments usage 1
'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

# Multi- line comment usage 2
"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Creating variables:
# x = 1  # in python there is no semi-colons and we don't have to add variable type before it's name (int, var) this is int by default

# y = 2.5 # float

# name = 'John' # str

# is_cool = True # boolean

# Multiple variables assignment
x, y, name, is_cool = (1, 2.5, 'John', True)


# print function
print('Hello')

print(x)

print(x, y, name, is_cool)

# Basic math
a = x + y

print(a)

# Changing a variable's type / Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z))

print("berke")