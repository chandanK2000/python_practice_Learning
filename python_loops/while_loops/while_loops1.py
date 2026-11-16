print('---------------while loops exercise Here-----------')

# 1. Print numbers from 1 to 10 using a while loop.

i=1

while i<=10:
    print(i)
    i+=1

# 7. Print multiples of 5 from 1 to 100.

# solution 1
i = 5

while i <= 100:
    print(i)
    i += 5


print('---------------------solutions 2-------------------')

j = 1

while j <= 100:
    if j % 5 == 0:
        print(j)

    j += 1