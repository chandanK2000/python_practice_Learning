print('----------------python List example below---------------')


# 1. Create a list containing five fruit names.

fruits=['apple','mango','litchi','pomegrantate','balckcurrant']


# 3. Create a list containing numbers from 1 to 10.

numbers=[1,2,3,4,5,6,7,8,9,10]

for x in numbers:
    print(x)

# 4. Create a list containing five different data types.

mylist=[2,"chandan",3.5,False,None]

print(mylist)

# 5. Create an empty list and print it.

mylist1=[]
print(mylist1)


# 6. Create a list containing duplicate numbers.

mylist2=[3,6,7,9,10,2,10,2,7,8,10]

print(mylist2)

mylist = ["Apple", 100, "Banana", 200, "Cherry", 300]

print(mylist)

print(type(mylist))


# ==========================================================
# Category 2: Accessing List Elements (13–27)

print(mylist[1])

# 15. Access the last element using a positive index.

last_elements=fruits[len(fruits)-1]

print(last_elements)

# 16. Access the last element using a negative index.

print(fruits[-1])

# 17. Access the third element from the end.

print(fruits[-3])

# 18. Access the first three elements using slicing.

print(fruits[0:3])

# 19. Access the last three elements.

print(fruits[-3:])

# 20. Access elements from index 2 to index 5.

print(fruits[2:5])


# 21. Print all elements except the first element.

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print(fruits[1:])

# 22. Print all elements except the last element.

print(fruits[:-1])

# 23. Access elements using a negative slice.


fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print(fruits[-4:-1])

# 24. Extract alternate elements using slicing.


fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange", "Litchi"]

print(fruits[::2])
print(fruits[::3])

# 25. Reverse a list using slicing.

print(fruits[::-1])

# 26. Access every second element starting from index 1.


fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange", "Litchi"]

print(fruits[1::2])


# 27. Print the middle element of a list with an odd number of elements.

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

middle = len(fruits) // 2

print(fruits[middle])


# ===========================================================

print('-------------------Category 3: Updating List Elements (28–39)----------')


# 28. Change the first element of a list.

fruits[0]='jackfruits'
print(fruits)

# 29. Change the last element of a list.

fruits[len(fruits)-1]='anar'
print(fruits)












