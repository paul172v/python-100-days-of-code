import csv
import pandas

data = pandas.read_csv("./weather_data.csv")

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

max = data["temp"].max()
# print(max)

## To read row
data[data.day == "Monday"]


# print(data[data.temp == max])


monday = data[data.day == "Monday"]

monday_temp = monday.temp

monday_fahrenheit = (monday_temp * 1.8) + 32

print(monday_fahrenheit)
