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





