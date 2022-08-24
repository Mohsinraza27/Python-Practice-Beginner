# Python chr(), and ord()

## chr()
# This takes in an integer i and convert it to character c, 
# So, it returns a character string.

# convert integer 65 to ASCII
# Character ('A')
y = chr(65)
print(y, type(y))
y = chr(74)
print(y)
y = chr(82)
print(y)
y = chr(91)
print(y)
y = chr(96)
print(y)

a = 68
print(chr(a))
b = 79
print(chr(b))

## ord()
# This takes a single unicode character(String_of_Lenght) and returns an integer,
# convert ASII unicode charcter 'A' to 65
y = ord('A')
print(y, type(y))
h = 'F'
print(ord(h))          # Capital letter start(A, B, C,...) 65
h = 'f'
print(ord(h))          # Small letter start(a, b, c,....) 97
g = 'M'
print(ord(g))
g = 'm'
print(ord(g))