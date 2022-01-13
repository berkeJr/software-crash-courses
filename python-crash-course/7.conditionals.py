# If/ Else conditions are used to decide to do something based on something being true or false

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword

"""

# Simple if
x = 21
y = 20

if x > y:
  print(f'{x} is greater than {y}')    # it prints 21 is greater than 20

# If/else
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{y} is greater than {x}')  

# if/elif/else 
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')  
else:
  print(f'{y} is greater than {x}')

# Nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')



# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x in numbers:
  print(x in numbers)  # x = 21  / returns false

# not in
if x not in numbers:   
  print(x not in numbers)   # x = 21  /  returns true


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is

"""
The is keyword is used to test if two variables refer to the same object.

The test returns True if the two objects are the same object.

The test returns False if they are not the same object, even if the two objects are 100% equal.

"""

# Example 1

a = ["apple", "banana", "cherry"]

b = a

print(a is b)  # returns true

# Example 2

c = ["apple", "banana", "cherry"]

d = ["apple", "banana", "cherry"]

print(c is d)  # returns false


# Example 3

x = 20 
y = 21

# is
if x is y:
  print(x is y)  # returns false

# is not 
if x is not y:
  print(x is not y)  # returns true