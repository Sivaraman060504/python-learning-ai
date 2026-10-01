number = [1, 2, 3, 4, 5]
result = map(lambda x : x * 10,number)
print(list(result))



square = map(lambda x : x * x , number)
print(list(square))


names = ["siva", "ravi", "kumar"]
CapNames = map(lambda x:x.upper(), names)
print(list(CapNames))