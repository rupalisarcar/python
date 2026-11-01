import os
import csv

file_path = os.path.dirname(os.path.abspath(__file__))

new_file_path = os.path.join(file_path,"weather_data.csv")

# with open(new_file_path,"r") as weather_file:
#     print(weather_file.readlines())

# with open(new_file_path,"r") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv(new_file_path)
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

total_temp = sum(temp_list)
avg_temp = total_temp/len(temp_list)
print(avg_temp)

max_data = data["temp"].max()
print(max_data)

print(data[data["temp"]==max_data])

monday = data[data["day"]=="Monday"]
print((monday["temp"]*1.8)+32)