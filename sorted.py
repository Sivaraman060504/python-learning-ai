students =[
    ("siva",90),
    ("ravi",80),
    ("ganesh",100),
    ("abi",90)
]

result = sorted(students,key= lambda x:x[0],reverse=True)
print(result)