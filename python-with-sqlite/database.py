import sqlite3 # we need to import sqlite in order to use it. 

# connection to the database

# there are 2 ways. either you create a db or you use a db that already exists.

# use a db in memory:
# conn = sqlite3.connect(':memory:')  # connects to a db in memory 


# here is to create and connect to database. 
# first, create a variable and then use the connect() method. parantez içine database adı yazılır.
conn = sqlite3.connect('customer.db') 

# now, we need to create a cursor as a variable(for example: c)
c = conn.cursor()

# We will use this cursor to do all kind of things.

# Create a table: Notes: Sqlite data types: NULL, INTEGER, REAL(decimal numbers), TEXT, BLOB(images, mp3 files and such kind of datas.) 
c.execute(""" CREATE TABLE customers( 
            first_name text,
            last_name text,
            email text
          )""")

# we need to commit our command
conn.commit()

# close our connection 
conn.close()