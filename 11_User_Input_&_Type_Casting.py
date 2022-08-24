# input(), int(), float(), and eval()

#a = input("Enter your number: ")
#b =34             TypeError: can only concatenate str (not "int") to str

#print(a+b)

# Always input function return 'str' so, we can convert (str into int) using int() 
a = int(input("Enter your number: "))  
c = 76
print(a + c)     

course_name = input("Enter your Course name you have enrolled: ")
course_duration = input("Enter your course duration: ")

print("Your course name is", course_name, ", And your course duration is", course_duration)

x = 23
g = float(x)     # 23.0
y = 78
h = float(y)     # 78.0
print(g+h)       # 132.0


e = input("Enter value: ")     # 34
f = input("Enter value: ")     # 45
print(e + f)                   # 3445

e = eval(input("Enter value: "))
f = eval(input("Enter value: "))     
print(e + f)                   

# e = 0b1010
# f = 20
# print(eval(e + f))             TypeError: eval() arg 1 must be a string, bytes or code object

a = '25'
b = eval(a)
c = 78.8
h = 99
print(eval(b + h + c))