import json

json_data='{"name":"sivaraman","age":22}'
person=json.loads(json_data)
print(person)
print(person["name"])