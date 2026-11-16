print('--------------Python Dictionaries------------')

# Python Dictionaries

mystudents={
    "name":"mohan",
    "class":"mca",
    "address":"karnataka",
    "country":"india",
    "phone":6360487464    
}

print(mystudents)

# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(mystudents["name"])

# duplicate not allowed

mystudents={
    "name":"mohan",
    "class":"mca",
    "address":"karnataka",
    "country":"india",
    "phone":6360487464 ,  
    "phone":6360487464,
    "is_married":True,
    "friends":["mohan","soahan","roahan","anjali"]
}

print(mystudents)
print(len(mystudents))
print(type(mystudents))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# ============================================================================
# Python - Access Dictionary Items


# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x=thisdict["year"]

print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.


x=thisdict.keys()

print(x)


print('==========================================')

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# Get Values
# The values() method will return a list of all the values in the dictionary.

x=car.values()

print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

x = car.items()

print(x)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# ===========================================================

# Python - Change Dictionary Items

mystudents={
    "name":"mohan",
    "class":"mca",
    "address":"karnataka",
    "country":"india",
    "phone":6360487464    
}

mystudents["country"]="japan"

print(mystudents)


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

mystudents={
    "name":"mohan",
    "class":"mca",
    "address":"karnataka",
    "country":"india",
    "phone":6360487464    
}
mystudents.update({"address": "ranchi"})


# =====================================================

# Python - Add Dictionary Items

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# =============================================

# Python - Remove Dictionary Items

# Removing Items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.


# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# =============================================================
# Python - Loop Dictionaries

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

print('===============================================')

for x in thisdict:
  print(thisdict[x])


print('===============================================')


# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

print('===============================================')

# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

print('===============================================')


# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x,":",y)

# ========================Python - Copy Dictionaries===========

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# =====================Python - Nested Dictionaries=====================

# Python - Nested Dictionaries
# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily={
  "child1":{
    "name":"chandan",
    "class":10
  },

   "child2":{
      "name":"mohan",
      "class":12
    },

     "child3":{
        "name":"ram",
        "class":"bca"
      }

}

print(myfamily)

# ============================================================

child1 = {
  "name" : "Emil",
  "year" : 2004
}

child2 = {
  "name" : "Tobias",
  "year" : 2007
}

child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

print(myfamily["child2"]["name"])

print('========================================')

# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])