import pandas as pd 

data ={
    "name":["siva","naveen","ela","nithish"],
    "city":["banglore","pondy","banglore","pondy"],
    "marks":[90,80,70,60]
}

df = pd.DataFrame(data)

res1= df.groupby("city")["marks"].sum()
res2= df.groupby("city")["marks"].count()
res3= df.groupby("city")["marks"].min()
res4= df.groupby("city")["marks"].mean()
res5 = df.groupby("city")["marks"].agg(["mean","max","min","count"])

print(df)
print("sum by city",res1)
print(res2)
print(res3)
print(res4)
print(res5)