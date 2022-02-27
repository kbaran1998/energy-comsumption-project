import pandas as pd


data = pd.read_csv("venv\Demo.csv")
# for col in data.columns:
#     print(col)

#extract column values until first NaN
index = data["GT Frequency(MHz)"].last_valid_index()   
print(data["System Time"].iloc[:index+1])
