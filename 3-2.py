import pandas as pd

# import df as a dataframe
df = pd.read_csv("result_withoutTotal.csv")

# add a new column, and assign a value to it via a formula
df["Total"] = 0.05 * (df["Ass1"] + df["Ass3"]) + 0.15 * \
    (df["Ass2"] + df["Ass4"]) + 0.6 * df["Exam"]

# round off the weird floating point errors to two decimal places
df["Total"] = df["Total"].round(2)

# add the total df to the final df
df["Final"] = df["Total"].round(0)

# if a value is bigger than 100, set it to 100
for value in df["Total"]:
    if value > 100:
        value = 100

# this is also one way to do the code below with fewer lines
# df["Grade"] = "HD"

# df.loc[df["Total"] <= 79.45, "Grade"] = "D"
# df.loc[df["Total"] <= 69.45, "Grade"] = "C"
# df.loc[df["Total"] <= 59.45, "Grade"] = "P"
# df.loc[df["Total"] <= 49.45, "Grade"] = "N"

# create a new column and fill it it with empty objects
df["Grade"] = ""

# iterate through the data with iterrows()
for index, row in df.iterrows():
    # if item is in range, then assign a result depending on value
    if 79.45 <= row["Total"] <= 100:
        df.at[index, "Grade"] = "HD"
    elif 69.45 <= row["Total"] <= 79.45:
        df.at[index, "Grade"] = "D"
    elif 59.45 <= row["Total"] <= 69.45:
        df.at[index, "Grade"] = "C"
    elif 49.45 <= row["Total"] <= 59.45:
        df.at[index, "Grade"] = "P"
    elif 0 <= row["Total"] <= 49.45:
        df.at[index, "Grade"] = "N"

# display the columns
print("column names: ")
print(df.columns.values)
# students with exam score < 48
print("students with exam score < 48: ")
print(df.loc[df["Final"] < 48])
# students with exam score > 100
print("students with exam score > 100 ")
print(df.loc[df["Final"] > 100])

# write the data to a csv
df.to_csv("result_updated.csv", index=False)

# find the students who passed and remove them from the table
df.drop(df.loc[df["Final"] > 48].index, inplace=True)
# then print the data to a csv
df.to_csv("failedhurdle.csv", index=False)
