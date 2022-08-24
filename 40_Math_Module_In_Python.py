import math

## Math.ceil(x):
    # Return the ceiling of 'x', the smallest integer greater than and equal to 'x',
    # If 'x' is not float, delegates to x.__ceil__().
    # which should return an integral value.

    
x = 10.5
print(math.ceil(x))




## Math.fabs(x):
    # Return te absolute value of 'x'.
    
x = -11
print(math.fabs(x))



## Math.factorial(x:):
    # Return 'x' factorial as an integer raise value.
    # Error if 'x' is not integral or is negative.
    
x = 5
print(math.factorial(x))



## Math.floor(x):
    # Return the floor of 'x', the largest integer less than or equal to 'x'.
    # If 'x' is not a float, delegates to x.__floor__().
    # Which should return an integral alue
    
x = 9.5
print(math.floor(x))


## Math.fsum(Iterable):
    # Return an accurate floating point sum of values in the iterable.
    
l = [10, 20, 30, 40, 50]
print(math.fsum(l))



## Math.sqrt(x):
    # Return the square root of 'x'
    
print(math.sqrt(25))