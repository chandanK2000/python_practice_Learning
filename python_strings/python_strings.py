print('----------------python strings  -----------------')

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:

print("Hello")
print('Hello')


# ===================================================

# Quotes Inside Quotes

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# ===================================================


# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# ===================================================

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a="""
hello my name is chandan kumar
i am a graduate student
my professing is software engineer
"""

print(a)


# ===========================================

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

name="chandan kumar"

print(name[1])

# ======================================================

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

name="chandan kumar"

for x in name:
    print(x)

# ===========================================================
# String Length
# To get the length of a string, use the len() function.

myname="siyaram"

print(len(myname))

# ============================================================

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"

print("free" in txt)

if('free' in txt):
    print('free is available in the strings')
else:
    print('free is not available in the strings')

# ========================================================
# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)
print("best" not in txt)


# ======================slicing strings=====================

# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

b="Hello,world"

print(b[2:5])

# ======================================================
# Slice From the Start
# By leaving out the start index, the range will start at the first character:

print(b[:5])

# ===========================================================

# Slice To the End
# By leaving out the end index, the range will go to the end:

print(b[2:])
print(b)

# ===================================================

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])
print(b[:-2])

# =====================================================
# Python - Modify Strings


# Upper Case

a="Hello chandan"

print(a.upper())

# =====================================================

# Lower Case
# Example
# The lower() method returns the string in lower case:

print(a.lower())

# =====================================================

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

a = " Hello, World! "
print(a)
print(a.strip()) # returns "Hello, World!"

# =====================================================

# Replace String
# Example
# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# =====================================================

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

a="Hello, World !"

spliteted=a.split()

result=spliteted[1]

print(spliteted)
print(result)



# =======================================================

# Python - String Concatenation

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a +" "+ b
print(c)

# ==================================================
# Python - Format - Strings

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)


# ==============================================

# Python - Escape Characters

txt = "We are the so-called \"Vikings\" from the north."

print(txt)


# ==============================================

# Python - String Methods

# capitalize()	Converts the first character to upper case

a="my name is chandan kumar"
print(a.capitalize())

# casefold()	Converts string into lower case

b="CHANDAN KUMAR"

print(b.casefold())

# center()	Returns a centered string

name = "Chandan"

result = name.center(20)

print(result)


name = "Python"

result = name.center(10, "*")
result1=name.center(2,'#')

print(result)
print(result1)