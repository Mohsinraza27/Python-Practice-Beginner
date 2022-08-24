## If you have a JSON, you can parse it by using the json.loads() method
import json
d = "{'course':'Pyhton', 'fees':12000, 'duration':'2 Months'}"
x = json.loads(d)
print(type(x))
print(x)

for a in x:
    print(a, x[a])