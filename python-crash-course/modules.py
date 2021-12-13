# A module is basically a file containing a set of functions to include in your application. 

# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules.

# We can also create our own modules. 

"""
Python Modules: 

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

"""

# How to import core python module: (date/time module)

# Example: Core module
import datetime 

today = datetime.date.today()
# date object is in datetime

print(today) 


# Another example: core module 
from datetime import date 

today = date.today()

print(today)


# Another example: Core module 
import time 

timestamp = time.time()

print(timestamp)


# Another example:  Core module 
from time import time 

timestamp = time()

print(timestamp)


# Python has package manager called Pip. We can install external packages from Pip.  

# We installed camelcase module from terminal using pip install camelcase method. 

# Pip module
from camelcase import CamelCase 
# camelcase module'den CamelCase fonksiyonunu import ettik. 

c = CamelCase()

print(c.hump('hello there world'))  # it outputs Hello There World.


# Create a custom module and import that. 
# We have a file named validator.py. We created it earlier. It validates an email. 

import validator  # validator file'ı import ettik

from validator import validate_email  # validator file içindeki validate_email fonksiyonunu import ettik

email = 'test@test.com'

if validate_email(email):
    print('Email is valid.')
else:
    print('Email is bad.')

