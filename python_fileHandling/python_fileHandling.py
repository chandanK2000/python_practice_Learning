print('---------python file handling example below -------------')


# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:


# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

file = open("demo.txt", "w")

file.write('Hello txt')


file=open('student.txt','w')

file.write("Name: Chandan\n")
file.write("Course: Python\n")
file.write("Experience: 3 Years\n")

file.close()


file=open('student.txt','r')

data=file.read()

print(data)


file = open('student.txt', 'a')

file.write('\nExperience: 10 Years')

file.close()


file=open('student.txt','r')

data=file.read()

print(data)


# file = open('employee.txt', 'x')

# file.write('Employee Name: Chandan')

# file.close()


# Read existing employee.txt file

file = open('employee.txt', 'r')

data = file.read()

print(data)

file.close()


print('=====================================')
f = open("student.txt", "r")

# print(f.readline())   return first line 
# print(f.readlines())  return all lines with a list 

# data=f.read(5)

print(f.read(10))
print(f.read(5))
print(f.read(5))
print(f.read(5))

f.close()

import os

os.remove('student.txt')

if os.path.exists('student.txt'):
    os.remove('student.txt')
else:
    print('the file does not exists')


