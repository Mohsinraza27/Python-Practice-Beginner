# (&) AND, (|) OR, and (^) XOR


# 1 = TRUE,  0 = FALSE
a = 0
b = 0
print(a&b)
print(a|b)
print(a^b)

a = 0
b = 1
print(a&b)
print(a|b)
print(a^b)

a = 1 
b = 0
print(a&b)
print(a|b)
print(a^b)

a = 1 
b = 1
print(a&b)
print(a|b)
print(a^b)

# check binary value
x = 10
y = 8
print(bin(x))            # 0b1010
print(bin(y))            # 0b1000
                         #   1000
print(x&y)               # 8 
print(x&y, bin(x&y))     # 8 0b1000


print(bin(x))            # 0b1010
print(bin(y))            # 0b1000
                         #   1010
print(x|y)               # 10
print(x|y, bin(x|y))     # 10 0b1010


print(bin(x))            # 0b1010
print(bin(y))            # 0b1000
                         #   0010
print(x^y)               # 2
print(x^y, bin(x^y)      # 2 0b10