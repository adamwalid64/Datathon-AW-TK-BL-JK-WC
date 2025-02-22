import pandas as pd
import matplotlib.pyplot as plt 

file = "C:\\Users\\willi\\OneDrive\\Documents\\Parking_Violations_-_2023_-_Present.csv"
df = pd.read_csv(file)
column = "description"
data = df["description"].value_counts()
total_sum = data.sum()
threshold_value = total_sum * 0.018
other_data = data[data < threshold_value]
data = data[data >= threshold_value]
data["Other"] = other_data.sum()
data = data.sort_values(ascending=False)
color_map = [
    "#ffe0b3",
    "#ffcc80",
    "#ffb84d",
    "#ff9900",
    "#ff7f00",
    "#e67300",
    "#cc6600",
    "#b35900",
    "#9f4d00",
    "#8c4000",
    "#803300",
    "#732600",
    "#661a00",
    "#5a0e00",
    "#4d0000",
    "#440000",
    "#3b0000",
    "#330000",
    "#290000",
    "#1f0000",
]
colors = (color_map * (len(data) // len(color_map) + 1))[:len(data)]
plt.figure(figsize=(12, 12))
plt.pie(data, labels=data.index, autopct="%1.1f%%", startangle=140, colors=colors)
plt.title(f"Distribution of {"Parking Violations by Type"}")
plt.show()
