import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import data via pandas into a variable
data = pd.read_csv("attack-type-frequency.csv", index_col=0, engine="python")

# plot as multiple subplot with a modifed figsize to fit my screen
fig, ax = plt.subplots(1, 2, figsize=(10, 5), dpi=100)

# set matplot colors
colors = ["blue", "red", "green", "yellow"]

# create a new pandas series from the category value, and count the times appeared
data_frequency = data["category"].value_counts()
# sort the data alphabetically (sorting index since it's made of strings)
data_frequency = data_frequency.sort_index()

# create a bar plot with (x,y,center aligned, set colors)
ax[0].bar(data_frequency.index, data_frequency.values,
          align="center", color=colors)

# set the barplot labels
ax[0].set_xlabel("Attack Categories")
ax[0].set_ylabel("Number of attack types in each category")
ax[0].set_title("Attack Categories and # of attack types in Cyber Security")

# create a pie plot with(x,labels, colors, % cut values)
ax[1].pie(data_frequency.values, labels=data_frequency.index,
          colors=colors, autopct="%1.1f")

# show it in console
plt.show()
