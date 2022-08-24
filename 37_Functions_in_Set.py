## set(), add(), pop(), remove(), clear(), discard(), and update()
s = {3, 7, 9, 12, 15 ,19, 22, 34}
print(s)
print(type(s))

# set()
l = [1, 2, 3, 4, 5]
print(l)
print(type(l))
print(set(l))    # {1, 2, 3, 4, 5}

# add()
print(s)
s.add(40)
print(s)

# pop()
print(s.pop())

# remove()
s.remove(19)
print(s)
s.remove(40)
print(s)

# discard()
s.discard(22)
print(s)

# clear()
s.clear()
print(s)

# update()
print(s)
print(l)
s.update(l)
print(s)