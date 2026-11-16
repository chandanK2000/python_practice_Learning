print('=====================range example in python ==================')

# 1. Print numbers from 0 to 9 using range().

x=range(0,10)

print(x)
print(list(x))\

for x in range(0,10):
    print(x)

print('----------------------------------------')
# 2. Print numbers from 1 to 10.

for x in range(1,11,1):
    print(x)

# 7. Print numbers from 20 to 30.

for x in range(20,31):
    print(x)

print(list(range(20,31)))

# =======================================================

# B. Range with step (16–30)

# 16. Print even numbers from 2 to 20.

for x in range(2,20,2):
    print(x)

print('----------print odd Numbers---------')

# 18. Print odd numbers from 1 to 99.

for x in range(1,99,2):
    print(x)

print('----------print step 5 Numbers---------')

# 21. Print numbers from 1 to 100 with a step of 5.

for x in range(1,100,5):
    print(x)

print('-----------------Print multiples of 7----------')

# 26. Print multiples of 7 from 7 to 100.

for x in range(7,100,7):
    print(x)

# ==================================================

# C. Reverse range (31–40)


# 31. Print numbers from 10 to 1 in reverse.

for x in range(10,0,-1):
    print(x)


# 32. Print numbers from 20 to 1 in reverse.

for x in range(20,0,-1):
    print(x)

print('------------------------------------')

# 35. Print numbers from 50 to 10 in reverse.

for x in range(50,9,-1):
    print(x)


# ==============D. Basic mathematical problems (41–50)========================

# D. Basic mathematical problem


print('-----------------------------------------------')
# 41. Calculate the sum of numbers from 1 to 10 using range().

total=0


for x in range(1,11):
    total=total+x
print(total)


# 43. Calculate the sum of even numbers from 1 to 50.

sumeven=0


for x in range(0,51,2):
    sumeven=sumeven+x
print(sumeven)


# 45. Print the square of numbers from 1 to 10.

for x in range(1,11):
    print(x*x)



print('---------Table of 5th----------------')

# 47. Print multiplication table of 5.


for x in range(5,51,5):
    print(x)
print('---------Table of 5th----------------')


for x in range(1,11):
    print(f"5 x {x} = {5*x}")


# 49. Count how many numbers exist between 1 and 100.

count=0

for x in range(2,100):
    count+=1
print(count)

print('-------------product of number 1 to 5---------')
# 50. Calculate the product of numbers from 1 to 5.

product=1
for x in range(1,6):
    product*=x

print(product)



# ===================================================================

# Part 2 – Medium Level (51–100)
# Intermediate

# E. Conditional logic with range() (51–65)




