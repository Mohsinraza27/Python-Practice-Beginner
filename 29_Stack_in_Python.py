## Implement a stcack, Using a ist data_type
## Stack_in_Python
# The stack is a linear data_structure.
# It stores items in a Last-in/First-out(LIFO) or First-in/Last-out(FILO)
## Stack_Operations:
# PUSH    ==>  Inserting on Element
# POP     ==>  Deleting An Element
# PEEK    ==>  Display the Last Element
# DISPLAY ==>  Display_List 


l = [ ]
while True:
    c = int(input('''
                  1__Push Elements
                  2__Pop Elements
                  3__Peak Elements
                  4__Display Stack
                  5__Exist
                  '''))
    if c == 1:
        n = input("Enter the value 1:- ")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l)==0:
            print("Empty_Stack!")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l)==0:
            print("Empty_Stack!")
        else:
            print("Last_Stack value", l[-1])
    elif c == 4:
        print("Display_Stack", l)
    elif c == 5:
        breakpoint
    else:
        print("___Invalid_syntax___")