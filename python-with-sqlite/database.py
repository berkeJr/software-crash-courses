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

# ------------------------------------------------------------------------------------------------------------------------

# We will use this cursor to do all kind of things.

###### CREATE TABLE

# Create a table: Notes: Sqlite data types: NULL, INTEGER, REAL(decimal numbers), TEXT, BLOB(images, mp3 files and such kind of datas.) 
# c.execute(""" CREATE TABLE customers( 
#             first_name text,
#             last_name text,
#             email text
#           )""")

# ------------------------------------------------------------------------------------------------------------------------


######  INSERT INTO: SINGLE RECORD

# Create another cursor command to insert a record inside the table
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@test.com')")
# c.execute("INSERT INTO customers VALUES ('Berke', 'Sayin', 'berke@test.com')")
# c.execute("INSERT INTO customers VALUES ('Mehdi', 'Ay', 'mehdi@test.com')")
# c.execute("INSERT INTO customers VALUES ('Hamza', 'Gunduz', 'hamza@test.com')")
# c.execute("INSERT INTO customers VALUES ('Selcuk', 'Yilmaz', 'selcuk@test.com')")
# c.execute("INSERT INTO customers VALUES ('Samet', 'Can', 'samet@test.com')")
# c.execute("INSERT INTO customers VALUES ('Sami', 'Ince', 'sami@test.com')")
# c.execute("INSERT INTO customers VALUES ('Hasan', 'Ozdogan', 'john@test.com')")

# ------------------------------------------------------------------------------------------------------------------------

######   INSERT INTO: MULTİPLE RECORDS

# If we want to add multiple records: 
# many_customers = [('Wes', 'Brown', 'wes@test.com'), 
#                   ('Steph', 'Kuewa', 'steph@test.com'), 
#                   ('Ahmet', 'Sayin', 'ahmet@test.com'),
#                  ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# ------------------------------------------------------------------------------------------------------------------------

######   DATABASE QUERY: SELECT

# Query Database
# c.execute("SELECT rowid, * FROM customers") #with id's
#c.execute("SELECT * FROM customers WHERE last_name = 'Sayin'")  == use where clause

# c.fetchone()     == 1 item from the table
# c.fetchmany(3)   == 3 items from the table
# print(c.fetchall())     # == all items from the table

# items = c.fetchall()

# for item in items:
#     print(item)

# ------------------------------------------------------------------------------------------------------------------------

######   DATABASE QUERY: Update

c.execute(""" UPDATE customers SET first_name = 'Burak' 
            WHERE last_name = 'Gunduz'
""")

c.execute("SELECT  * FROM customers")


# print all records ar the screen as items
items = c.fetchall()

for item in items:
    print(item)



# we need to commit our command
conn.commit()

# close our connection 
conn.close()