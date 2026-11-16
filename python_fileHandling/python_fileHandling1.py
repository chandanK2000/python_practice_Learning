print('--------------python file handling example belwo ------------')

# 2. Create a file called hello.txt.

file = open('hello.txt', 'w')

text = 'hello i am chandan kumar'

file.write(text)

print(text)

file.close()


# 3. Write Hello Python into a file.

file=open('hello.txt','w')
text='hello python'

file.write(text)

print(text)

file.close()

# 4. Write your name, age and city into a file.

file = open('details.txt', 'w')

file.write('Name: Chandan Kumar\n')
file.write('Age: 25\n')
file.write('City: Bangalore\n')

file.close()

print('Data written successfully!')


# 5. Write five different lines into a file.


file = open('lines.txt', 'w')

file.write('My name is Chandan.\n')
file.write('I am learning Python.\n')
file.write('I am a software developer.\n')
file.write('I am learning file handling.\n')
file.write('I want to become a full-stack developer.\n')

file.close()

print('Five lines written successfully!')

readfile=open('lines.txt','r')

data=readfile.read()

print(data)

print('==============================================')

# 8. Create a file using x mode.

# 1. What is 'x' mode in Python?
# 'x' means Exclusive Creation Mode.

# It is used to create a new file, but there is one important condition:
# - If the file does not exist → Python creates it.
# - If the file already exists → Python raises FileExistsError.


# file = open('student.txt', 'x')

# file.write('Hello, I am learning Python')

# file.close()

# print('File created successfully!')


# 1. What is Append Mode ('a')?
# Append mode is used to add new content to an existing file without deleting its previous content.
# - If the file exists → Adds content at the end.
# - If the file doesn't exist → Creates a new file.

file = open('student.txt', 'a')

file.write('\nCity: Bangalore')

file.close()

print('New content added successfully!')


print('----------------------------------------------')

# Category 2: Reading Files (16–30)
# Focus: read(), readline(), readlines()


# 16. Read the complete content of a text file.

import os

if os.path.exists('details.txt'):

    f = open('details.txt', 'r')

    print(f.read())

    f.close()

else:
    print('File does not exist')

print('---------------------------------------------')

# 17. Read only the first five characters using read(5).

if os.path.exists('details.txt'):

    f = open('details.txt', 'r')

    print(f.read(5))

    f.close()

else:
    print('File does not exist')


print('----------------------------------------------')
# 19. Read the first line using readline().

f= open('details.txt', 'r')
print(f.readline(10))
print(f.readline(10))
f.close()