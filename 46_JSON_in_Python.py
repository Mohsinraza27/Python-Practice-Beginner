## -> JSON(JavaScript Object Notation)
## -> It is mainly used for storing and transferring data between the browser and the server.
## -> JSON is test, written with JavaScript Object Notation
## -> Python to Supports JSON with a built-in package called json.

## JSON_Supports_maily_6_datatypes:
    # String
    # Number
    # Boolean
    # Null
    # Object
    # Array

import json
p = "{'name':'WS', 'lang':['Python', 'Java']}"
blog = {"URL": 'www.wscubetech', 'name':'wscubetech'}
to_json = json.dumps(blog)


d = {"cousre_name":'Python', "Fees":12000}
f = json.dumps(d)
print(f) 
print(type(f))

