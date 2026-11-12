print('----------------Python Sets------------------')

# Python Sets

myset = {"apple", "banana", "cherry"}

print(myset)


# Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Python - Access Set Items

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# ====================================================================

# Python - Add Set Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset.add('blackcurrant')

print(thisset)

# ==============================================================

# Python - Remove Set Items

# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# clear method

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

# del thisset

print(thisset)


# Python - Loop Sets

thissets={"apple","banana","litchi","mango","orange"}

for x in thissets:
  print(x)


# ===================================================

# Python - Join Sets

# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# Union
# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.

# The result will be a set.


x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# Update
# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# Python frozenset

# Python frozenset
# frozenset is an immutable version of a set.

# Like sets, it contains unique, unordered, unchangeable elements.

# Unlike sets, elements cannot be added or removed from a frozenset.


# Creating a frozenset
# Use the frozenset() constructor to create a frozenset from any iterable.


x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))