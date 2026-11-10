print('----------------python operators--------------')

# Python Operators
# Operators are used to perform operations on variables and values.

print(10+5)

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# ================================================================
# Python Arithmetic Operators

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# ==============================================================

# The Ternary Operator
# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)


# ==============================================================

# Python Comparison Operators


x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# ===================================================================

print('-------------logical operations--------------');
# Logical Operators
# Logical operators are used to combine conditional statements:

x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))


# ===============================================================

# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


print('----------------------------------------------------------')

# ================================================================

# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

fruits=["apple","banana","pineapple","guava"]

print("apple" in fruits)


fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)
