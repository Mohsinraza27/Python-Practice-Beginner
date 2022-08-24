print('''+ ADDTION
- Substraction
* Multiplication
/ Divide''')

num1 = int(input("Enter your number_1:- "))
num2 = int(input("Enter your number_2:- "))
opr = input("Enter your Operater(+, -, *, /):- ")

if opr=='+':
    print(num1+num2)
elif opr=='-':
    print(num1-num2)
elif opr=='*':
    print(num1*num2)
elif opr=='/':
    print(num1/num2)
else:
    print("Invalid Syntax!")


# We can use (Only_If)
num1 = int(input("Enter your number_1:- "))
num2 = int(input("Enter your number_2:- "))
opr = input("Enter your Operater(+, -, *, /):- ")
if opr=='+':
    print(num1+num2)
if opr=='-':
    print(num1-num2)
if opr=='*':
    print(num1*num2)
if opr=='/':
    print(num1/num2)
if opr != '+' and opr != '-' and opr != '*' and opr != '/':
    print("Invalid Syntax!")