## del , pop(), remove(), and clear(), 
l = [5, 10, 15, 20, 25, 30]
print(l)
del l[2]
print(l)
del l[4]
print(l)


l = [5, 10, 15, 20, 25, 30]
print(l)
print(l.pop(3))
print(l)
print(l.pop(1))
print(l)

l = [5, 10, 15, 20, 25, 30]
print(l)
print(l.remove(30))
print(l)
l.remove(5)
print(l)

l = [5, 10, 15, 20, 25, 30]
print(l)
print(l.clear())
print(l)
l = [5, 10, 15, 20, 25, 30]
print(l)
l.clear()
print(l)


## Update_element_from_List
# Update list, insert(), append(), and extends()

l = [5, 10, 15, 20, 25, 30]
print(l)
l[0]=1
print(l)
l[2]=5
print(l)
l[4]=45
print(l)
l[5]=67
print(l)

l = [5, 10, 15, 20, 25, 30]
print(l)
l.insert(5, 40)
print(l)
l.insert(6, 50)
print(l)
l.insert(8, 55)
print(l)
print(l.insert(0, 1))
l.insert(0, 1)
print(l)

l = [5, 10, 15, 20, 25, 30]
print(l)
l.append(40)
print(l)
l.append(45)
print(l)
l.append(50)
print(l)

l = [5, 10, 15, 20, 25, 30]
print(l)
l.extend('Hello')
print(l)
l.extend('Python')
print(l)