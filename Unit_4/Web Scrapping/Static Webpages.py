from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# URL
# ---------------------------------

url = "https://tatamumbaimarathon.procam.in/results/race-results"
html = urlopen(url)
soup = bs(html, "lxml")

# ---------------------------------
# Title
# ---------------------------------

print(soup.title.text.strip())

# ---------------------------------
# Extract table
# NOTE: Page is JS-rendered, so this will usually return empty.
# Code is defensive and will not crash.
# ---------------------------------

table = soup.find("table")

if table is None:
    print("No static table found. Page content is JavaScript-rendered.")
    exit()

# ---------------------------------
# Extract headers
# ---------------------------------

headers = [th.get_text(strip=True) for th in table.find_all("th")]

# ---------------------------------
# Extract rows
# ---------------------------------

rows = []
for tr in table.find_all("tr"):
    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
    if cells:
        rows.append(cells)

# ---------------------------------
# Create DataFrame
# ---------------------------------

df = pd.DataFrame(rows, columns=headers)
print(df.head())

# ---------------------------------
# Basic Cleaning
# ---------------------------------

df.columns = df.columns.str.upper().str.replace("\n", " ", regex=False)
df = df.dropna(how="any")

# ---------------------------------
# Convert FINISH TIME → minutes
# ---------------------------------

def time_to_minutes(t):
    try:
        h, m, s = map(int, t.split(":"))
        return (h * 3600 + m * 60 + s) / 60
    except:
        return None

if "FINISH TIME" in df.columns:
    df["RUN_MINS"] = df["FINISH TIME"].apply(time_to_minutes)
    df = df.dropna(subset=["RUN_MINS"])
else:
    print("FINISH TIME column not found.")
    exit()

print(df.head())

# ---------------------------------
# Visualization
# ---------------------------------

plt.hist(df["RUN_MINS"], bins=10)
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.title("Finish Time Distribution")
plt.show()

plt.boxplot(df["RUN_MINS"])
plt.ylabel("Minutes")
plt.title("Finish Time Boxplot")
plt.show()

if "NATIONALITY" in df.columns:
    df["NATIONALITY"].value_counts().plot(kind="bar")
    plt.title("Runners by Nationality")
    plt.show()

    df.groupby("NATIONALITY")["RUN_MINS"].mean().plot(kind="bar")
    plt.title("Average Finish Time by Nationality")
    plt.show()

if "RANK" in df.columns:
    plt.scatter(df["RANK"].astype(int), df["RUN_MINS"])
    plt.xlabel("Rank")
    plt.ylabel("Finish Time (mins)")
    plt.title("Rank vs Finish Time")
    plt.show()

top10 = df.nsmallest(10, "RUN_MINS")

plt.barh(top10["NAME"], top10["RUN_MINS"])
plt.xlabel("Minutes")
plt.title("Top 10 Fastest Runners")
plt.show()

plt.plot(df["RUN_MINS"].expanding().mean())
plt.title("Expanding Mean of Finish Time")
plt.ylabel("Minutes")
plt.show()


'''
This website cannot be scraped fully with BeautifulSoup alone
The results table is populated via JavaScript. Your original approach cannot work reliably.

Correct tool for real data
If you actually need the results:

selenium

OR direct API calls (preferred)

OR browser network inspection

Regex-based HTML stripping is incorrect
BeautifulSoup already provides clean text safely.

Your plotting depended on Run_mins, which never existed
This was a guaranteed runtime failure.

'''