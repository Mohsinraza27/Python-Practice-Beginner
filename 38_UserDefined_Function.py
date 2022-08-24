## A Function is a block of statements which can be used reptitively-in a program.
## It saves the time of a developer.
## In Python concept of function is same as in other languages.
## You can pass 'DATA', Known as parameters, into a function.


## Creating_a_Function:
#    In Python a function is defined using the def keyword
#a = int(input("Enter your number_1:- "))
#b = int(input("Enter your number_2:- "))
def sumfunction(a, b):
    print(a + b)

def subtraction(c, d):
    print(c-d)

def multiply(e, f):
    print(e*f)
    
def divide(g, h):
    print(g/h)

def marks(a, b, c, d, e, f):
    y = (a + b + c + d + e + f)
    x = y//6
    print(y)
    print(x,"%")
    
    if x >= 85:
        print("A+ Grade")
    elif x >= 70:
        print("A Grade")
    elif x >= 55:
        print("B Grade")
    elif x >= 35:
        print('C Grade')
    else:
        print("YOU FAIL!")
    

# Calling_a_Function
sumfunction(12, 23)
sumfunction(13, 45)
subtraction(89, 23)
subtraction(90, 48)
multiply(12, 23)
multiply(34, 93)
divide(3162, 276)
divide(90, 3)
marks(23, 45, 67, 78, 55, 63)
marks(44, 55, 66, 75, 82, 70)
marks(62, 68, 74, 78, 82, 88)
marks(78, 83, 86, 92, 95, 80)

## Function_Arguments:
#   Information can be Passed to functions as parameters 




# Calling_with_Arguments



# Default_Parameter_Value




# Calling_with_Arguments




# Return_Values:
#   To let a function return a value, use the return statement    