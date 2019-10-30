import os
import pandas as pd

print(os.listdir(".")) # list of current dir content

entries = ["a", "b", "c"]
for index, value in enumerate(entries):
  print(f"{index}, {value}")

data = pd.read_csv("./homework_02/iris.csv")

print(type(data))
# <class 'pandas.core.frame.DataFrame'>

print(data.head())
print(data.info())
print(data.describe())
print(data['Species'].value_counts())
# Iris-setosa        50
# Iris-versicolor    50
# Iris-virginica     50
# Name: Species, dtype: int64


rows, col = data.shape
