## List comprehension is an elegant way to define and create lists based on existing list
## List comprehension is generally more compact and faster then normal functions and loop for creating list
# Syntax_of_list_comprehension
## [empression for item in list]

l = []
for a in range(1, 101):
    print(a)
    l.append(a)
print(l)

n = [m for m in range(1,101)]
print(n)

n = [m for m in range(1, 101) if m%2==0]
print(n)

n = [i for i in range(1, 101) if i%3==0]
print(n)


s = "Hello World"
d = [g for g in s]
#d = [g for g in range(len(s))]
print(d)