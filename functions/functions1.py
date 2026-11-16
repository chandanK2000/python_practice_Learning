print('-----------------------functions example in python -------------------------')

# 1. Create a function that prints Hello World.

def Helloworld():
    print('Hello')

Helloworld()

# 2. Create a function that prints your name.

def myname():
    print('chandan kumar')

myname()

# 3. Create a function that prints your name, age, and city.

def mydetails():
    name="chandan"
    age=26
    city="bangalore"
    print(f"my  name is {name},age is  {age} and i belong from {city}")

mydetails()


# 4. Create a function that prints numbers from 1 to 10.

def printNumbers():
    for x in range(1,11):
        print(x)

printNumbers()

# 5. Create a function that prints all even numbers from 1 to 50.

def evenNumbers():
    for x in range(1,51):
        if x%2==0:
            print(x)


evenNumbers()


# 6.  a function that prints all odd numbers from 1 to 50.

def oddNumbers():
    for x in range(1,51):
        if x%2!=0:
            print(x)


oddNumbers()


print('============================================')

# 7. Create a function that prints the multiplication table of 5.

def tablePrint():
    x=6
    for a in range(1,11):
        print(a*x)

tablePrint()


# 8. Create a function that prints the multiplication table of any number.

# num=int(input('ener your Number Please')) 

# def anytablePrint():
#     print(num)
#     for a in range(1,11):
#         print(a*num)

# anytablePrint()


# 9. Create a function that prints the first 10 natural numbers.

print('==================print natural Numbers=================')

def NaturalNumbers():
    i=1
    while(i<=10):
        print(i)
        i+=1


NaturalNumbers()


# 10. Create a function that prints the square of numbers from 1 to 10.

def SquareNumbers():
    i=1
    while(i<=10):
        print(i*i)
        i+=1


SquareNumbers()


# 11. Create a function that displays a welcome message.

def greetings(name):
    return f"welcome {name}"



print(greetings('chandan'))

# 12. Create a function that displays a menu for a calculator.

print('========== CALCULATOR MENU ==========')

def calculator_menu():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    print('=====================================')

calculator_menu()

# 18. Create a function that prints a list of fruits.

def printFruits(fruits):
    for x in fruits:
        print(x)


printFruits(["apple","mango","litchi","banana","pomegrantate"])



# 19. Create a function that displays the current year.

from datetime import datetime

def current_year():
    year = datetime.now().year
    print(f"Current Year: {year}")

current_year()


# 20. Create a function that prints a message five times.

# def RepeatedMessage():
#     for message in range(1,6):
#         print('Hello chandan How are You !')

# RepeatedMessage()


def RepeatedMessage(message,count):
    for i in range(count):
        print(message)

RepeatedMessage('Hello chandan How are You !',5)
RepeatedMessage('i am python developer!',3)



