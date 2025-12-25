# Write the CSV Files - To write into CSV it has to be List of Lists

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Abbot', 11, 'BLR'],
    ['Shannu', 30, 'HNR'],
    ['Bob', 40, 'MLR']
]

with open('output_data.csv','w') as f:
    write = csv.writer(f)
    write.writerows(data)

with open('output_data.csv','a') as f:
    write = csv.writer(f)
    write.writerow(['Dean', 11, 'Manchester'])
    write.writerow(['eDGAR', 20, 'PARIS'])

