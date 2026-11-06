print('------------python data types example--------------')


# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# --------------------------------------------

# 1. Numeric Types

age = 25
price = 99.50
num = 3 + 5j

print(type(age))    # <class 'int'>
print(type(price))  # <class 'float'>
print(type(num))    # <class 'complex'>

# --------------------------------------------


# 2. Text Type
# Used to store text.

# str – String

name = "Chandan Kumar"

print(name)
print(type(name))

# --------------------------------------------

# 3. Boolean Type
# Used to store True or False values.

# bool

is_employed = True
is_married = False

print(type(is_employed))

# --------------------------------------------

# 4. Sequence Types

# Used to store multiple values in an ordered collection.

# A. list

# Mutable (you can change its values).

fruits = ["Apple", "Mango", "Banana"]

print(fruits)
print(type(fruits))


# B. tuple

# Immutable (you cannot change its elements).

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))


# C. range

# Used to represent a sequence of numbers.

numbers = range(1, 6)

print(list(numbers))
print(type(numbers))

# --------------------------------------------

# 5. Mapping Type
# dict – Dictionary

# Stores data in key-value pairs.

employee = {
    "name": "Chandan",
    "age": 25,
    "salary": 45000
}

print(employee)
print(type(employee))

# --------------------------------------------

# 6. Set Types
# Used to store unique values.

# A. set

# Mutable collection of unique elements.

numbers = {10, 20, 30, 10}

print(numbers)
print(type(numbers))


# B. frozenset

# Immutable version of a set.

numbers = frozenset({10, 20, 30})

print(numbers)
print(type(numbers))

# --------------------------------------------


# 7. Binary Types
# Used to work with binary data.
# Type	Example
# bytes	b"Hello"
# bytearray	bytearray(5)
# memoryview	memoryview(bytes(5))


a = b"Hello"
b = bytearray(5)
c = memoryview(a)

print(type(a))
print(type(b))
print(type(c))

# --------------------------------------------

# 8. None Type
# NoneType

# Represents the absence of a value.

result = None

print(result)
print(type(result))
