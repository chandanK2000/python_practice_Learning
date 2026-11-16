print('-------------------------python funciton example--------------');

# Python Functions

# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def myname():
    return  'my name is chandan kumar'

print(myname())

def Hello(name):
    return f" myself {name} "

print(Hello("chandan"))
print(Hello("mohan"))
print(Hello("sohan"))
print(Hello("roahn"))

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Keyword Arguments

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.

# However, positional arguments must come before keyword arguments:

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


def myfunctions(fruits):
   for fruits in fruits:
      print(fruits)


fruits=["apple","mango","litchi","banana","orange","papaya"]
myfunctions(fruits)


# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.

# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300
  print(x)

myfunc()


# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# global scope

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Python Decorators


# Decorators let you add extra behavior to a function, without changing the function's code.

# A decorator is a function that takes another function as input and returns a new function.


# # Lambda Functions
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))