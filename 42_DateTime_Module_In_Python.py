## Import a module named datetime to work with, date time objects.

import datetime
x = datetime.datetime.now()
print(x)


# Python_Dates:
    # he method is called strftime(), and takes one parameter, format, to specify the format of returned string
    # %b ==> Month name, Short version ===> Dec
    # %B ==> Month name, Full version ===> December
    # %m ==> Month as a Number 01-12 ===> 12
    # %y ==> Year name, Short version ===> 22
    # %Y ==> Year name, Full version ===> 2022
    # %H ==> Hour 0-23 ===> 17
    # %I ==> Hour 0-12 ===> 5
    # %p ==> AM/PM ===> PM
    # %M ==> Minute 00-59 ===> 41
    
    
print(x)
year = x.strftime("%Y")
print(year)
