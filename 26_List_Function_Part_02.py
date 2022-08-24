## count(), max(), min(), sort(), reverse(), and index()

l = [5, 10, 15, 20, 25, 30]
print(l)
l.count(15)
print(l.count(15))
l = [5, 10, 15, 20, 25, 30, 15, 45, 56, 78, 15]
print(l)
print(l.count(15))

l = [5, 10, 15, 20, 25, 30]
m = max(l)
print(m)

l = [5, 10, 15, 20, 25, 30]
n = min(l)
print(n)

l = [5, 10, 15, 20, 25, 30, 0, 1, 2, 35, 40, 45, 50, 3, 4]
l.sort()
print(l)

l.reverse()
print(l)

l.index(10)
print(l)
l.index(10, 1, 50)
print(l)