print('---------  polymorphism in python example below -------')

# polymorphism:-  operator overlaoding

#  when the same operator is  allowed to have  different meaning  according to the context

print(1+2)

print(type(1))

print('appna'+' '+'college')

print(type('aapna'))

print([1,2,4,5]+[3,6,8,9,10])

print(type([1,2,4,5]))


# 

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i+",self.img,'j+')

    # def add(self,num2):
    #     newReal=self.real+num2.real
    #     newImg=self.img+num2.img
    #     return Complex(newReal,newImg)

    def __add__(self,num2):  # this __add__ is called here dunder function in polymorphism
            newReal=self.real+num2.real
            newImg=self.img+num2.img
            return Complex(newReal,newImg)
    
    def __sub__(self,num2):
            newReal=self.real-num2.real
            newImg=self.img-num2.img
    
            return Complex(newReal,newImg)


num1=Complex(1,3)

num1.showNumber()

num2=Complex(5,8)

num2.showNumber()

# num3=num1+num2
num3=num1-num2

# num3=num1.add(num2)

num3.showNumber()

print('---------------------practice question in oops in python ----------')


# practice questions 

class Circle:
      def __init__(self,radius):
           self.radius=radius

      def Area(self):
            return (22/7)*self.radius**2

      def Perimeter(self):
            return 2*(22/7)*self.radius
      
                  
cir=Circle(21)

print(cir.radius)

print(cir.Area())
print(cir.Perimeter())

            
