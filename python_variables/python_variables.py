x=5
y="mohan"

print(x)
print(y)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Many Values to Multiple Variables

x,y,z="orange","lemon","cherry"

print(x)
print(y)
print(z)

print('--------------------------------------');


# One Value to Multiple Variables

x=y=z="lemon";

print(x)
print(y)
print(z)

print('--------------------------------------');

# Unpack a Collection

fruits=['apple','mango','litchi']

x,y,z=fruits

print(x)
print(y)
print(z)

# ============================================
# Output Variables
x='python is awesome';

print(x)

print('-------------------------------------')

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print('---------------------------------------')

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print('--------------Global Variables-------------------------')
# Global Variables


# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x='awesome'

def myfunction():
    print('python is',x)

myfunction()

print('----------------------------------');

x='Hello python'

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print('-------------The global Keyword--------');

myname="chandan kumar";

def myName():
    global name='chandan'
    print(f'my name is {myname}')
    # print(q)

myName()
print(name)
