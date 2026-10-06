import pandas as pd

students =pd.DataFrame({
    "student_id":[1,2,3,4],
    "name":["siva","ela","naveen","neam"]
})
marks=pd.DataFrame({
    "student_id":[1,2,3],
    "mark":[90,80,60]
})

df = pd.merge(students,marks,on="student_id")
print(df)