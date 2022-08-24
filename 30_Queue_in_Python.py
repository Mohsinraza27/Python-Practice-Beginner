## Implement a Queue, Using a ist data_type
# The queue is a linear data structure
# It stores items in First-Out(FIFO) manner.
## Queue_OPerations:
# ENQUEUE ==>  Addsome items to the queue.
# DEQUEUE ==>  Removes an item from queue.
# FRONT   ==>  Get the front item from queue.
# REAR    ==>  Get the last item from queue.


l = [ ]
while True:
    c = int(input('''
                  1__Push Elements
                  2__Pop First Elements
                  3__Front Element
                  4__Last Element
                  5__Display Stack
                  6__Exist
                  '''))
    if c == 1:
        n = input("Enter the value 1:- ")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l)==0:
            print("Empty_Queue!")
        else:
            del l[0]
            
            print(l)
    elif c == 3:
        if len(l)==0:
            print("Empty_Queue!")
        else:
            print("First_Queue value", l[0])
    elif c == 4:
        if len(l)==0:
            print("Empty_Queue!")
        else:
            print("Last_Queue value", l[-1])
    elif c == 5:
        print("Display_Queue", l)
    elif c == 6:
        breakpoint
    else:
        print("___Invalid_syntax___")