# A function is a block of code which only runs when it is called. 

# In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# A function can return data as a result.

"""
Creatig and calling a function 

def my_function():
  print("Hello from a function")

my_function()

def keyword is used to define the function

"""

# Create function with def keyword
def sayHello(name):
    print(f'Hello {name}')  # F-strings

# Call function
sayHello('Berke Sayın')


# Example (deafult parameter is used if no argument is written calling the function )
def sayHello(name="Sam"):
    print(f'Hello {name}')  # F-strings

sayHello() # it prints Hello Sam


# return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3, 4))    




# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

"""
a'ya 10 ekleyen lambda function
x = lambda a: a + 10
print(x(5))


a ile b'yi çarpan lambda function       
x = lambda a, b : a * b
print(x(5, 6))

"""

getSum = lambda num1, num2 : num1 + num2 

print(getSum(15,25))