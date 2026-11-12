
print('----------------python set example in python----------')

# 1. Create an empty set in Python.

myset={}

print(myset)

# 2. Create a set containing 5 integer values.

myset={2,4,5,6,7,8,9,1}

print(myset)

# 3. Create a set containing 5 string values.

myset={"apple","mango","litchi","orange","pomegranate"}

print(myset)

# 4. Create a set containing integers and strings.

myset={"apple","mango","litchi",5,7,8,10,True,False}

print(myset)

# 5. Create a set with duplicate values and print it.

myset={"apple","litchi",10,10,"apple"}

print(myset)
print(len(myset))
print(type(myset))

# 8. Create a set using the set() constructor.

myset=set(("apple","litchi",10,10,"apple"))

print(myset)
print(type(myset))

# 9. Convert a list into a set.

fruits=["apple","mango","litchi","orange"]

mysets=set(fruits)

print(fruits)
print(myset)
print(type(mysets))

# 12. Create a set containing 10 numbers and print it.

numbers={10,20,34,56,12,23,45,65,34,87}

print(numbers)

for x in numbers:
    print(x)


myset = set()

if not myset:
    print("Set is empty")
else:
    print("Set is not empty")

myset = {10, 20, 30}

if len(myset) == 0:
    print("Set is empty")
else:
    print("Set is not empty")


# 14. Create an empty set and add 5 elements.

myset=()
# Create an empty set
myset = set()

print(myset)
print(type(myset))

# Add 5 elements
myset.add(10)
myset.add(20)
myset.add(30)
myset.add(40)
myset.add(50)

print(myset)
print(type(myset))


myset=set(range(1,21))

print(myset)


