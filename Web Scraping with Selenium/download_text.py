import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
print("File downloaded successfully!")