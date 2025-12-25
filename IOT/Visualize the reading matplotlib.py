# ------------------------------------------
# Visualization of the reading (matplotlib)
# ------------------------------------------

# Interpret the data and visualize

import matplotlib.pyplot as plt
import pandas as pd

# 1. Create the data frame from the readings

df = pd.read_csv('sensor_read.csv')
print(df.shape)

# 2. Convert the string to a numeric data

print(df.columns)
df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors = 'coerce')

print(df.dtypes)

# 3. Convert Timestamp to standard date and time format

df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
print(df.head())

# 4.a Visualize the graph

print(plt.figure()) # New empty figure is created. This ensures that the graph is created on a new canvas.

# 4.b Plot the graph with x and y axis

print(plt.plot(df['Timestamp'], df['Temperature'])) # A line graph is drawn
''' x axis uses timestamp column
    y axis uses temperature column'''
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
print(plt.show())

plt.title('Raw Sensor Data') # Add a title to describe a graph
plt.xticks(rotation = 45) # The x axis lables are rotated by 45 degrees
plt.tight_layout() # The layout is adjusted such that the labels and the ticks fit inside the canvas
print(plt.show())

# Visualize the smoothened data