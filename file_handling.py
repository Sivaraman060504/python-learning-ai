file =open("sample.txt","r")
content = file.read()
print(content)
file.close()

with open("sample.txt","r") as file:
    content=file.readlines()
    print(content)






with open("sample.txt","r", encoding="utf-8") as file:
    content = file.readline()
    print(content)




with open("sample.txt","w",encoding="utf-8") as file:
     file.write("hello python")
   