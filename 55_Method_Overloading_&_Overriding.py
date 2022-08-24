## Method Overloading 

# Method overloading is one concept of polymorphism.
# It comes under the elements of OOPs.
# It worked in the same method names and different arguments.
# Arguments different will be based on a number of argumets and types of arguments.
class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Area of Rectangle: ", (a*b))
        elif a != None:
            print("Area of Square: ", (a*a))
        else:
            print("Nothing to find!")
obj = Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10, 30)            
    
print()

## Mehod Overriding
# Method overriding is the method having the same name with same arguments.
# It is implemented with inheritance also..
# It mostly used for memory reducing processes.
class A:
    def show_Data(self):
        print("I'm in A")
class B(A):
    def show_Data(self):
        print("I'm in B")
obj = B()
obj.show_Data()