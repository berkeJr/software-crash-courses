# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. 
 
# Almost everything in Python is an object

# Create a simple class and object. 
"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

To create a class, use the keyword class:

class MyClass:
  x = 5

print(MyClass)   // it outputs <class '__main__.MyClass'>

Now we can use the class named MyClass to create objects: // Create an object named p1, and print the value of x:

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)  // it outputs 5

The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

"""


# The __init__() Function
"""
To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when 
the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

it outputs:
John
36

"""

# Create class
class User:
    # Constructor: A constructor is a function that runs when we instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Create a method inside the class
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    # Create another method inside the class
    def has_birthday(self):
        self.age += 1  # Yaşını 1 arttıran method.


# Initialize User Object
user1 = User('Brad Traversy', 'test@test.com', 25)
print(user1.name, user1.email, user1.age)

user1.has_birthday()
print(user1.greeting())

print(type(user1))  # it outputs: <class '__main__.User'>  ---> it is an object from User class. 



# Extend Class: Inheritance
class Customer(User):  # The parameter is parent class
    # Constructor: A constructor is a function that runs when we instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    # method
    def set_balance(self, balance):
        self.balance = balance

    
# Initialize a customer object 
customer1 = Customer('Janet Johnson', 'janet@yahoo.com', 25)

customer1.set_balance(500)

print(customer1.greeting())



