## A dictionary is a collection of, which is unordered. In python dictionaries are written by curly brackets { }
## A dictionary has key:value pairs
# 1__Unordered datatypes
# 2__key:value 
# 3__{ }

d = {'name':'Pyhton',
     'fees':7500,
     'duration':'2_Month'}
print(d)
print(type(d))
print(d['name'])
print(d['fees'])
print(d['duration'])


## For_Loop method 
for i in d:
    print(i)
    print(d[i])
    
    
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
print(laptop_data['Dell'])
print(laptop_data['Apple'])
print(laptop_data['Acer'])

for a in laptop_data:
    print(a)
    print(laptop_data[a])
    


