# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Brad'
age = 37

# Concatanate: Inserting a variable into a string. 
# print("My name is" + " " + name + " and I am " + str(age))

# String Formatting

# Arguments by position
print("My name is {name} and I am {age}".format(name=name, age=age))

# F-strings
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string: only first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case: küçük harfleri büyük, büyük harfleri küçük yapar.
print(s.swapcase())

# Get length: string'deki karakter sayısı
print(len(s))

# Replace: string'deki bir kelimeyi farklı bir ifadeyle değiştirir. 
print(s.replace('world', 'everyone'))

# Count: seçilen karakteri sayar
sub = 'h'
print(s.count(sub))

# Starts with: seçili kelime ya da karakter ile başladığını kontrol eder
print(s.startswith('hello'))

# Ends with: seçili kelime ya da karakter ile bittiğini kontrol eder
print(s.endswith('d'))

# Split into a list: kelimeleri array listesine ayırır. 
print(s.split())

# Find position: seçili karakterin sırasını bulur.
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())



