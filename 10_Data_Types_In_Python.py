# --> Numeric Type
# < Integers >
# < Float >
# < Complex_Number >

# --> Sequence Type
# < String >
# < List >
# < Tuple >

# --> Dictionary
# --> Set

##  Mutable Datatypes
# Mutable object can change it's state or contents
# > List
# > Dictionary
# > Byte Array

## Immutable Datatypes
# ImMutable object cannot change it's state or contents
# > Integers
# > Float
# > Complex_Number
# > String
# > Tuple
# > Set


## Numbers
a = 5
print(a, "is of type", type(a))
print(a, "is", type(a), "Type!")
a = 4.6
print(a, "is", type(a), "Type..")
a = 1 + 2j
print(a, "is", type(a), "Type..")


## String
# A string is a collection of one or more characters
# put in a 'Single-quote', "Double-qoutes" or '''Triple-qoutes'''
# Multi line strings can be denoted using triple qoutes, '''or'''
s = "Hello@123"
print(s)
print(s, type(s))
str_ = "Hello Python Strigs"
print(str_)
print(str_, type(str_))
s = '10'
print(s)
print(s, type(s))
print(str_+"_" +s)


## List
# List is an odered sequence of items.
# It is the one of the most used datatype in Python and is very flexible
# []  
a = [1, 2.4, 'P10']
print(a)
print(a, type(a))

l = [10, "Hello", 20, "Python", 30, "Course", "!"]
print(l)
print(l, type(l))

# Check that list is 'Mutable'
print(l)
l[4]="Easy"   # or l[-3]="Easy" 
print(l)


## Tuple
# Tuple is an ordered sequence of items same as a list
# It is defined within parentheses() where items are seprated by commas.
t= (4, 'Program', 2.5, 1+3j)
print(t)
print(t, type(t))

t1 = ("hello", 12, "This", 45, 78.9)
print(t1)
print(t1, type(t1))

t2 = (10)     # <class 'int'>
print(t2)     # because this value is not in seprated commas
print(t2, type(t2))


## Dictionary
# Dictionary is an unordered collection of key-value pairs.
# In Python, dictionaries are defined within braces{} with each item being a pair form key:value
d = {1:"value", 
     "key": 2}
print(d)
print(d, type(d))

d1 = {'course':"Python10",
      'course_duration': "2Month"}
print(d1)
print(d1, type(d1))
print(d1['course'])
print(d1['course_duration'])

d2 = {'daba': 'Box', 
      'kursi': 'Chair', 
      'pankha': 'Fan'}
print(d2, type(d2))
print(d2['pankha'])


## Set
# Set is an unordered collection of items.
# Every set element is unique(no-duplicate) and must be immutable(not-changable)
my_set = {1, 2, 3}
print(my_set)
print(my_set, type(my_set))

st = {1, 2, 4, 6, 3, 5, 2, 7, 9,6, 7}
print(st)
print(st, type(st)) 