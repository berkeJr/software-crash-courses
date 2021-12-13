# Python Inheritance

"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

"""

# Create a parent class: Any class can be a parent class, so the syntax is the same as creating any other class:

class Person: 
    def __init__(self, fname, lname):  # properties: firstname and lastname 
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# We use the Person class to create an object, and then execute the printname method:
person1 = Person("John", "Doe")

person1.printname()


# Create a child class. 

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class

# Use the pass keyword when you do not want to add any other properties or methods to the class.
class Student(Person):  # Child: Student  / Parent: Person 
    pass  # Now the Student class has the same properties and methods as the Person class.


student1 = Student("Berke", "Sayın")

student1.printname()


# Create another child class:
class Worker(Person):  # Child: Worker  / Parent: Person
    # We want to add the __init__() function to the child class (instead of the pass keyword).
    # When we add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname, email):  
        self.firstname = fname
        self.lastname = lname
        self.email = email

    def workerInfo(self):
        print(self.firstname, self.lastname, self.email)

worker1 = Worker("Ahmet", "Sayın", "test@test.com")

worker1.workerInfo()
    

# Create another child class: 
class Teacher(Person): 
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Teacher("Mike", "Olsen")
x.printname()


# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Instructor(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Instructor("Johnathan", "Owen")
x.printname()