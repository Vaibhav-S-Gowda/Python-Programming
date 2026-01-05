import requests as r
import json
import csv

response = r.get("https://dummyjson.com/posts/149")

# Convert the data into JSON object
data = response.json()

#save single api data into csv file
with open('api_data.csv','w',newline="")as f:
    writer=csv.writer(f)
    writer.writerow(['Id','Title','Body','userId'])
    writer.writerow([data['id'],data['title'],data['body'],data['userId']])
print('Data stored in a csv file.')