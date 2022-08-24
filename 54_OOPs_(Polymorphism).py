## Polymorphism means same function name (but different signatures) being uses for dfferent types.
l = [10, 20, 30, 40]
print(len(l))
s = "Python"
print(len(l))


class Python:
    def display_info(self, name = " "):
        print("Welcome to Python course! " + name)
obj = Python()
obj.display_info()
obj.display_info("for Data Science")

print( )

class Py:
    def display_info(self):
        print("Welcome to Python course")
class IIP(Py):
    def display_info(self):
        print("Welcome to IIP.")
obj = IIP()
obj.display_info()
        
print( )

class Py:
    def display_info(self):
        print("Welcome to Python course")
class IIP(Py):
    def display_info(self):
        super().display_info()
        print("Welcome to IIP.")
obj = IIP()
obj.display_info()