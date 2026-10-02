import pandas as pd 
data = [10,20,30,40,50]
series=pd.Series(data)
print(series)

#access the value using the index here 


#Series = one column

print("\nindex of 1",series[0])
print(series[3])

marks = pd.Series(
    [90,80,70],
    index=["siva","naveen","ela"]
)

print("\nmarks:",marks)
print(marks["siva"])

#data frame = multpile column 


data ={
    "Name":["siva","naveen","ela"],
    "age":[21,20,19],
    "marks":[90,80,70],
}

dataframe = pd.DataFrame(data)
print(dataframe)

print(dataframe[["Name","marks","age"]])

print(dataframe.shape)

#printing teh columns 
print(dataframe.columns)

# using info get some basic information here 
print(dataframe.info())