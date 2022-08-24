## Debugging in Python

import pdb
def sum_values(a, b):
    return a + b 


def test_function():
    
    pdb.set_trace()           ## we have added a breakpoint here. The code pause execution here
    print('This is the first line.')
    print('This is second line.')
    value = sum_values(2, 3)
    print('The code is done!')
    return value

test_function()

value = sum_values(2, 3) 
