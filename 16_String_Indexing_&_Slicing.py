##indexing
# -17|-16|-15|-14|-13|-12|-11|-10|-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |
#  W | e | l | c | o | m | e | _ | t | o | _ | P | y | t | h | o | n | 
#  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 

w = 'Welcome to Python'
print(len(w))

print(w[6])
print(w[12])
print(w[9])

## Slicing
print(w[0:7])
print(w[0:])
print(w[8:17])
print("next")

print(w[0: :2])
print(w[1:10:2])
print(w[7:17:3])
print("next")

print(w[-1:])
print(w[-10:-1])
print(w[-12:-2:-1])
print("next")

# reverse method
print(w[-1:-10:-2])
print(w[-1: :-1])
print(w[-2:-15:-2])