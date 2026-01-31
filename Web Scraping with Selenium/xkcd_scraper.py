import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# Just downloading the first 5 for a test
for i in range(5):
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comicElem = soup.select('#comic img')
    if comicElem != []:
        comicUrl = 'https:' + comicElem[0].get('src')
        print(f'Downloading image {comicUrl}...')
        res = requests.get(comicUrl)
        res.raise_for_status()

        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imgFile:
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')