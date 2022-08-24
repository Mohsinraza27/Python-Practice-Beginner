# find(), index(), isalpha(), isdigit(), and isalnum()

w =  "Welcome to Python"

print(w.find('l'))
print(w.find('y'))
print(w.find('o'))
print(w.find('o', 5))
print(w.find('t', 9))
print(w.find('z'))        # If the value is not in variable then this print (-1)

print(w.index('e'))
print(w.index('m'))
print(w.index('h', 4))
# print(w.index('i'))       # ValueError: substring not found

x = 'Python'
print(x.isalpha())
x1 = 'Puthon course'
print(x1.isalpha())        # It returns 'False' because use of 'space'
                          # It always return 'False' use 'special character' and 'Number' and 'Space'
x2 = 'Python 3.10'
print(x2.isalpha())
  

x3 = '1234'
x4 =  'Python@3.10'
print(x.isdigit())
print(x1.isdigit())
print(x2.isdigit())    
print(x3.isdigit())
# print(x4.isdigit())   AttributeError: 'int' object has no attribute 'isdigit'
                    

print(x.isalnum())
print(x1.isalnum())
print(x2.isalnum())
print(x3.isalnum())
print(x4.isalnum())