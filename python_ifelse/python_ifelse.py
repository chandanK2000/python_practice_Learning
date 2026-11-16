# Python If Statement

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


a = 33
b = 200
if b > a:
  print("b is greater than a")


number = 15
if number > 0:
  print("The number is positive")


age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


# Using Variables in Conditions

is_logged_in = True
if is_logged_in:
  print("Welcome back!")


# ==================Python Elif Statement===============

# Python Elif Statement

# The Elif Keyword
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Multiple Elif Statements
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


# ================================================
# Python Else Statement

# The Else Keyword
# The else keyword catches anything which isn't caught by the preceding conditions.

# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a=20
b=30

if a<b:
  print('b is greater than a')
elif a==b:
  print('a is equal to b')
else:
  print('a is greater than b')



# ========================Python Shorthand If===========================

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

a = 5
b = 2
if a > b: print("a is greater than b")


# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

# Example

# One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B")


# ===============================================================
# Python Logical Operators


# Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# ================================================

# or operator 

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# ===============================================

# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# ==============================================

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")


# =========================Nested if ==========

score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")