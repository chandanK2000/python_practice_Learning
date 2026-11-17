print('-------python oops example in python below---------')


# class Student:
#     name="chandan"
#     age=26
#     address='bangalore'


# s=Student()
# s1=Student()

# print(s)
# print(s1)
# print(s.name)
# print(s.age)
# print(s.address)

# print('------------ s1 ---------')

# print(s1.name)
# print(s1.age)
# print(s1.address)


class Student:

    # defatult constructor
    def __init__(self):
        pass

    # paramaterized constructor
    def __init__(self, name,marks,email,address,age,phone):
        self.name=name     
        self.marks=marks
        self.email=email
        self.address=address
        self.age=age
        self.phone=phone
        print('adding new student in database')


# creating object 
s1=Student('chadan',67,'ck933970@gmail.com','bangalroe',26,7648764873)

print(s1.name,s1.marks,s1.email,s1.address,s1.age,s1.phone) 

print('--------------mohan Details---------------')

s2=Student('mohan',77,'mohan@gmail.com','ranch',27,9873843864833)

print(s2.name,s2.marks,s2.email,s2.address,s2.age,s2.phone) 


print('------- class attribute and object attributes -----')


# class attribute and object attributes



class Teacher:

    # defatult constructor
    def __init__(self):
        pass
    city='patna'

    # paramaterized constructor
    def __init__(self, name,email,address,age,phone):
        self.name=name     
        self.email=email
        self.address=address
        self.age=age
        self.phone=phone
        print('adding new Teacher in database')

    def welcome_teacher(self):
        print('welcome teacher',self.name)

    def get_address(self):
        return self.address


# creating object 
t1=Teacher('siyaram','ck933970@gmail.com','bangalroe',26,7648764873)

print(t1.name,t1.email,t1.address,t1.age,t1.phone) 
print(t1.city)

print('--------------mohan Details---------------')

t2=Teacher('samim','mohan@gmail.com','ranchi',27,9873843864833)

print(t2.name,t2.email,t2.address,t2.age,t2.phone) 
print(t2.city)
print(Teacher.city)
t2.welcome_teacher()
print(t2.get_address())




# notes: always  obj attributs precedence is greater than class attributes (obj attr > class attr)

# methods
# ->methods are functionstion that belong to objects


class Persons:
      def __init__(self,name,age):
          self.name=name
          self.age=age
            
      def greet(self):
          print("Hello,my name is",self.name)

p1=Persons("John",36)
print(p1.name,p1.age)
p1.greet()

# =========================================================================

print('----------------class 2 -------- ')

print('----static method------')

# static method

# methods that don't use the self parameter(work as class level)

# decorator allows us to  wrap another fucntion  in order to  extend the behaviour  of the 
# wrapped  function  without permanently modifying it

class College:
    def __init__(self,cname,caddress):
        self.cname=cname
        self.caddress=caddress

# static method -> without decorator self 
    @staticmethod    
    def HelloCollege():
        print('my college located is haryana')

c=College("abc college",'bangalore')

print(c.cname,c.caddress)
c.HelloCollege()

# ========================================================================

print('------------------abstraction in python')

# Abstraction 
# -> hiding the implementation detaisl of  a class and only showing the essentials features  to the user


# encapsulation 

# -> wrapping data  and functions into a single  unit(objects)

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def startCar(self):
        self.acc=True
        self.clutch=True
        print('car started  successfully !')

car1=Car()
car1.startCar()




class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        # Internal implementation
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful!")

    def check_balance(self):
        print("Available Balance:", self.balance)


# Create object
account = BankAccount(10000)

# User operations
account.withdraw(2000)
account.check_balance()



# Q create account class  with 2 attributes - balnace and account number  create method for  debit,credit
#  & printing the  balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        print('successfuly created my account')

    # debit methood
    def debit(self,amount):
        self.balance-=amount
        print('Rs',amount,'was debited')
        print('total balance =',self.get_balance())

    # credit methoud
    def credited(self,amount):
        self.balance+=amount
        print('Rs',amount,'was credited')
        print('total balance =',self.get_balance())


    # get balance methoud
    def get_balance(self):
        return self.balance



acc1=Account(10000,123456789)
print(acc1.balance)
print(acc1.account_no)

print('--------------------------------')

acc1.debit(1000)
acc1.credited(500)

print('-------------------------acc2-----------')

acc2=Account(12000,123456767023)
print(acc1.balance)
print(acc1.account_no)

print('--------------------------------')

acc1.debit(1500)
acc1.credited(12500)
acc1.credited(1500)





# ============================== del keyword ===============

# del keyword
#  used to delted object properties or  object itself

# del s1.name
# del se

class fruits:
    def  __init__(self,fname):
        self.fname=fname

f1=fruits('apple')

print(f1.fname)
# del f1

f1.fname='manago'
print(f1.fname)
        








