print('----------Python Tuples----------')

# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets*.

thistuple=("chandan","mohan","roahan","sanjay","dayalal")

print(thistuple)


# *Tuples can also be created without the parentheses:

thistuple = "apple", "banana", "cherry"
print(thistuple)

# allow duplicates values

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# tuple length

print(len(thistuple))

# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.


thislist=('orange',)
print(thislist)

#NOT a tuple
thistuple = ("apple",)
print(type(thistuple))

# Create an Empty Tuple
thistuple = ()
print(type(thistuple))


# Tuple Items - Data Types
# Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Python - Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[2])


# Negative Indexing
# Negative indexing means start from the end.

# -1 refers to the last item, -2 refers to the second last item etc.

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[4:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# Python - Update Tuples


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple

x=('radha','rani','ram','anand')

print(x)

# x[1]='ray'  // throw error because tuple is ordered,unchangagble and allow duplicated values
print(x)


y=list(x)

y[1]='chandan'

x=tuple(y)

print(f"y list here {y}")
print(f" x tuples here {x}")


# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
# del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


# Python - Unpack Tuples

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Packing a tuple:

fruits = ("apple", "banana", "cherry")

(green,yellow,red)=fruits

print(green)
print(yellow)
print(red)

print('----------asterisk use----------------')

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


print('------------------------------')
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Python - Loop Tuples

thistuples=('ram','shyam','anand','hariom','rani','rajani','richa')

print(len(thistuples))

print('-------------range----------')

for x in thistuples:
  print(x)

for i in range(len(thistuples)):
  print(thistuples[i])


# ----------------join tuples------------

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# ---------------multiply tuples----------

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)