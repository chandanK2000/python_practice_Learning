print('------------Python Lists-----------')

# List
# Lists are used to store multiple items in a single variable.


thislist=['apple','banana','cherry']

print(thislist);

print(len(thislist))

# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.


# List Items - Data Types


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

print(type(list3))


# ===================================================================

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


thislist=['apple','banana','cherry','litchi','mango','pomegranate','jackfruits']


print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])
print(thislist[-4:-1])

available = 'litchi'

if available in thislist:
    print(available, 'is available in the list')
else:
    print(available, 'is not available in the list')


if available not in thislist:
    print(available, 'is not available in the list')
else:
    print(available, 'is available in the list')


# ==================================================================

print('---------------change list items----------------------------')

thislist[1]='blackcurrant';

print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# =====================================================================

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist.insert(1,'anar')

print(thislist)


# =======================================================
# Python - Add List Items

mystudents=['mohan','sohan','roahan','anjali','anamika','rahul']

print(mystudents)

mystudents.append('sital')

print(mystudents)

# insert items

mystudents.insert(1,'sujan')

print(mystudents)

# extend list

mystudents2=['radha','rani','rajani','ankita','anarkali','rajani']

mystudents.extend(mystudents2);

print(mystudents)

# =========================================================
# Python - Remove List Items

# Remove Specified Item
# The remove() method removes the specified item.

mystudents.remove('sital')

print(mystudents)

# Remove Specified Index
# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
# del thislist

print(thislist)

# ========================================================

# clear the list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# ============================================================

# Python - Loop Lists

for x in mystudents:
    print(x)


for i in range(len(mystudents)):
    print(mystudents[i])


print('-----------------list comprehension---------')
# ==================================================
# Looping Using List Comprehension

[print(x) for x in mystudents]


# mystudents.sort()

print(mystudents)

# mystudents.sort(reverse=True)

mystudents.reverse()

print(mystudents)

# ================================copy list ===========================

# Python - Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(thislist)
print(mylist)


# Use the list() method
# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# ==============================join list ==========================


# Python - Join Lists

# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


