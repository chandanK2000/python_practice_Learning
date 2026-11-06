
print('----------casting example------------');

print('-------------In Python, Casting means converting one data type into another data type.----');


#1 integer casting

x=10


z=int(x);
print(z)
print(type(z))

# 2. Float casting – float()

f=100;
g=float(f)
print(f)
print(type(g))

# ========================================

# 3. String casting – str()

x = 100

y = str(x)

print(y)
print(type(y))


# ================================
# 4. Boolean casting – bool()

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))

# 5 list() – Convert to List

name="chandan";

result=list(name)
w=result[-2]

print(result)
print(type(result))
print(w)

# ======================================
# 6. tuple() – Convert to Tuple

numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
print(type(result))


# =======================================
# 7. set() – Convert to Set

numbers = [10, 20, 20, 30, 30, 40]

result = set(numbers)

print(result)
print(type(result))

# ==================================================

# 8. dict() – Convert to Dictionary

students = [("name", "Chandan"), ("age", 25), ("city", "Bangalore")]

result = dict(students)

print(result)
print(type(result))