## get(), keys(), values(), and items()


my_dict = {
    'course'  : 'Python',
    'fees'    :  8000,
    'duration': '2 Month'
    }

print(my_dict)

# .get()
print(my_dict.get('fees'))
print(my_dict.get('course'))
print(my_dict.get('duration'))

# .keys()
print(my_dict.keys())

# .values()
print(my_dict.values())

# .items()
print(my_dict.items())

my_dict = {
    'course_1'  : 'Python',
    'fees_1'    :  8000,
    'duration_1': '2 Month',
    'course_2'  : 'Java_script',
    'fees_2'    : 9000,
    'duration_2': '2.5 Month',
    }
for a in my_dict:
    print(a)
for a, b in my_dict.items():
    print(a, b)
for a in my_dict.keys():
    print(a)
for a in my_dict.values():
    print(a)


laptop_data = {
    'HP'     : 'Notebook 14-df0008nx',
    'Lenovo' : 'IdeaPad 330S-14IKB',
    'Huawei' : 'MateBook D Volta',
    'Dell'   : 'Inspiron 15 3567',
    'Asus'   : 'VivoBook 15 X510UR',
    "Apple"  : 'MacBook Air (Retina)',
    'Acer'   : 'Swift 5 SF514-52TP-8933'
    }
print(laptop_data)

# .get()
print(laptop_data.get('fees'))
print(laptop_data.get('course'))
print(laptop_data.get('duration'))

# .keys()
print(laptop_data.keys())

# .values()
print(laptop_data.values())

# .items()
print(laptop_data.items())


for a in laptop_data:
    print(a)
for a, b in laptop_data.items():
    print(a, b)
for a in laptop_data.keys():
    print(a)
for a in laptop_data.values():
    print(a)

