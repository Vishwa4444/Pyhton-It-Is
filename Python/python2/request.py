import json
# json1 = '{"name":"vishwa","age":21}'
# dict1 = json.loads(json1)
# print(dict1['name'])
#
#
dict1 = {'name':'vishwa','age':21}
json1 = json.dumps(dict1)
print(type(json1))