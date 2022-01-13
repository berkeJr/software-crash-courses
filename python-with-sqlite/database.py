import sqlite3 # we need to import sqlite in order to use it. 

# connection to the database

# there are 2 ways. either you create a db or you use a db that already exists.

# use a db in memory:
# conn = sqlite3.connect(':memory:')  # connects to a db in memory 


# here is to create a db. 
# first, create a variable and then use the connect() method. parantez içine database adı yazılır.
conn = sqlite3.connect('customer.db') 
