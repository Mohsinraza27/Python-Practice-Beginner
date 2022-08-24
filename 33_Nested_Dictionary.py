## Nested_Dictionary:- Nested_dictionary means putting a dictionary inside another dictionary.
## It's a collecting a dictionaries into a single dictionary


# Created_Nested_Dictionary
laptop_data = {
    'HP'      : {'laptop_name':'Notebook 14-df0008nx',    'display_size' :14,   'processor_type' : 'Intel Celeron N4000',     'disk_space' : '64 GB (eMMC)',      'price_in_$' :1259},
    'Lenovo'  : {'laptop_name':'IdeaPad 330S-14IKB',      'display_size' :14,   'processor_type' : 'Intel Core i5-8250U',     'disk_space' : '1 TB HDD',          'price_in_$' :2099},
    'Huawei'  : {'laptop_name':'MateBook D Volta',        'display_size' :14,   'processor_type' : 'Intel Core i5-8250U',     'disk_space' : '256 GB SSD',        'price_in_$' :3799},
    'Dell'    : {'laptop_name':'Inspiron 15 3567',        'display_size' :15.6, 'processor_type' : 'Intel Core i3-7020U',     'disk_space' : '1 TB HDD',          'price_in_$' :1849},
    'Asus'    : {'laptop_name':'VivoBook 15 X510UR',      'display_size' :15.6, 'processor_type' : 'Intel Core i7-8550U',     'disk_space' : '1 TB HDD',          'price_in_$' :3149},
    'Apple'   : {'laptop_name':'MacBook Air (Retina)',    'display_size' :13.3, 'processor_type' : 'Intel Core i5 Dual Core', 'disk_space' : '128 GB (PCIe SSD)', 'price_in_$' :5199},
    'Acer'    : {'laptop_name':'Swift 5 SF514-52TP-8933', 'display_size' :14,   'processor_type' : 'Intel Core i7-8550U',     'disk_space' : '512 GB SSD',        'price_in_$' :5999}, 
    }
print(laptop_data)

print()
print(laptop_data['HP'])
print()
print(laptop_data['Lenovo'])
print()
print(laptop_data['Huawei'])
print()
print(laptop_data['Dell'])
print()
print(laptop_data['Asus'])
print()
print(laptop_data['Apple'])
print()
print(laptop_data['Acer'])
print()

for i in laptop_data.keys():
    print(i)
    print(laptop_data[i])
print(laptop_data['HP']['laptop_name'])
print()
print(laptop_data['Lenovo']['laptop_name'])
print()
print(laptop_data['Huawei']['laptop_name'])
print()
print(laptop_data['Dell']['laptop_name'])
print()
print(laptop_data['Asus']['laptop_name'])
print()
print(laptop_data['Apple']['laptop_name'])
print()
print(laptop_data['Acer']['laptop_name'])
print()

print(laptop_data['HP']['disk_space'])
print()
print(laptop_data['Lenovo']['disk_space'])
print()
print(laptop_data['Huawei']['disk_space'])
print()
print(laptop_data['Dell']['disk_space'])
print()
print(laptop_data['Asus']['disk_space'])
print()
print(laptop_data['Apple']['disk_space'])
print()
print(laptop_data['Acer']['disk_space'])
print()

for a, b in laptop_data.items():
#    print(a, b)
    print(a, ':-' ,b['laptop_name'],':' ,b['display_size'],':' ,b['processor_type'],':' ,b['disk_space'],':' ,b['price_in_$'])