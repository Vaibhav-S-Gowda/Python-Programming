import requests as req
import xml.etree.cElementTree as et

response = req.get('https://dummyjson.com/posts/120')

if response.status_code == 200:
    print('Request Successful')
else:
    print(f'Request failed: {response.status_code}')

print(type(response.text), response.text)

data = response.json()
print(data)

root = et.Element("post")

id_el = et.SubElement(root, "id")
id_el.text = str(data["id"])

title_el = et.SubElement(root, "title")
title_el.text = str(data["title"])

user_el = et.SubElement(root, "userId")
user_el.text = str(data["userId"])

tree = et.ElementTree(root)
tree.write("api_data.xml", encoding="utf-8", xml_declaration=True)

print("Data stored successfully.")
