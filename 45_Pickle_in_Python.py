## The Pickle module implements a fundamental, but powerfull algorithm for 
## serializing(store) and de-serializing a Python object structure.
# You can Pickle objects with the following datatypes:
    # Booleans 
    # Integers
    # Floats
    # Complex_Numbers
    # Strings(normal_&_Unicode)
    # Tuples
    # Lists
    # Sets
    # Dictionaries
    
## Pikling Files:
    # Pickle has two main methods.
    # The first one is dump, which dumps an object to a file object,
    # and The second one is load, which loads an object from file object.
# dump()-<=:=>-: This function is called to serialize an object hierarchy.
# loads()-<=:=>: This function is called to de-serialize a data stream

# Syntax: dump(obj, file)
# obj  == Object to be pckled
# file == File object where pickeled data will be written 
import pickle
example = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
pickle_write = open('mobile.txt', 'wb')
pickle.dump(
    example, pickle_write)
pickle_write.close()



# Syntax: file object from where the serialized data will be raad.
f = open("mobile.txt", "rb")
pickle.load(f)
print(f)