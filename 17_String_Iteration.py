w = 'Welcome to Python'
t = len(w)
print(t)

for n in range(t):
    print(n)
    print(w[n])
# w[0] = W
# w[1] = e


## Reverse method
w = 'Welcome to Python'
r = w[-1: : -1]
print(r)

for a in range(t-1, -1, -1):
    print(a)
    print(w[a])
    
## second method
for n in w:
    print(n)