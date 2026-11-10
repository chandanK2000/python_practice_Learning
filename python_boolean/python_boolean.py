print(10>9)
print(10==9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool('Hello'))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


username = "Chandan"
password = ""

if bool(username):
    print("Username is entered")
else:
    print("Username is missing")

if bool(password):
    print("Password is entered")
else:
    print("Password is missing")

def myfucntion():
   return True


if myfucntion:
   print('yes')
else:
   print('no !')