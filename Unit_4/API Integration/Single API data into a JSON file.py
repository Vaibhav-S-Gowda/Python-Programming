import requests as r
import json

# Get the data from an API call
response = r.get("https://dummyjson.com/posts/149")
data = response.json()
print(data)

# Save the data into a JSON file with formatting
with open('api_data.json', 'w') as f:
    json.dump(data, f, indent = 4)
print('Data saved to file')
