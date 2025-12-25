# Simulation of Sensor Data

import random as r
import time as t

for i in range(10):
    t_c = 25 + r.uniform(-2, 2)
    print(f'Reading {i+1}: {t_c:.2f} C')
    t.sleep(2)


