import pandas
import os

file_path = os.path.dirname(os.path.abspath(__file__))
new_file_path = os.path.join(file_path,"2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


squirral_data = pandas.read_csv(new_file_path)
gray_clr = (squirral_data["Primary Fur Color"]=="Gray").sum()
black_clr = len(squirral_data[squirral_data["Primary Fur Color"]=="Black"])
cinamon_clr = (squirral_data["Primary Fur Color"]=="Cinnamon").sum()

new_csv = {
    "Fur Color": ["Gray","Red","Blak"],
    "Count":[gray_clr, cinamon_clr, black_clr]
    }

data = pandas.DataFrame(new_csv)
new_csv_path = os.path.join(file_path,"new_csv.csv")
data.to_csv(new_csv_path)
