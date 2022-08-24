## A Tuple is a collection which is ordered,
## and immutable iterating through tuple is Faster than with list


## Creating_Tuple
t = (5, 10, 15, 20, 25, 30)
print(t)
print(type(t))

## It is defined within parentheses() where items are seprated by commas.
t_1 = (20)
print(t_1)
print(type(t_1))     # <class 'int'>

t_2 = ()
print(t_2)
print(type(t_2))

t_3 = ('Python')
print(t_3)
print(type(t_3))


## Accessing Elements in Tuple
print(t[0])
print(t[3])
print(t[4])

for a in range(len(t)):
    print(a)
    print(t[a])