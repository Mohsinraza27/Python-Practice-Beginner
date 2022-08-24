import random
## Random.randit():
    # Return a number between [5 and 10 (both included)]

print(random.randint(5, 10))


## Random.randrange():
    # Return a number between [3(included) and 9(not included)]
    
print(random.randrange(3, 9))


## Random.choice():
    # Return a random element from a 'list'
    
l = ['apple', 'banana', 'cherry']
print(random.choice(l))


## Random.random():
    # Return a random float number [0 and 1]
    
r = random.random()
print(r)

## Random..shuffle():
    # Takes a sequence and returns the sequence in a random order.

l = [10, 20, 30, 40]
random.shuffle(l)
print(l)

## Random.uniform():
    # Returns a random float number between two given number
    
u = random.uniform(3, 9)
print(u)