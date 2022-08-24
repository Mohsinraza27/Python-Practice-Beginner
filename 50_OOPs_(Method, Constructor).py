class DemoClass:
    a = 28
    def showvalue(self):
        print(self.a)
obj = DemoClass()
obj.showvalue()


class DemoClass:
    a = 28
    def showvalue(self):
        self.c = self.a*self.a
        print(self.c)
obj = DemoClass()
obj.showvalue()


class DemoClass:
    a = 28
    def showvalue(self):
        print("Welcome to Python Course!")
obj = DemoClass()
obj.showvalue()


class DemoClass:
    a = 28
    def showvalue(self, a, b):
        print(a+b)
obj = DemoClass()
obj.showvalue(23, 78)




class DemoClass:
    def __init__(self):
        print("Welcome to Python Course!")
obj = DemoClass()
