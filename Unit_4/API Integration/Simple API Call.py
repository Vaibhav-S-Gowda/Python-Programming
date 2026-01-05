import requests as r

response = r.get('https://dummyjson.com/posts/150')
print(type(response), response)

# Check if the request was successful

if response.status_code == 200:
    print('Request Successful')
else:
    print(f'Request failed with status code: {response.status_code}')

# Check the response data
print(response.text)
print(type(response.text))

# Handle JSON responses
data = response.json()
print(f"Post Title: {data['title']}")
print(f"Post User: {data['userId']}")
