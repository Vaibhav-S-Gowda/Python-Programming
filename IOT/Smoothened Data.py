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