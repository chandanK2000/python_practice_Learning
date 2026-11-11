print('-------------python tuples1 excercise started from here--------')

# level a

# 1. Create an empty tuple.

list=()
print(list)

# 2. Create a tuple containing five integers.

integerstuples=(10,20,30,34,67,89)
print(integerstuples)

# 3. Create a tuple containing five strings.

stringsTuples=("mohan","sohan","rohan","anjali","anamika","anawar","shyam")

print(stringsTuples)

# 9. Create a tuple containing student names and roll numbers.

# this type of tuple is called the nested tuples 
students=(
    ("mohan",101),
    ("sohan",102),
    ("rohan",103),
    ("rahima",104),
    ("anamika",105),
    ("rajani",106)
)

print(students) 

# 11. Create a tuple containing a single element.

tuple1=("ram",)

print(type(tuple1))

# 13. Create a tuple using the tuple() constructor.

tuple2=tuple((10,20,30,40))

print(tuple2)

print(type(tuple2))

# 14. Convert a list into a tuple.

students=["rahima","mohan","sohan","ranjan","rahim","raja","Anawar"]

print(students)
print(type(students))

studentsTuples=tuple(students)

print(studentsTuples)
print(type(studentsTuples))

# 15. Convert a string into a tuple.

mystrings="rahim"

mytuples=tuple(mystrings)

print(mytuples)
print(type(mytuples))

# ======================================================

# B. Accessing tuple elements

# 16. Create a tuple and print its first element.

fruits=("apple","mango","litchi","cherry","blackcurrant","guava")

print(fruits)
print(fruits[1])

# 17. Print the last element using positive indexing.


mytuple = (10, 20, 30, 40, 50)

print(mytuple[len(mytuple) - 1])

# 18. Print the first element using negative indexing.

mytuple = (10, 20, 30, 40, 50)

print(mytuple[-5])

# 19. Print the last element using negative indexing.

print(mytuple[-1])

# 22. Print all elements using indexing.

mytuple = (10, 20, 30, 40, 50)

for i in range(len(mytuple)):
    print(mytuple[i])

# 23. Access an element using a variable as an index.

mytuple = (10, 20, 30, 40, 50)

index = 2

print(mytuple[index])


# 24. Access the middle element of an odd-length tuple.

mytuple = (10, 20, 30, 40, 50)

middle = len(mytuple) // 2

print(mytuple[middle])

# 25. Access the middle two elements of an even-length tuple.

mytuple = (10, 20, 30, 40, 50)

middle = len(mytuple) // 2

print(mytuple[middle-1])


# =======================================================

# C. Tuple slicing













