import requests as req

try:
    response = req.get('https://dummyjson.com/posts/2400')
    response.raise_for_status()
    # Raise an exception for 4**, 5** errors
    data = response.json()
    print(f'Retrived {len(data)} records')
except req.exceptions.HTTPError as e:
    print(f'HTTP Error: {e}')
except req.exceptions.ConnectionError as e:
    print(f'Connection Error: Check internet connection {e}')
except req.exceptions.Timeout as e:
    print(f'Timeout Error: Took too long to respond {e}')
except req.exceptions.RequestException as e:
    print(f'Error in making request {e}')
except ValueError:
    print('Error in passing the JSN response')