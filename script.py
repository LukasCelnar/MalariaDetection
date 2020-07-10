"""
Script that creates labels.csv file with
Filenames in first column and labels in second
column where 1 = Parasitized and 0 = Uninfected
"""

# Import modules
import os
import pandas as pd

# Dataset file path
path = "./cell_images"

# Variables with filenames
parasitized = os.listdir(path + "/Parasitized")
uninfected = os.listdir(path + "/Uninfected")

# Dataframe 1 thats gonna hold parasitized cell pictures
df1 = pd.DataFrame(columns=["Filenames", "Parasitized"])

# Loop throw filenames and add them to Filenames column
# Add 1 to Parasitized column which means cell is parasitized
df1["Filenames"] = [picture for picture in parasitized]
df1["Parasitized"] = [1 for i in range(len(parasitized))]

# Drops last row which contains .db file
df1 = df1[:-1]

# Dataframe 2 thats gonna hold uninfected cell pictures
df2 = pd.DataFrame(columns=["Filenames", "Parasitized"])

# Loop throw filenames and add them to Filenames column
# Add 1 to Parasitized column which means cell is uninfected
df2["Filenames"] = [picture for picture in uninfected]
df2["Parasitized"] = [0 for i in range(len(parasitized))]

# Drops last row which contains .db file
df2 = df2[:-1]

# Append dataframes together
df = df1.append(df2)

# Save in csv format
df.to_csv("labels.csv", index=False)