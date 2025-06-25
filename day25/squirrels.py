import csv
import pandas

data = pandas.read_csv("./squirrel_census.csv")

colors = data["Primary Fur Color"].tolist()


grey = []
red = []
black = []

for color in colors:
    if color == "Gray":
        grey.append(color)
    elif color == "Cinnamon":
        red.append(color)
    elif color == "Black":
        black.append(color)

print(f"There are {len(grey)} grey squirrels")
print(f"There are {len(red)} red squirrels")
print(f"There are {len(black)} black squirrels")

data = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey), len(red), len(black)],
}
df = pandas.DataFrame(data)
df.to_csv("squirrel_color_count.csv", index=False)
