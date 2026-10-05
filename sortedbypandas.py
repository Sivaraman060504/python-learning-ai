import pandas as pd
df = pd.read_csv("students.csv")
resultDes = df.sort_values("Marks")
resultAse = df.sort_values("Marks",ascending=False)
df["Passed"]= True
print(resultDes)
print(resultAse)
print(df)   