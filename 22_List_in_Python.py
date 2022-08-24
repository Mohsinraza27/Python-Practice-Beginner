## List is a Mutable
## [ ]
## Enter the value with comma_saperated(,)
## List store Multiple value with comma saperated 
# e.g. Number, String, list, Tuple, and Dictionary 


l = [1, 2, 3, 4, 5]
print(l)
print(type(l))


## Nested_List
l_1 = [1, 2, 3, 4, [7, 8, 9, 12]]
print(l_1)
print(type(l_1))

 
## List_slicing
print(l[3])
print(l[1])
print(l[0:3])
print(l[2:4])
print(l[:])
print(l[1:])

print(l_1[4][3])
print(l_1[4][2])
print(l_1[4][0:3])
print(l_1[1: :4])
print(l_1[1: :2])
print(l_1[: : 2])


## reverse_list
# Method_01
print(l)
print(l_1)
print(l[-1: :-1])
print(l_1[-1: :-1])
# Method_02
l.reverse()
print(l)
l_1.reverse()
print(l_1)
print(l.reverse())