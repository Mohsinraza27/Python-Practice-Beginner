# (If), (If, else), and (If, elif, else)

# if[conditional expression]:
#    [statement(s) to execute]
a =10
if a%2==0:
    print("Even number")
b = 9
if b%2==0:
    print("Even number")
    

# if[conditional expression]:
#    [statement(s) to execute]
# else:
#    [alternate statement to execute]
a =10
if a%2==0:
    print("Even number")
else:
    print("Odd number")
    
a =45
if a%2==0:
    print("Even number")
else:
    print("Odd number")
    
    
# if[conditional expression]:
#    [statement(s) to execute]
# elif[conditional expression]:
#    [statement to execute]
# else:
#    [alternate statement to execute]
per = 55
if per>=60:
    print("First Divsion!")
elif per>=48:
    print("second Divson!")
elif per>35:
    print("Third Dision")
else:
    print("Fail")
    
marks = int(input("Enter your marks: "))
if marks>=80:
    print("First Divsion!")
elif marks>=65:
    print("second Divson!")
elif marks>40:
    print("Third Dision")
else:
    print("Fail")
    
marks = int(input("Enter your marks: "))
if 100>=marks>=80:
    print("First Divsion!")
elif 100>=marks>=65:
    print("second Divson!")
elif 100>=marks>40:
    print("Third Dision")
else:
    print("Fail!")