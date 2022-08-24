## Iterate over 2+ lists at the same time
## zip_function


# Make sure all list lenght is equal
l = [5, 10, 15, 20, 25, 30]
l1= [2, 3, 4,6, 8, 12]
l2= [43, 22, 49, 56, 29, 88]
print(l)
print(len(l))
print(l1)
print(len(l1))
print(l2)
print(len(l2))

for a, b, c in zip(l, l1, l2):
    print(a, b, c)
print()
       
    
t=len(l1)
for g in range(t):
    print(l1[g])
    print(l[g])
    print(l2[g])
    
    
    