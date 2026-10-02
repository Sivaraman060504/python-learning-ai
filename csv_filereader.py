import pandas as pd 

df=pd.read_csv("students.csv")
print(df)

print(type(df))

# get the colummn you need 

print(df["Marks"])

print(df[df["Marks"]>80])

print(df[df["City"]=="Chennai"])

print(df.head())

print(df.head(1))
print("\ntail",df.tail())
print(df.info())
print(df.describe())