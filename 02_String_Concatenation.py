a = "Hello"
b = "Python"

print(a+b)
print(a + " " + b)

a = 23
b = 67
print(a + b)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# you can add only string to string and integer to integer
# c = "67"
# print(a+c)

d = 98
print(type(d))
# <class 'int'>
f = 34
print(type(f))
# <class 'int'>
print(f+d)

str_1 = "Python is Open"
print(type(str_1))
# <class 'str'>
str_2 = "Source Language and Easy to Learn!"
print(type(str_2))
# <class 'str'>
print(str_1 + str_2)
print(str_1 + " " + str_2)

print(d)
# <class 'int'>
print(str_1)
# <class 'str'>

# print(d + str_1)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# You can Covert 'string into Integer'

g = 45       # this is integer class type
h = str(g)   
# you can convert 'integer to string and string to integer
# This method is called 'Type Casting'
k = " Fortyfive"    # this is string class type
print(h + k)

# Type Casting another Example
v = '78'
x = int(v)
p = 123
print(x + p)
# print(v + p)    TypeError: can only concatenate str (not "int") to str
