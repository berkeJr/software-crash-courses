# Python has functions for creating, reading, updating, and deleting files.

"""
File Handling

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"""


# Open a file: open() funciton will create the file and w for writing
myFile = open('myfile.txt', 'w')

# Get some info
print("Name: ", myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode', myFile.mode)

# Write to file: 
myFile.write('I love Python and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like C#')

# Read from file: 
myFile = open('myfile.txt', 'r')
text = myFile.read(100)
print(text)