## Program to convert string to a List
## split(), function


a = input("Enter your value:- ")
print(a)
l = a.split()

l = [ ]
for x in range(1, 6):
    a = input("Enter your value" +str(x)+ ":-")
    l.append(a)
print(l)
    