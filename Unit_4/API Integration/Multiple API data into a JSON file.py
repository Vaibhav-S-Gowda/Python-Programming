import requests as r
import json

response = r.get("https://dummyjson.com/posts")

# Convert the data into JSON object
data = response.json()
print(data)

# ----------------------------
# Save the data into JSON file
# ----------------------------

# Process data into individual records
posts_list = []
for post in data['posts']:
    posts_list.append({'id': post['id'],
                       'title': post['title'],
                       'body': post['body'],
                       'userId': post['userId'],
                       'reactions': post['reactions']}
                       )
print()
print(posts_list)

# Store the data into a JSON file
with open('api_data_1.json', 'w') as f:
    json.dump(posts_list, f, indent = 4)
print('Data stored successfully!')

