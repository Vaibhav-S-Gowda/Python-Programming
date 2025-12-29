import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('sensor_read.csv')

df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors = 'coerce')

df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

df['Value'] = pd.to_numeric(df['Temperature'], errors= 'coerce')

df['Value_Smooth'] = df['Value'].rolling(window= 5, min_periods= 1).mean()
# A rolling mean is calculated
# windows = 5 means each point is replaced with the average of itself and four previous values
# min_periods = 1 means that the calculation will start immediately

print(df.head())

plt.figure()
plt.plot(df['Timestamp'], df['Value'], label = 'Raw', alpha = 0.5) # alpha creates transparency of the visualization to see over lapping points or lines
plt.plot(df['Timestamp'], df['Value_Smooth'], label =  'Smoothened')
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Raw v/s Smoothened Senson Data')
plt.legend()
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# ----------------------------
# Mean of Temperature Readings
# ----------------------------

mid_index = len(df)//2

first_half_mean = df['Value_Smooth'].iloc[:mid_index].mean()
second_half_mean = df['Value_Smooth'].iloc[mid_index:].mean()

print(f'Mean of First half: {first_half_mean} \nMean of Second half: {second_half_mean}')

