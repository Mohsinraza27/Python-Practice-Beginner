#class A:
#    def displayA(self):
#        print("Welcome to Python Course! A")
#class B:
#    def displayB():
#        print("Welcome to Python Course! B")
        
#obj = B()
#obj.displayA()
#obj.displayB()



class A:
    def displayA(self):
        print("Welcome to Python Course! A")
class B(A):
    def displayB(self):
        print("Welcome to Python Course! B")
        
obj = B()
obj.displayA()
obj.displayB()

print("")

class A:
    def displayA(self):
        print("Welcome to Python Course! A")
class B(A):
    def displayB(self):
        print("Welcome to Python Course! B")
class C(B):
    def displayC(self):
        print("Welcome to Python Course! C")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

print("")

class A:
    def displayA(self):
        print("Welcome to Python Course! A")
class B():
    def displayB(self):
        print("Welcome to Python Course! B")
class C(A, B):
    def displayC(self):
        print("Welcome to Python Course! C")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()