# Web scraping of Static Webpages

from urllib.request import urlopen

from bs4 import BeautifulSoup as bs  # Creating a parse tree for parsed pages that can be used to extract data from a HTML page

# ---------------------------------
# Specify the URL containing the dataset
# ---------------------------------

url = "https://tatamumbaimarathon.procam.in/results/race-results"

# ---------------------------------
# Pass the URL to urlopen() to get the HTML of the page
# ---------------------------------

html = urlopen(url) # Content is returned as a file-like object that can be read and processed

print(type(html), html)

# ---------------------------------
# Construct a BeautifulSoup object using the HTML
# ---------------------------------

soup = bs(html, 'lxml') 
''' It interprets the HTML
    It takes the unprocessed HTML text and converts it into python objects
    lxml refers to the HTML parser. 
'''

# ---------------------------------
# Extract the title of the Webpage
# ---------------------------------

title = soup.title
print(title, type(title))

# ---------------------------------
# Extract the text of the webpage
# ---------------------------------

text = soup.get_text()
# print(soup.text,"\n")
# print(text,"\n")
# print(type(text))

# ---------------------------------
# Extract useful HTML tags within the page
# ---------------------------------

soup.find_all('a')

# ---------------------------------
# Print the hyperlinks
# ---------------------------------

all_links = soup.find_all('a')
# for link in all_links:
#     print(link.get('href'))

# ---------------------------------
# Extract Tabular data 
# ---------------------------------

rows = soup.find_all('tr')
# print(rows)
# print('\n\n')
# print(type(rows))

# ---------------------------------
# Get all table rows in a list form and convert it into a dataframe
# ---------------------------------

for row in rows:
    row_td = row.find_all('td')
# print(row_td)
# print('\n\n')
# print(type(row_td))

# ---------------------------------
# Extract the data without the HTML tags
# ---------------------------------

str_cell = str(row_td)
cleantext = bs(str_cell, 'lxml').get_text()
# print(cleantext)
# print('\n\n')
# print(type(cleantext))

# ---------------------------------
# Extract the data without HTML tags using regular expressions
# ---------------------------------

import re

list_row = []
for row in rows:
    cells = row.find_all('td')
    str_cell = str(cells)
    clean = re.compile('<.*?>')
    clean_1 = (re.sub(clean, '', str_cell))
    list_row.append(clean_1)
    # print(list_row)

# ---------------------------------
# Convert it to dataframes 
# ---------------------------------

import pandas as pd
df = pd.DataFrame(list_row)
print(df.head(10))

# ---------------------------------
# Data Manipulation and Cleaning
# ---------------------------------

df1 = df[0].str.split(',', expand=True)
''' expand = True ensures that the split values are returned as seperate columns in the df'''
print(df1.head(5))

# ---------------------------------
# Remove the opening square bracket
# ---------------------------------

df1[0] = df1[0].str.strip('[')
df1.head(5)

# ---------------------------------
# Remove the closing square brackets
# ---------------------------------

df1[4] = df1[4].str.strip(']')
print(df1.head(5))

# ---------------------------------
# Get the headers for the columns
# ---------------------------------

col_labels = soup.find_all('th')
print(col_labels)
print('\n\n')
print(type(col_labels))

all_head = []
col_str = str(col_labels)
clean_text = bs(col_str, 'lxml').get_text()
all_head.append(clean_text)
print(all_head)

df2 = pd.DataFrame(all_head)
print(df2)

df3 = df2[0].str.split(',', expand=True)
print(df3.head())

df3[0] = df3[0].str.strip('[')
df3[4] = df3[4].str.strip(']')
df3.head(5)

# ---------------------------------
# Merge the two dataframes
# ---------------------------------

frames = [df3, df1]
df4 = pd.concat(frames)
print(df4.head(5))

# ---------------------------------
# Assign the first row to be the table header
# ---------------------------------

df5 = df4.rename(columns=df4.iloc[0])
print("\n",df5.head(5))

# ---------------------------------
# DROP all rows with missing values
# ---------------------------------

df5 = df5.dropna(axis=0, how='any')
print(df5.head())

# ---------------------------------
# DROP Row 0 
# ---------------------------------

df5 = df5.drop(index=1)
print(df5.head())

# ---------------------------------
# Get overview
# ---------------------------------

df5.info()
print(df.shape)

# ---------------------------------
# Processing of the dataframe
# ---------------------------------

# Convert the finish time to total number of minutes