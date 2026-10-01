import json

person={
    "name":"sivaraman",
    "age":22,
    "skills":["java","sql","python"]
}

json_data= json.dumps(person)
print(json_data)