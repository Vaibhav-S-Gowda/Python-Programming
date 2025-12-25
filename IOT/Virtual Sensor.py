# Simulate a virtual sensor

import random as r
import time as t
import csv

with open('sensor_read.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Temperature'])
    '''Column headers are created for the csv file'''
    for i in range(50):
        ts = t.time()
        # Current time is captured in seconds from Unix Epach Time
        # float value
        t_c = 25 + r.uniform(-2, 2)
        # random temperature is being generated
        # random uniform unmber between -2 and 2 is generated and gets added to 25
        writer.writerow([ts, f'{t_c:.2f}'])
        # ts is stored as a number
        # t_c is formatted as a string with two decimal places
        print(ts, t_c)
        t.sleep(0.5)



