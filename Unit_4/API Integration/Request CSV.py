import requests as req
import csv

response = req.get('https://dummyjson.com/posts')
data = response.json()

posts = data['posts']

with open('api_data_1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Id', 'Title', 'UserId', 'Views'])

    for p in posts:
        writer.writerow([
            p['id'],
            p['title'],
            p['userId'],
            p['views']
        ])

print('Data written successfully!!')
