print('============python range example=========')
# Python range


# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# This set of numbers has its own data type called range.

# Creating ranges
# The range() function can be called with 1, 2, or 3 arguments, using this syntax:

# range(start, stop, step)

x=range(10)

print(x)

print(list(x))

# Call range() With Two Arguments
# If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.

# range(3, 10) returns a sequence of each number from 3 to 9:


# Create a range of numbers from 3 to 9:

x = range(3, 10)

print(x)

print(list(x))


# Call range() With Three Arguments
# If the range function is called with three arguments, the third argument represents the step value.

# The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.

# range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:


x = range(3, 10, 2)

print(x)

print(list(x))

for x in range(0,10,2):
    print(x)

# ==================================================================

# Using List to Display Ranges
# The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.

# Therefore, ranges are often converted to lists for display.

# Example
# Convert different ranges to lists:

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))


# ==================================================

# Slicing Ranges
# Like other sequences, ranges can be sliced to extract a subsequence.

# Example
# Extract a subsequence from a range:

r = range(10)
print(r[2])
print(r[:3])


r = range(0, 10, 2)
print(len(r))