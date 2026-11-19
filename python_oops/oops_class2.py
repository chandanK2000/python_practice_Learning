print('-----------oops class 2 example ---------')


# Private (like) attribues & methods

# conceptual implmentations in python

# private attribues & methods are meant to be used  only within  the class and
#   are not  accessible  from outside the class

class Person:

    __name="anonymous"


    def __Hello(self):
        print('hello personosn')
        

    def welcome(self):
        self.__Hello()


p1=Person()

# print(p1.__name)
# print(p1.Hello())  // this way directly we can not accessible here because this is private here sir got ?

print(p1.welcome())


# ===================== inheritance ====================

# inheritance

# when one class(child/derived) derives the  properties  & methods  of another  class(parent/base)


# class Car:

#     ->start()
# -   ->stop()

#  class ToyotaCar(Car):

#    ---------
#    ---------
#    --------

# example below :

# class Car:
#    color='black'
#    @staticmethod
#    def start():
#        print('car started')
#    @staticmethod
#    def stop():
#        print('car stopped')

       
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand



# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type=type


# car1=ToyotaCar('abc')
# this will print
# print(car1.name)  

# print(car1.start())
# print(car1.stop())
# print(car1.color)


# multilevel inheritance -> parent->child->super child(carry features from parent and child also both )
# car1=ToyotaCar('diesel')

# car1.start()
# car1.stop()


# multiple inheritance  ->

class A:
    varA='welcome to class A'

class B:
    varB='welcome to class B'

class C(A,B):
    varC='welcome to class c'


c1=C()

print(c1.varA)
print(c1.varB)
print(c1.varC)



# super method
# super() methods is  used to access methods  of the parent class

class Car:

   def __init__(self,type):
       self.type=type
    
   @staticmethod
   def start():
       print('car  already started')
   @staticmethod
   def stop():
       print('car stopped')

       
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()


car1=ToyotaCar('perius','electrical')

print(car1.type)


print('---------- class method example -----------')

# ===================================== class method ===================================
#  a class method is  boud to the  class and receives  the  class  as an  implict first arguments
# note - static method can't access or modify  class state  and generally for utility

class Person:

    name='anonymous'

    # def changeName(self,name):
    #     # self.name=name
    #     # Person.name=name
    #     self.__class__.name='rahul kumar'

    @classmethod
    def changeName(cls,name):
            cls.name=name



p1=Person()
p1.changeName('rahul kumar')

print(p1.name)
print(Person.name)



print('--------------- property decorator ------------')

# property decoractor

# 

class Student:

    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+'%'
    
    # def calpercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+'%'

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+'%'


s=Student(87,98,78)
# print(s.percentage)

s.chem=99
# print(s.chem)
# print(s.calpercentage())

print(s.percentage)

        



      

