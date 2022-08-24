## An objects variables should not always be directly accessible.
## The methods can ensure the correct values are set.
## If an incorrect value is set, the method can return an error.

class Student:
    __name = "Ali Raza"
    def __init__(self):
        print(self.__name)
obj = Student()

print( )

class Student:
    __name = "Ali Raza"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("Welcome to Python Course!")
obj = Student()