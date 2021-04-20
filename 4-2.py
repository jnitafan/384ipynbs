import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# add in the data as a variable
data = pd.read_csv(
    "Malicious_or_criminal_attacks_breakdown-Top_five_industry_sectors_July-Dec-2019.csv", index_col=0, engine="python")

# initialize two subplots in a row, modified figsize to fit screen
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 7), dpi=100)

# set in default colours and labels,
colors = ["mediumblue", "darkviolet", "hotpink", "yellow"]
labels = ["Health service providers", "Finance", "Education",
          "Legal, Accnt & Mngmt services", "Personal Services"]
# set a simple array
x_pos = np.arange(5)
# hard coded width
width = 0.2

# create a bar graph with xpos data, for each attack variables with, colors and labels
ax[0].bar(x_pos, data.loc["Cyber incident"].values,
          align="center", width=width, color=colors[0], label="Cyber incident")
ax[0].bar(x_pos + width, data.loc["Theft of paperwork or data storage device"].values,
          width=width, color=colors[1], label="Theft of paperwork or data storage device")
ax[0].bar(x_pos + 2*width, data.loc["Rogue employee / insider threat"].values,
          width=width, color=colors[2], label="Rogue employee / insider threat")
ax[0].bar(x_pos + 3*width, data.loc["Social engineering / impersonation"].values,
          width=width, color=colors[3], label="Social engineering / impersonation")

# apply graph settings with title, label, legend and custom xtick locations
ax[0].legend()
ax[0].set_title("Type of attack by top five industry sectors")
ax[0].set_ylabel("# of attack")
ax[0].set_xticks(x_pos + width + (width/2))
ax[0].set_xticklabels(labels, rotation=33, size=10, ha="right")

# custom function to determine the height value to stack barchart lines on top of each other


def height_value(levels):
    height = np.zeros([5, ])
    for i in range(levels):
        height = np.add(height, data.iloc[i].values)
    return height


# create new bar graph with previous function, colors, labels and values
ax[1].bar(x_pos, data.loc["Cyber incident"].values,
          width, label="Cyber incident", color=colors[0])
ax[1].bar(x_pos, data.loc["Theft of paperwork or data storage device"].values,
          width, bottom=height_value(1), label="Theft of paperwork or data storage device", color=colors[1])
ax[1].bar(x_pos, data.loc["Rogue employee / insider threat"].values,
          width, bottom=height_value(2), label="Rogue employee / insider threat", color=colors[2])
ax[1].bar(x_pos, data.loc["Social engineering / impersonation"].values,
          width, bottom=height_value(3), label="Social engineering / impersonation", color=colors[3])

# apply graph settings to second graph
ax[1].legend()
ax[1].set_title("Type of attack by top five industry sectors")
ax[1].set_ylabel("# of attack")
ax[1].set_xticks(x_pos)
ax[1].set_xticklabels(labels, rotation=33, size=10, ha="right")

# move the bottom of the subplot a bit up to fit the names
plt.subplots_adjust(bottom=0.3)

# display graph in console
plt.show()
