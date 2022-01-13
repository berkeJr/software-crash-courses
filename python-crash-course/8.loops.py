# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
it outputs: apple, banana, cherry

"""

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
  print(f'Current Person: {person}')  # Sırasıyla alt alta dizinin elemanlarını yazar

# Break keyword in loops 
for person in people:
  if person == 'Sara':  
    break  # Sara'ya gelene kadar olan elemanları yazar, Sara'ya gelince onu yazmadan döngüyü bitirir.
  print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sara':  
    continue   # Sara'ya gelince dögünün başına döner ne next elemana geçer, Sara'yı yazmaz.
  print(f'Current Person: {person}')

# range
for i in range(len(people)):
  print(people[i])   # Elemanları tek tek alt alta yazar. 

for i in range(0, 11):
  print(f'Number: {i}')   # 0'dan 10'a kadar olan sayıları tek tek alt alta ekrana yazar. 


# While loops execute a set of statements as long as a condition is true.

"""
i = 1
while i < 6:
  print(i)
  i += 1
1'den 5'e kadar tüm sayıları alt alta ekrana yazar. 

"""

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1    # 0'dan 9'a kadar tüm sayıları ekrana yazar. 